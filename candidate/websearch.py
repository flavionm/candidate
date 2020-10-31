'''Parses the DuckDuckGo results page'''
import requests
from bs4 import BeautifulSoup


def search(term):
    '''Searches and parses the resulting html'''
    html = fetch_results(term)
    return parse_results(html)


def fetch_results(search_term):
    '''Gets the response from the search engine'''
    usr_agent = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                 '(KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
    ddg_url = 'https://html.duckduckgo.com/html/?q={}&kl=us-en'.format(
        search_term)

    response = requests.get(ddg_url, headers=usr_agent)
    response.raise_for_status()

    return response.text


def parse_results(raw_html):
    '''Parses the HTML for relevant resources'''
    soup = BeautifulSoup(raw_html, 'html.parser')
    suggestion = soup.find('div', attrs={'id': 'did_you_mean'})
    correction = ''
    if suggestion is not None:
        correction = suggestion.find('a', href=True).text
    result_block = soup.find_all('div', attrs={'class': 'result'})
    results = []
    for result in result_block:
        link = result.find('a', href=True, attrs={'rel': 'nofollow'})
        description = result.find('a', href=True, attrs={
                                  'class': 'result__snippet'})
        results.append((link['href'], link.text, description.text))
    return correction, results
