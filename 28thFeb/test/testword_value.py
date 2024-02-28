from word_values import load_words,calc_word_value,max_word_value

words = load_words()

def test_load_word():
    assert type(words)==list 
    assert words[10] == 'Aaronic'
    assert words[100] == 'abbas'


def test_word_value():
    assert calc_word_value('BOB')==7
    assert calc_word_value('JuliaN') == 13
    assert calc_word_value('PyBites') == 14
    assert calc_word_value('benzalphenylhydrazone') == 56

def test_max_word_value():
    assert max_word_value(['BOB','JuliaN']) =='JuliaN'