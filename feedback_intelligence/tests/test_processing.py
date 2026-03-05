from src.processing.cleaner import clean_text
from src.processing.categorizer import categorize

def test_clean_text():
    assert clean_text("Hello!!!") == "hello"

def test_categorize_bug():
    assert categorize("app crash issue") == "Bug"