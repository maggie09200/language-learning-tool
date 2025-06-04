import random
from data import vocab
from data import reversed_vocab
from data import question_count

#從單字表隨機出題


#日翻中
def get_first_q_jp_zh():
    global question_count
    question_count += 1
    return random.choice(list(vocab.keys()))



#中翻日
def get_first_q_zh_jp():
    global question_count
    question_count += 1
    return random.choice(list(reversed_vocab.keys()))