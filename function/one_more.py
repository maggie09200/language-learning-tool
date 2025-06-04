import gradio as gr
import data

def one_more():
    data.question_count = 0
    data.wrong_count = 0
    data.wrong_question = {}
    return gr.update(visible=True),gr.update(visible=False),gr.update(visible=False)