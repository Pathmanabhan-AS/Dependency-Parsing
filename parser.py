# parser.py
import stanza
import pandas as pd

# Ensure the English model is downloaded
stanza.download('en')

# Load Stanza pipeline
nlp = stanza.Pipeline(lang='en', processors='tokenize,pos,lemma,depparse')

# Dependency label mapping (short → full description)
dependency_labels = {
    "nsubj": "Nominal Subject",
    "amod": "Adjectival Modifier",
    "det": "Determiner",
    "root": "Root",
    "case": "Case Marking",
    "obl": "Oblique Modifier",
    "punct": "Punctuation",
    "obj": "Object",
    "iobj": "Indirect Object",
    "advmod": "Adverbial Modifier",
    "acl": "Clausal Modifier",
    "xcomp": "Open Clausal Complement",
    "ccomp": "Clausal Complement",
    "mark": "Marker",
    "cc": "Coordinating Conjunction",
    "conj": "Conjunct",
    "nmod": "Nominal Modifier",
    "compound": "Compound Word",
    "csubj": "Clausal Subject",
    "aux": "Auxiliary Verb",
    "cop": "Copula",
    "neg": "Negation",
    "nummod": "Numeric Modifier",
    "appos": "Appositional Modifier",
    "discourse": "Discourse Element",
    "vocative": "Vocative",
    "expl": "Expletive",
    "parataxis": "Parataxis",
    "dep": "Unspecified Dependency",
}

def parse_sentence(sentence):
    """Parses a sentence and returns dependency relations with full names."""
    doc = nlp(sentence)

    dependencies = []
    for sent in doc.sentences:
        for word in sent.words:
            full_relation = dependency_labels.get(word.deprel, word.deprel)  # Convert to full name if available
            dependencies.append({
                "Token": word.text,
                "Head": sent.words[word.head - 1].text if word.head > 0 else "ROOT",
                "Relation": full_relation
            })

    return pd.DataFrame(dependencies)

