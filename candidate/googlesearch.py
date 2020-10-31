'''Parses the google page results'''
from bs4 import BeautifulSoup
from requests import get


def search(term):
    '''Searches and parses the resulting html'''
    usr_agent = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}

    def fetch_results(search_term):
        escaped_search_term = search_term.replace(' ', '+')

        ddg_url = 'https://duckduckgo.com/html/?q={}&s=1&o=json'.format(escaped_search_term)
        response = get(ddg_url, headers=usr_agent)
        response.raise_for_status()

        return response.text

    def parse_results(raw_html):
        soup = BeautifulSoup(raw_html, 'html.parser')
        suggestion = soup.find('div', attrs={'id': 'did_you_mean'})
        correction = ''
        if suggestion is not None:
            correction = suggestion.find('a', href=True).text
            # print('correction: ' + str(correction.text) + '\n')
        result_block = soup.find_all('div', attrs={'class': 'result'})
        results = []
        for result in result_block:
            link = result.find('a', href=True, attrs={'rel': 'nofollow'})
            # print('link: ' + str(link['href']) + '\n')
            # print('title: ' + str(link.text) + '\n')
            description = result.find('a', href=True, attrs={'class': 'result__snippet'})
            # print('description: ' + str(description.text) + '\n')
            results.append((link['href'], link.text, description.text))
        return correction, results

    html = fetch_results(term)
    return parse_results(html)
