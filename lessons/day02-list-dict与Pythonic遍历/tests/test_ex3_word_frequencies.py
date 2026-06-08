from exercises.ex3_word_frequencies import word_frequencies


def test_counts_words_case_insensitive():
    assert word_frequencies("Hi hi Python") == {"hi": 2, "python": 1}


def test_treats_punctuation_as_separator():
    assert word_frequencies("red, blue; red!") == {"red": 2, "blue": 1}


def test_keeps_digits_inside_tokens():
    assert word_frequencies("py3 py3 python") == {"py3": 2, "python": 1}


def test_empty_text():
    assert word_frequencies("  , ! ") == {}
