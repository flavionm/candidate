'''Tests both annotation methods'''
import annotator
import candidate


def _examples():
    _test('Armstrong mon lading')
    _test('Barak Obama iram bombing', 15)
    _test('Socialism vs communism', 5)
    _test('WAT api token')


def _test(query, tries=0):
    _test_custom(query, tries)
    print()
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
        print(f'{note["spot"]}: https://en.wikipedia.org/wiki/{note["wiki_title"]}')


if __name__ == "__main__":
    _examples()
