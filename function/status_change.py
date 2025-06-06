import gradio as gr
import os
    
def file_uploaded(file):
    if file:
        filename = os.path.basename(file.name)
        return f"已選擇檔案：{filename}"
    else:
        return "尚未上傳檔案，請上傳檔案"
    
def clear_input():
    return gr.update(value="")

def clear_result():
    return gr.update(value="按下提交確認是否正確")
