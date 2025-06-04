# 語意比對式語言學習工具 Language Learning Tool with Semantic Matching

本專案是一款以 **SQLite 資料庫** 儲存歷史練習紀錄，結合 **AI 語意比對** 技術的雙向語言學習工具。主要用於背單字練習，支援日文與中文的相互翻譯與語意比對。
 
--- 
 
## 主要功能 
 
- ✅ 支援上傳自訂的單字表 CSV 檔（格式：日文, 中文）
- ✅ 利用 AI 模型進行語意比對，判斷使用者輸入的答案是否正確（包含同義詞、語意相似）
- ✅ 每次練習以 10 題為單位，結束後顯示錯題與錯誤題數 
- ✅ 支援雙向語言練習（中翻日、日翻中）
- ✅ 使用 SQLite 建立本地資料庫，減少 API 呼叫次數，提高效率與反應速度 
 
--- 
 
## 專案架構 
 
- `app.py` - Gradio 網頁介面主程式 
- `function.py` - 主要邏輯及 AI 語意比對函式 
- `database.py` - 使用 SQLAlchemy ORM 與 SQLite 操作資料庫 
- `check_db.py` - 確認資料庫裡的資料 
- `demo.csv` - 範例單字表 CSV 檔案 
 
--- 
 
## 安裝說明 

- `Python                       3.12.3`
- `google-generativeai          0.8.5`
- `gradio                       5.32.0`
- `SQLAlchemy                   2.0.41`
 
- `pip install <module name>`

--- 

## 使用說明  
  
啟動應用程式：  
-cd到所在資料夾  執行`python app.py`  
-打開瀏覽器，訪問 Gradio 介面（預設網址會在終端顯示）。   
  
-上傳你的單字表 CSV 檔。  
-選擇練習模式（日翻中 / 中翻日），開始答題。  
-答題過程中，系統會根據 AI 語意比對給出判斷，並將答題紀錄存入資料庫。  
-每 10 題結束會顯示錯題與錯誤次數，並可回首頁重置。  
   
 --- 
