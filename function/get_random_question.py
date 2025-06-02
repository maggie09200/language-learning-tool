import random
from data import vocab
from data import reversed_vocab

#從單字表隨機出題

#日翻中
def get_question_jp_zh():
    return random.choice(list(vocab.keys()))


#中翻日
def get_question_zh_jp():
    return random.choice(list(reversed_vocab.keys()))