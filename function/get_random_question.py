import random
from data import vocab

#從單字表隨機出題
def get_question_jp_zh():
    return random.choice(list(vocab.keys()))

def get_question_zh_jp():
    return random.choice(list(vocab.values()))