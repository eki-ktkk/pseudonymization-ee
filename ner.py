from estnltk.taggers import NerTagger

nertagger = NerTagger()

from estnltk import Text


def get_ner_dict(raw_text):
    text = Text(raw_text)
    text = text.tag_layer(['sentences', 'morph_analysis'])

    nertagger.tag(text)

    ner_dict = {}

    for span in text.ner.spans:
        ner_dict[(span.start, span.end)] = span.annotations[0].nertag

    return ner_dict