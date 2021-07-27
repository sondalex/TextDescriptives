import textdescriptives as td
import spacy
import pytest
import ftfy


@pytest.fixture(scope="function")
def nlp():
    nlp = spacy.load("en_core_web_sm")
    nlp.add_pipe("textdescriptives")
    return nlp


def test_extract_df_single_doc(nlp):
    doc = nlp("This is just a cute little text. Actually, it's two sentences.")
    td.extract_df(doc)
    for metric in ["descriptive_stats", "readability", "dependency_distance"]:
        td.extract_df(doc, metrics=metric)


def test_extract_df_pipe(nlp):
    text = [
        "I wonder how well the function works on multiple documents",
        "Very exciting to see, don't you think?",
    ]
    docs = nlp.pipe(text)
    td.extract_df(docs)

def test_extract_df_subsetters(nlp):
    doc = nlp("This is just a cute little text. Actually, it's two sentences.")
    df = td.extract_df(doc, include_text=False)
    df[td.readability_cols]
    df[td.dependency_cols]
    df[td.descriptive_stats_cols]
