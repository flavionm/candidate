'''Tests both annotation methods'''
import annotator
import candidate


def _examples():
    _test('Armstrong mon lading')
    _test('Barak Obama mandate lenght', 15)
    _test('best cheap cat food', 5)
    _test('WAT api token')
    _test('seven wonders of the world')


def _test(query, tries=0):
    print(f'Query: {query}')
    print()
    print('SMAPH-like')
    _test_custom(query, tries)
    print()
    print('WAT')
    _test_wat(query)
    print()
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
            f'{note["spot"]}: https://en.wikipedia.org/wiki/{note["wiki_title"]}')


if __name__ == "__main__":
    _examples()
