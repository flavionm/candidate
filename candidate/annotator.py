'''Annotates the text excerpt using the WAT API'''
import requests

MY_GCUBE_TOKEN = '9a76e60f-84bd-4a05-a2ac-048bf6f3a731-843339462'


def _wat_annotation(annotation):
    return {'spot': annotation['spot'], 'wiki_title': annotation['title']}


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
    return [_wat_annotation(a) for a in response.json()['annotations']]
