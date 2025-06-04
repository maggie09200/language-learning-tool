import gradio as gr
import function
from data import wrong_question 
from data import wrong_count
from data import question_count
import function.back_to_hp
import function.semantic_check
import function.get_first_q


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


        #結果頁面
        with gr.Column(visible=False) as result_page:
            gr.Markdown("# 練習結束-- 結果")

            wrong_q = gr.TextArea(value="",label = "答錯的題目")
            wrong_c = gr.Textbox(value="",label = "錯題數")

            one_more = gr.Button("再來一次")
            back_to_hp = gr.Button("回到首頁重新上傳單字表")
            


        #日翻中問答
        with gr.Column(visible=False) as quiz_jp_zh:
            gr.Markdown("# 單字練習")

            question_text_jp = gr.Textbox(value="", label = "日文單字", interactive=False)
            user_input = gr.Textbox(label="請輸入中文意思")
            result = gr.Label(label = "結果",value="按下提交確認是否正確")
            direction_jp = gr.Textbox(value="Jp2zh",visible=False)

            btn_submit = gr.Button("提交")   #按下按鈕後顯示結果並清空輸入格
            btn_submit.click(fn=function.semantic_check_jp_zh, inputs= [question_text_jp, user_input, direction_jp], outputs= [result])
            btn_submit.click(fn=function.status_change.clear_input, inputs=[],outputs=[user_input]) 

            btn_next = gr.Button("下一題")
            btn_next.click(function.get_question_jp_zh, inputs=[], outputs=[question_text_jp,quiz_jp_zh,result_page,wrong_q, wrong_c])
            btn_next.click(function.status_change.clear_result, inputs=[],outputs=[result])

        #中翻日問答
        with gr.Column(visible=False) as quiz_zh_jp:
            gr.Markdown("# 單字練習")

            question_text_zh = gr.Textbox(value="", label = "中文意思", interactive=False)
            user_input = gr.Textbox(label="請輸入日文單字")
            result = gr.Label(label = "結果",value="按下提交確認是否正確")
            direction_zh = gr.Textbox(value="zh2jp",visible=False)

            btn_submit = gr.Button("提交")   #按下按鈕後顯示結果並清空輸入格
            btn_submit.click(fn=function.semantic_check_zh_jp, inputs= [question_text_zh, user_input,direction_zh], outputs= [result])
            btn_submit.click(fn=function.status_change.clear_input, inputs=[],outputs=[user_input]) 

            btn_next = gr.Button("下一題")
            btn_next.click(function.get_question_zh_jp,inputs=[], outputs=[question_text_zh,quiz_zh_jp,result_page,wrong_q,wrong_c])
            btn_next.click(function.status_change.clear_result, inputs=[],outputs=[result])
        
        btn_start_quiz = gr.Button("開始練習",visible=True)

        with gr.Column(visible=False) as quiz_select:
            gr.Markdown("# 選擇練習模式")

            btn_jp_zh = gr.Button("日翻中")
            btn_jp_zh.click(function.show_jp_zh_quiz, inputs=[],
            outputs=[question_text_jp,quiz_jp_zh,upload_section,btn_start_quiz,quiz_select])

            btn_zh_jp = gr.Button("中翻日")
            btn_zh_jp.click(function.show_zh_jp_quiz, inputs=[],
            outputs=[question_text_zh,quiz_zh_jp,upload_section,btn_start_quiz,quiz_select])

        #顯示練習模式按鈕
        btn_start_quiz.click(
            fn=function.show_quiz_select, inputs=[],
            outputs=[quiz_select,upload_section,btn_start_quiz]
            )
        
        #再來一次和回到首頁
        one_more.click(function.one_more,outputs=[quiz_select,btn_start_quiz,result_page])
        back_to_hp.click(function.back_to_hp, outputs=[upload_section,result_page,btn_start_quiz])

    demo.launch()
    

if __name__ == "__main__":
    main()
