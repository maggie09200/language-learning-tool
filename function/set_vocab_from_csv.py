import csv
from data import vocab
from data import reversed_vocab

#處理用戶上傳的CSV檔案
def set_vocab_from_csv(file):
    try:
        with open(file,'r',encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) == 2:
                    jp, zh = row[0].strip(), row[1].strip()
                    vocab[jp] = zh
                    reversed_vocab[zh] = jp
        if vocab:
            return "單字表上傳成功! 點選開始練習。"
        else:
            return "CSV檔內容錯誤，請確認每行格式為「日文，中文」"
    except Exception as e:
        return f"讀取CSV發生錯誤: {e}"