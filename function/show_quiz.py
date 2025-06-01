from .get_random_question import get_random_question
import gradio as gr
from data import vocab

def show_quiz():
    if vocab:
        return get_random_question(), gr.update(visible=True), gr.update(visible=False), gr.update(visible=False)
    else:
        return "", gr.update(visible=False)