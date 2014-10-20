import sys
from bs4 import BeautifulSoup
from htmldom import htmldom
import requests
import urllib
import math
import random
from operator import itemgetter

# ISSUES
# - quite slow
#   * research into techniques to improve text analysis
# - filter out obviously unrelated pages?
# - not all notes have a useful set of tags
#   * if small no. of tags then apply text analysis to define top relevant
#     keywords that accurately describe the nature of the note

base_url = 'http://en.wikipedia.org'
subject = ''

def is_disambiguation_page(soup):
    return soup.find('a', {"title": "Category:Disambiguation pages"})

def is_search_result_page(soup):
    content = soup.find('div', {'id': 'bodyContent'})
    divs = content.find_all('div')
    for div in divs:
        if div.has_attr('class'):
            return div.get('class') == 'searchresults'
    return False

# Call this if the page is a disambiguation page.
def find_correct_page(soup, tags):
    bodyContent = soup.find('div', {'id': 'bodyContent'})
    list_items = bodyContent.find_all('li')
    pages = dict()
    for li in list_items:
        try:
            # Get the paragraph text
            url = base_url + li.find('a')['href']

            frequencies = dict()
            # Initialise tag keys
            for tag in tags:
                frequencies[tag] = 0

            pages[url] = get_tag_frequency(url, tags)
        except:
            continue

    statistics = determine_relevance(pages, tags)
    url = find_best_match(statistics)[0]
    frequency = get_tag_frequency(url, tags)
    return [url, frequency]

def find_best_match(statistics):
    # Find best match
    best = ['', 0, 0]
    for url, stats in statistics.iteritems():
        if stats[0] > best[1]:
            best[1] = stats[0]
            best[2] = stats[1]
        elif (stats[0] == best[1]) and (stats[1]) > best[2]:
            best[0] = url
            best[1] = stats[0]
            best[2] = stats[1]
    return best

# Dictionary where key is URL and value is dictionary.
def determine_relevance(urls, tags):
    statistics = dict()
    # Define tag frequency and percentage of tags met
    for url, frequencies in urls.iteritems():
        total_frequency = 0
        tags_met = 0

        for tag, frequency in frequencies.iteritems():
            if frequency > 0:
                tags_met += 1
            total_frequency += frequency

        percentage = float(tags_met) / len(tags)
        average_frequency = total_frequency / len(tags)

        statistics[url] = [percentage, average_frequency]
    return statistics

def get_tag_frequency(url, tags):
    soup = BeautifulSoup(urllib.urlopen(url).read()) 
    content_div = soup.find('div', {'id': 'mw-content-text'})
    paragraphs = content_div.find_all('p')
    all_text = ''
    frequencies = dict()
    for paragraph in paragraphs:
        p = innerHTML(paragraph)
        for word in p:
            word.lower()
        all_text += p
    for tag in tags:
        frequencies[tag] = all_text.count(tag)
    return frequencies

def innerHTML(element):
    return element.decode_contents(formatter="html")

def find_correct_result(search_term):
    results = get_search_results(search_term)
    for i in range(3):
        result = results[i]
         
def find_relevant_page(soup):
    section = soup.find('div', {"class": "searchresults"}).parent
    ul = section.find_next('ul', {'class' :'mw-search-results'}).find_all('li')
    for li in ul:
        div =  li.find('div', {'class': 'mw-search-result-heading'})
        print base_url + div.find('a')['href']

def try_force_disambiguation(search_term, tags):
    search_terms = search_term.split()
    search_terms.append('disambiguation')
    for link in get_search_results(search_terms):
        link = link.lower()
        if search_term in link and 'disambiguation' in link:
            return link
        search_terms = search_term.split()
        for term in search_term:
            if term in link and 'disambiguation' in link:
                return link
    return False

def get_total_tag_frequency(frequencies):
    total = 0
    for tag, frequency in frequencies.iteritems():
        total += frequency
    return total

def find_page(search_term, tags):
    url = base_url + "/w/index.php?search=" + search_term

    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    page = None

    is_disambiguated = False
    tag_frequency = 0

    if is_disambiguation_page(soup):
        page = find_correct_page(soup, tags)
    elif is_search_result_page(soup):
        print "%s is likely a search result page." % url
        page = [find_correct_result(search_term), 0]
    else:
        frequencies = get_tag_frequency(requests.get(url).url,tags)
        page = [requests.get(url).url, frequencies]

    return page

# search_terms is an array of search terms
def get_search_results(search_terms):
    url = base_url + "/w/index.php?search=" + '+'.join(search_terms)
    soup = BeautifulSoup(urllib.urlopen(url).read()) 

    results = []

    section = soup.find('div', {"class": "searchresults"}).parent
    ul = section.find_next('ul', {'class' :'mw-search-results'}).find_all('li')
    for li in ul:
        div =  li.find('div', {'class': 'mw-search-result-heading'})
        results.append(base_url + div.find('a')['href'])
    return results
    
# Scrape Wikipedia to find one main article and 3 related external articiles.
def scrape(subject, tags):
    articles = dict()
    subject_page = find_page(subject, tags)
    articles[subject_page[0]] = subject_page[1]
    for tag in tags:
        try:
            tag_page = find_page(tag, tags)
            articles[tag_page[0]] = tag_page[1]
        except:
            continue
    return articles 

def main(subject, tags, link_limit):
    to_append = subject.split(' ')
    for ta in to_append:
        tags.append(ta)
    articles = scrape(subject, tags)

    top_articles = []

    # Ensure link_limit is equal to or less than number of articles
    while link_limit > len(articles):
        link_limit -= 1
    
    # Return the most relevant wikipedia articles
    while len(top_articles) < link_limit:
        statistics = determine_relevance(articles, tags)
        best_url = find_best_match(statistics)[0]
        for url in articles.keys():
            if url == best_url:
                del articles[url]
        top_articles.append(best_url)

    for article in top_articles:
        print article

if __name__ == "__main__":
    limit = int(sys.argv[1])
    subject = str(sys.argv[2])
    tags = list(sys.argv[3::])
main(subject, tags, limit)
