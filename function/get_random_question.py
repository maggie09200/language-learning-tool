import random
import gradio as gr
from data import vocab
from data import reversed_vocab
import data 
import json

#從單字表隨機出題


#日翻中
def get_question_jp_zh():
    if data.question_count < 10:
        data.question_count += 1
        return random.choice(list(vocab.keys())), gr.update(visible=True), gr.update(visible=False),gr.update(value = data.wrong_question),gr.update(value = data.wrong_count)
    elif data.question_count >= 10 :
        wq = json.dumps(data.wrong_question, indent=2, ensure_ascii=False).replace("{","").replace("}","").replace('"','').replace(":","→")
        return random.choice(list(vocab.keys())), gr.update(visible=False),gr.update(visible=True),gr.update(value = wq),gr.update(value = data.wrong_count)


#中翻日
def get_question_zh_jp():
    if data.question_count < 10:
        data.question_count += 1
        return random.choice(list(reversed_vocab.keys())), gr.update(visible=True), gr.update(visible=False),gr.update(value = data.wrong_question),gr.update(value = data.wrong_count)
    elif data.question_count >= 10 :
        wq = json.dumps(data.wrong_question, indent=2, ensure_ascii=False).replace("{","").replace("}","").replace('"','').replace(":","→")
        return random.choice(list(reversed_vocab.keys())), gr.update(visible=False),gr.update(visible=True),gr.update(value = wq),gr.update(value = data.wrong_count)