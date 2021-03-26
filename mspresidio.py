import spacy

from ner import get_ner_dict

spacy_model_fi = 'spacy_fi_experimental_web_md'
spacy_multi = 'xx_ent_wiki_sm'
spacy_multi_trf = 'xx_sent_ud_sm'
text = "Mi nimi on Eduardo. Olen 26-aastane ja pärit Tartust. Olen sündinud 25. jaanuaril 1995. Minu e-posti aadress on eduardo@eki.ee ja krediitkaart on see 4111 1111 1111 1111."

from presidio_analyzer import AnalyzerEngine, RecognizerRegistry
from presidio_analyzer.nlp_engine import NlpEngineProvider

# Create configuration containing engine name and models
configuration = {
    "nlp_engine_name": "spacy",
    "models": [{"lang_code": "ee", "model_name": spacy_multi},],
}




def anonymize(text):
    # Create NLP engine based on configuration
    provider = NlpEngineProvider(nlp_configuration=configuration)
    nlp_engine_with_estonian = provider.create_engine()

    # Pass the created NLP engine and supported_languages to the AnalyzerEngine
    analyzer = AnalyzerEngine(
        nlp_engine=nlp_engine_with_estonian,
        supported_languages=["ee"]
    )

    # Analyze in different languages
    analyzer_results_ee = analyzer.analyze(text=text, language="ee")
    print(analyzer_results_ee)
    
    ner_dict = get_ner_dict(text)

    #remove false person tags
    analyzer_results_ee = [r for r in analyzer_results_ee if r.entity_type != 'PERSON' or (r.start,r.end) in ner_dict.keys() and ner_dict[(r.start,r.end)] == 'PER']

    from presidio_anonymizer import AnonymizerEngine
    from presidio_anonymizer.entities import RecognizerResult, AnonymizerConfig

    # Initialize the engine with logger.
    engine = AnonymizerEngine()

    # Class the anonymize function with the text, analyzer results and
    # Anonymizers config to define the anonymization type.
    result = engine.anonymize(
        text=text,
        analyzer_results=analyzer_results_ee,
        # anonymizers_config={"PERSON": AnonymizerConfig("replace", {"new_value": "BIP"})}
    )

    return result

