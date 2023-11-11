from flask import Flask, render_template, request
from datetime import datetime
app = Flask(__name__)

@app.route("/")
def index():
    homepage = "<h1>資管二A 411111868 賴品瑄的求職相關資訊</h1>"
    homepage += "<a href=/mis>我的個人簡介</a><br>"
    homepage += "<a href=/today>MIS相關工作介紹</a><br>"
    homepage += "<a href=/welcome>職業測驗結果</a><br>"
    homepage += "<a href=/about>求職履歷自傳</a><br>"
    return homepage


if __name__ == "__main__":
    app.run()
