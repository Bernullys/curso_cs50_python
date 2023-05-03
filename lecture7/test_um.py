import pytest
from um import count

def main():

    test_uppers()
    test_punctuation_marks()
    test_words_with_um()

def test_uppers():
    assert count("UM Um uM") == 3

def test_punctuation_marks():
    assert count("um. um, um? um{ um]") == 5

def test_words_with_um():
    assert count("jummy jumbo humbrella sum") == 0


if __name__=="__main__":
    main()