from .get_random_question import get_question_jp_zh
from .get_random_question import get_question_zh_jp
import gradio as gr
from data import vocab

def show_jp_zh_quiz():
    if vocab:
        return get_question_jp_zh(), gr.update(visible=True), gr.update(visible=False), gr.update(visible=False),gr.update(visible=False)
    else:
        return "", gr.update(visible=False)
    
def show_zh_jp_quiz():
    if vocab:
        return get_question_zh_jp(), gr.update(visible=True), gr.update(visible=False), gr.update(visible=False),gr.update(visible=False)
    else:
        return "", gr.update(visible=False)