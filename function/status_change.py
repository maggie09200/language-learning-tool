import gradio as gr
import os
from data import vocab
    
def file_uploaded(file):
    if file:
        filename = os.path.basename(file.name)
        return f"已選擇檔案：{filename}"
    else:
        return "尚未上傳檔案，請上傳檔案"
    
def clear_result():
    return gr.update(value="")