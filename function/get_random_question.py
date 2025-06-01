import random
from data import vocab

#從單字表隨機出題
def get_random_question():
    return random.choice(list(vocab.keys()))