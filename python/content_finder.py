from bs4 import BeautifulSoup
from htmldom import htmldom
import requests
import urllib
import math
base_url = 'http://en.wikipedia.org'
subject = ''

def is_disambiguation_page(soup):
    return soup.find('a', {"title": "Category:Disambiguation pages"})

def innerHTML(element):
    return element.decode_contents(formatter="html")

# Call this if the page is a disambiguation page.
def find_correct_page(soup, tags):
    bodyContent = soup.find('div', {'id': 'bodyContent'})
    list_items = bodyContent.find_all('li')
    vectors = dict()
    for li in list_items:
        try:
            url = base_url + li.find('a')['href']
            sub_soup = BeautifulSoup(urllib.urlopen(url).read()) 
            content_div = sub_soup.find('div', {'id': 'mw-content-text'})
            paragraphs = content_div.find_all('p')

            vector = dict()
            for tag in tags:
                vector[tag] = 0

            for paragraph in paragraphs:
                p = innerHTML(paragraph)
                for word in p:
                    word = word.lower()
                for tag in tags:
                    vector[tag] += p.count(tag)

            vectors[url] = vector
        except:
            continue
    best_match = ['', 0]
    # Find the best match
    for url, vector in vectors.iteritems():
        total = 0
        for tag, frequency in vector.iteritems():
            total += frequency
        if total > best_match[1]:
            best_match[0] = url
            best_match[1] = total
    return best_match[0]

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

# Scrape Wikipedia to find one main article and 3 related external articiles.
def scrape(subject, tags):
    url = base_url + "/w/index.php?search=" + subject
    response = requests.get(url)

    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)

    if is_disambiguation_page(soup):
        find_correct_page(soup, tags)
    if is_search_result_page(soup):
        find_correct_result(soup)

def main():
    subject = 'python'
    tags = ['recursion', 'fibonacci', 'base case', 'recursive call', 'stack', 'computer science']
    articles = scrape(subject, tags)

main()
