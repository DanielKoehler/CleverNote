from bs4 import BeautifulSoup
from htmldom import htmldom
import requests
import urllib
import math
base_url = 'http://en.wikipedia.org'
subject = ''

def is_disambiguation_page(soup):
    return soup.find('a', {"title": "Category:Disambiguation pages"})

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

    best_match = ['', 0]
    # Find the best match
    for url, frequencies in pages.iteritems():
        total_frequency = 0
        for tag, frequency in frequencies.iteritems():
            total_frequency += frequency
        if total_frequency > best_match[1]:
            best_match[0] = url
            best_match[1] = total_frequency

    return best_match[0]

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

def get_tag_frequency(paragraphs, tag):
    return frequency

def find_correct_result(soup):
    print "Finding correct result"

def is_search_result_page(soup):
    return False

def find_relevant_page(soup):
    section = soup.find('div', {"class": "searchresults"}).parent
    ul = section.find_next('ul', {'class' :'mw-search-results'}).find_all('li')
    for li in ul:
        div =  li.find('div', {'class': 'mw-search-result-heading'})
        print base_url + div.find('a')['href']


def try_force_disambiguation(search_term, tags):
    print "Showing search results for disambiguration effort."
    search_terms = search_term.split()
    search_terms.append('disambiguation')
    
    for link in get_search_results(search_terms):
        link = link.lower()
        if search_term in link and 'disambiguation' in link:
            print "%s can definitely be disambiguated." % search_term
            return link
        search_terms = search_term.split()
        for term in search_term:
            if term in link and 'disambiguation' in link:
                print "%s can likely be disambiguated." % search_term
                return link
    return False
    #url = base_url + "/w/index.php?search=" + search_term + "+Disambiguation"
    #html = urllib.urlopen(url).read()
    #soup = BeautifulSoup(html)
    #results = get_search_results(soup)
    #if is_disambiguation_page(soup):
        #return True
    #else:


def find_page(search_term, tags):
    url = base_url + "/w/index.php?search=" + search_term

    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    page = None

    is_disambiguated = False

    #if not is_disambiguation_page(soup):
        #if try_force_disambiguation(search_term, tags):
            #is_disambiguated = True
    #else:
        #is_disambiguated = True

    if is_disambiguation_page(soup):
        page = find_correct_page(soup, tags)
    elif not is_search_result_page(soup): 
        # Assume a wiki article 
        # Compare tag frequency with possible disambiguated article.
        link = try_force_disambiguation(search_term, tags)
        if link:



    elif is_search_result_page(soup):
        page = find_correct_result(soup)
    else:
        page = requests.get(url).url

    print page
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
    articles = []
    articles.append(find_page(subject, tags))
    for tag in tags:
        articles.append(find_page(tag, tags))
    return articles 

def main():
    subject = 'python'
    tags = ['recursion', 'list', 'dictionary', 'programming'] 
    articles = scrape(subject, tags)

main()
