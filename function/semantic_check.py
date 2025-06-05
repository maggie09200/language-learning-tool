import google.generativeai as genai
from data import vocab
from data import reversed_vocab
from models import get_answer_from_db, save_answer_to_db
import data 

#設定Gemini API
genai.configure(api_key="API KEY")
model = genai.GenerativeModel('gemini-2.0-flash')

#日翻中比對
def semantic_check_jp_zh(question, user_input, direction):
    correct_answer = get_answer_from_db(question, direction)
    if not correct_answer:
        correct_answer = vocab.get(question, None)
        save_answer_to_db(question,correct_answer,direction)
        if not correct_answer:
            return "題目錯誤"

    if user_input in correct_answer:
        return "正確!"
    
    else:
        prompt = f"""
            你是語言比對專家。
            請判斷下面兩句話的意思是否相近（包含同義詞、語意相似）。
            如果相近，請回覆 "True"。
            如果不相近，請回覆 "False"。
            正確答案：「{correct_answer}」
            使用者輸入：「{user_input}」
        """
        response = model.generate_content(prompt)
        reply = response.text.strip()
        
        if "True" in reply:
            return f"正確!"
        else:
            data.wrong_question[question] = correct_answer
            data.wrong_count += 1
            return f"答錯了，正確答案是:{correct_answer}"
    

#中翻日比對
def semantic_check_zh_jp(question, user_input, direction):
    correct_answer = get_answer_from_db(question, direction)
    if not correct_answer:
        correct_answer = reversed_vocab.get(question, None)
        save_answer_to_db(question,correct_answer,direction)
        if not correct_answer:
            return "題目錯誤"

    if user_input in correct_answer:
        return "正確!"
    
    else:
        prompt = f"""
            你是語言比對專家。
            請判斷下面兩句話的意思是否相近（包含同義詞、語意相似）。
            如果相近，請回覆 "True"。
            如果不相近，請回覆 "False"。
            正確答案：「{correct_answer}」
            使用者輸入：「{user_input}」
        """
        response = model.generate_content(prompt)
        reply = response.text.strip()
        
        if "True" in reply:
            return f"正確!"
        else:
            data.wrong_question[question] = correct_answer
            data.wrong_count += 1
            return f"答錯了，正確答案是:{correct_answer}"
