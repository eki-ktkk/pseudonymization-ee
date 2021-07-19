import csv

import spacy
import re
from ner import get_ner_dict
from presidio_analyzer import AnalyzerEngine, RecognizerRegistry, RecognizerResult
from presidio_analyzer.nlp_engine import NlpEngineProvider

spacy_model_fi = 'spacy_fi_experimental_web_md'
spacy_multi = 'xx_ent_wiki_sm'
spacy_multi_trf = 'xx_sent_ud_sm'
spacy_en = 'en_core_web_sm'
text = "Mi nimi on Eduardo. Olen 26-aastane ja pärit Tartust. Olen sündinud 25. jaanuaril 1995. Minu e-posti aadress on eduardo@eki.ee ja krediitkaart on see 4111 1111 1111 1111."
estnltk2spacytags = {'PER':'PERSON', 'LOC':'LOCATION', 'ORG': 'ORGANIZATION'}


# Create configuration containing engine name and models
configuration = {
    "nlp_engine_name": "spacy",
    "models": [{"lang_code": "et", "model_name": spacy_multi}]
    #"models": [{"lang_code": "en", "model_name": spacy_en}]
}


def anonymize(text):
    # Create NLP engine based on configuration
    provider = NlpEngineProvider(nlp_configuration=configuration)
    nlp_engine_with_estonian = provider.create_engine()

    # Pass the created NLP engine and supported_languages to the AnalyzerEngine
    analyzer = AnalyzerEngine(
        nlp_engine=nlp_engine_with_estonian,
        supported_languages=["en", "et"],default_score_threshold=0.01
    )

    # Analyze in different languages
    analyzer_results_ee = analyzer.analyze(text=text, language="et")
    print(analyzer_results_ee)
    
    ner_dict = get_ner_dict(text)

    #remove false person tags
    #analyzer_results_ee = [r for r in analyzer_results_ee if r.entity_type != 'PERSON' or (r.start,r.end) in ner_dict.keys() and ner_dict[(r.start,r.end)] == 'PER']

    #analyzer_results_ee = []

    #add org tags
    from presidio_analyzer import RecognizerResult
    for key, value in ner_dict.items():

        r = RecognizerResult(estnltk2spacytags[value],key[0], key[1], 0.85)
        analyzer_results_ee.append(r)

    from presidio_anonymizer import AnonymizerEngine
    from presidio_anonymizer.entities import RecognizerResult, AnonymizerConfig

    # Initialize the engine with logger.
    engine = AnonymizerEngine()

    # Class the anonymize function with the text, analyzer results and
    # Anonymizers config to define the anonymization type.
    result = engine.anonymize(
        text=text,
        analyzer_results=analyzer_results_ee,

        #anonymizers_config={"ORG": AnonymizerConfig("replace", {"new_value": "<ORG>"})}
    )

    return result

def hide_dates(text, tag):
    text = re.sub('[0-9]+\. (jaanuar|veebruar|märts|aprill|mai|juuni|juuli|august|september|oktoober|november|detsember|jaanuaris|veebruaris|märtsis|aprillis|mais|juunis|juulis|augustis|septembris|oktoobris|novembris|detsembris)( [0-9]+)*', tag,text)
    text = re.sub("([1-9]|0[1-9]|1[0-9]|2[0-9]|3[0-1])(\.|-|/)([1-9]|0[1-9]|1[0-2])(\.|-|/)([0-9]{4}|[0-9]{2})|([0-9][0-9]|19[0-9][0-9]|20[0-9][0-9])(\.|-|/)([1-9]|0[1-9]|1[0-2])(\.|-|/)([0-9]{4}|[0-9]{2})", tag, text)
    text = re.sub("[0-9]{4}", tag, text)
    return text



def hide_names(text, tag):
    given_names = load_given_names("given_names.csv")
    surnames = load_surnames("surnames.txt")

    for name in given_names:
        text = text.replace(name + " ", tag + " ")
    for name in surnames:
        text = text.replace(name + " ", tag + " ")

    return text



def load_given_names(file):
    l = []
    with open(file, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            l.append(row[0].capitalize())
    l = l[:-1]
    l = [s for s in l if len(s) > 3 and s.isalpha()]
    return l

def load_surnames(file):
    l = []
    n = 0
    with open(file, encoding='utf8') as f:
        for row in f:
            try:
                l.append(re.split('\s+', row)[2].capitalize())
            except:
                print(n)
            n+=1
    l = [s for s in l if len(s) > 3 and s.isalpha()]
    return l
