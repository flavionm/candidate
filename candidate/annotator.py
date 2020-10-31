'''Annotates the text excerpt using the WAT API'''
import json

import requests

MY_GCUBE_TOKEN = '12663f54-03ff-42fb-98e4-59864815eca6-843339462'


class WATAnnotation:
    '''An entity annotated by WAT'''

    def __init__(self, d):
        self.start = d['start']
        self.end = d['end']
        self.spot = d['spot']

        self.wiki_title = d['title']
        self.wiki_link = f'https://en.wikipedia.org/wiki/{self.wiki_title}'

    def json_dict(self):
        '''Simple dictionary representation'''
        return {'wiki_title': self.wiki_title,
                'spot': self.spot,
                'start': self.start,
                'end': self.end,
                'link': self.wiki_link,
                'entity': f'{self.spot} -> {self.wiki_link}'
                }

    def print_wat_annotation(self):
        '''Prints the annotation'''
        print(json.dumps(self.json_dict(), indent=4))


def wat_entity_linking(text):
    '''Main method, text annotation with WAT entity linking system'''
    wat_url = 'https://wat.d4science.org/wat/tag/tag'
    payload = [("gcube-token", MY_GCUBE_TOKEN),
               ("text", text),
               ("lang", 'en'),
               ("tokenizer", "nlp4j"),
               ('debug', 9),
               ("method",
                "spotter:includeUserHint=true:includeNamedEntity=true:includeNounPhrase=true,"
                "prior:k=50,filter-valid,centroid:rescore=true,topk:k=5,voting:relatedness=lm,"
                "ranker:model=0046.model,confidence:model=pruner-wiki.linear")]

    response = requests.get(wat_url, params=payload)
    return [WATAnnotation(a) for a in response.json()['annotations']]


if __name__ == "__main__":
    wat_annotations = wat_entity_linking(
        'The Obama administration set records for the fewest air-polluted days.'
    )
    for a in wat_annotations:
        a.print_wat_annotation()
