'''Searchs for the candidates to be selected by the SMAPH algorithm'''
import websearch


def main(initial_query):
    '''Starting function'''
    create_set_1(initial_query)


def create_set_1(query):
    '''Creates set containing Wikipedia links from query result'''
    correction, results = websearch.search(query)
    print(correction)
    print()
    for result in results[0:5]:
        print('link: ' + result[0])
        print('title: ' + result[1])
        print('description: ' + result[2])
        print()



if __name__ == '__main__':
    main('carlos aberto de noberga')
