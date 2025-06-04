import gradio as gr
import data

def back_to_hp():
    data.question_count = 0
    data.wrong_question = {}
    return gr.update(visible=True),gr.update(visible=False),gr.update(visible=True)