'''Searchs for the candidates to be selected by the SMAPH algorithm'''
import annotator
import websearch


def main(initial_query):
    '''Starting function'''
    create_set_1(initial_query)


def create_set_1(query):
    '''Creates set containing Wikipedia links from query result'''
    correction, results = websearch.search(query)
    list_query = correction.split()
    print(list_query)
    print()
    for result in results[0:3]:
        print(result[2])
        annotations = annotator.wat_entity_linking(result[2])
        for annotation in annotations:
            annotation.print_wat_annotation()
        print()


if __name__ == '__main__':
    main('barak obama iram bombing')
