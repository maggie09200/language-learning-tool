from .get_first_q import get_first_q_jp_zh, get_first_q_zh_jp
import gradio as gr
from data import vocab
from data import reversed_vocab

def show_jp_zh_quiz():
    if vocab:
        return get_first_q_jp_zh() , gr.update(visible=True), gr.update(visible=False), gr.update(visible=False),gr.update(visible=False)
    else:
        return "", gr.update(visible=False), gr.update(visible=True), gr.update(visible=True),gr.update(visible=True)
    
def show_zh_jp_quiz():
    if reversed_vocab:
        return get_first_q_zh_jp(), gr.update(visible=True), gr.update(visible=False), gr.update(visible=False),gr.update(visible=False)
    else:
        return "", gr.update(visible=False), gr.update(visible=True), gr.update(visible=True),gr.update(visible=True)