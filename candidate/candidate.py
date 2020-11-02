'''Searchs for the candidates to be selected by the SMAPH algorithm'''
import sys

import annotator
import websearch


def annotate_query(query, tries=10):
    '''Annotates que given query string'''
    if query == '':
        raise RuntimeError("Query can't be empty")
    if tries < 5:
        raise RuntimeError("Tries can't be lower than 5")

    correction, results = websearch.search(query)
    entity_mappings = _annotate_excerpts(query, results, correction, tries)

    annotations = _select_annotations(entity_mappings, tries//5)
    return annotations


def _annotate_excerpts(query, results, correction, tries):
    entities = [entity.lower() for entity in correction.split()]
    query_entities = query.split()
    name_map = {entity: query_entities[i] for i, entity in enumerate(entities)}
    entity_mappings = {name_map[entity]: {} for entity in entities}
    for result in results[0:tries]:
        annotations = annotator.wat_entity_linking(result[2])
        for annotation in annotations:
            for entity in annotation['spot'].lower().split():
                if entity in entities:
                    mappings = entity_mappings[name_map[entity]]
                    mappings[annotation['wiki_title']] = mappings.get(
                        annotation['wiki_title'], 0) + 1
    return entity_mappings


def _select_annotations(entity_mappings, min_weight):
    annotations = []
    for entity in entity_mappings.keys():
        mappings = entity_mappings[entity]
        best_match = ''
        weight = min_weight - 1
        for title in mappings.keys():
            if mappings[title] > weight:
                best_match = title
                weight = mappings[title]
        if weight >= min_weight:
            annotations.append(
                (entity, f'https://en.wikipedia.org/wiki/{best_match}', weight))
        else:
            annotations.append((entity, '', 0))
    return annotations


def print_annotations(annotations):
    '''Prints the annotation list'''
    for annotation in annotations:
        if annotation[2] > 1:
            print(f'{annotation[0]}: {annotation[1]} ({annotation[2]})')
        else:
            print(f'{annotation[0]}: (0)')


if __name__ == '__main__':
    try:
        ARGS_NUM = len(sys.argv)
        if ARGS_NUM < 2:
            print('Missing query')
        elif ARGS_NUM == 2:
            print_annotations(annotate_query(sys.argv[1]))
        elif ARGS_NUM == 3:
            print_annotations(annotate_query(sys.argv[1], int(sys.argv[2])))
        else:
            print('Too many arguments')
    except RuntimeError as error:
        print(str(error))
