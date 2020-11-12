'''Tests both annotation methods'''
import annotator
import candidate


def _examples():
    _test('Armstrong mon lading',
          'Armstrong -> Neil_Armstrong, mon lading -> Moon_landing,')
    _test('Barak Obama mandate lenght', 'Barak Obama -> Barack_Obama,', 15)
    _test('best cheap cat food', 'cat food -> Cat_food,', 5)
    _test('WAT api token',
          'api -> Application_programming_interface, token -> Access_token,')
    _test('seven wonders of the world',
          'seven wonders of the world -> Seven_Wonders_of_the_Ancient_World,')


def _test(query, truth, tries=0):
    print(f'Query: {query}')
    print()
    print('Truth:', truth)
    print('SMAPH-like: ', end='')
    _test_custom(query, tries)
    print('WAT: ', end='')
    _test_wat(query)
    print()


def _test_custom(query, tries):
    if tries > 0:
        result = candidate.annotate_query(query, tries)
    else:
        result = candidate.annotate_query(query)
    candidate.print_annotations(result)


def _test_wat(query):
    wat_annotations = annotator.wat_entity_linking(query)
    for note in wat_annotations:
        print(
            f'{note["spot"]} -> {note["wiki_title"]}', end=',')
    print()


if __name__ == "__main__":
    _examples()
