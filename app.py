import gradio as gr
import function

def main():
    with gr.Blocks()as demo:
        with gr.Column(visible=True) as upload_section:
            gr.Markdown("# 上傳CSV檔案開始練習")

            #上傳CSV檔案
            csv_input =gr.File(label="上傳單字CSV檔(格式：日文,中文)")
            status = gr.Label(label="狀態",value="尚未上傳檔案，請上傳檔案")

            btn_upload = gr.Button("上傳單字表")
            btn_upload.click(fn=function.set_vocab_from_csv, inputs=[csv_input], outputs=[status])

        #上傳檔案(未按下上傳時)顯示選擇的檔案名稱
        csv_input.change(function.status_change.file_uploaded,inputs=[csv_input],outputs=[status])

        #日翻中問答
        with gr.Column(visible=False) as quiz_jp_zh:
            gr.Markdown("# 單字練習")

            question_text = gr.Textbox(value="", label = "日文單字", interactive=False)
            user_input = gr.Textbox(label="請輸入中文意思")
            result = gr.Label(label = "結果",value="按下提交確認是否正確")

            btn_submit = gr.Button("提交")   #按下按鈕後顯示結果並清空輸入格
            btn_submit.click(fn=function.semantic_check, inputs= [question_text, user_input], outputs= [result])
            btn_submit.click(fn=function.status_change.clear_input, inputs=[],outputs=[user_input]) 

            btn_next = gr.Button("下一題")
            btn_next.click(function.get_question_jp_zh, outputs=question_text)
            btn_next.click(function.status_change.clear_result, inputs=[],outputs=[result])

        #中翻日問答
        with gr.Column(visible=False) as quiz_jp_zh:
            gr.Markdown("# 單字練習")

            question_text = gr.Textbox(value="", label = "中文意思", interactive=False)
            user_input = gr.Textbox(label="請輸入日文單字")
            result = gr.Label(label = "結果",value="按下提交確認是否正確")

            btn_submit = gr.Button("提交")   #按下按鈕後顯示結果並清空輸入格
            btn_submit.click(fn=function.semantic_check, inputs= [question_text, user_input], outputs= [result])
            btn_submit.click(fn=function.status_change.clear_input, inputs=[],outputs=[user_input]) 

            btn_next = gr.Button("下一題")
            btn_next.click(function.get_question_zh_jp, outputs=question_text)
            btn_next.click(function.status_change.clear_result, inputs=[],outputs=[result])
        
        btn_start_quiz = gr.Button("開始練習",visible=True)

        with gr.Column(visible=False) as quiz_select:
            gr.Markdown("# 選擇練習模式")
            btn_jp_zh = gr.Button("日翻中")
            btn_jp_zh.click(fn=function.show_jp_zh_quiz, inputs=[],
            outputs=[question_text,
            quiz_jp_zh,upload_section,btn_start_quiz,quiz_select])

            btn_zh_jp = gr.Button("中翻日")
            btn_zh_jp.click(fn=function.show_zh_jp_quiz, inputs=[],
            outputs=[question_text,
            quiz_jp_zh,upload_section,btn_start_quiz,quiz_select])

        #顯示練習模式按鈕
        btn_start_quiz.click(
            fn=function.show_quiz_select, inputs=[],
            outputs=[quiz_select,upload_section,btn_start_quiz]
            )

    demo.launch()
    

if __name__ == "__main__":
    main()
