import google.generativeai as genai
from data import vocab

#設定Gemini API
genai.configure(api_key="AIzaSyD664dnxA_GoG-ehVt9MhNxUbM2KvIhpGQ")
model = genai.GenerativeModel('gemini-2.0-flash')

def semantic_check_zh(question, user_input):
    correct_answer = vocab.get(question, None)
    if not correct_answer:
        return "題目錯誤"
    
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
        return f"答錯了，正確答案是:{correct_answer}"
    
def semantic_check_jp(question, user_input):
    correct_answer = vocab.get(question, None)
    if not correct_answer:
        return "題目錯誤"
    
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
        return f"答錯了，正確答案是:{correct_answer}"