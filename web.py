from flask import Flask, render_template, request
from datetime import datetime
app = Flask(__name__)

@app.route("/")
def index():
    homepage = "<h1>資管二A 411111868 賴品瑄的求職相關資訊</h1>"
    homepage += "<a href=/rwd>我的個人簡介</a><br>"
    homepage += "<a href=/code>職業測驗結果</a><br>"
    homepage += "<a href=/work>相關工作介紹</a><br>"
    homepage += "<a href=/own>求職履歷自傳</a><br>"
    return homepage

@app.route("/rwd")
def rwd():
    return render_template("rwd.html")

@app.route("/code")
def code():
    return render_template("code.html")

@app.route("/work")
def work():
    return render_template("work.html")

@app.route("/own")
def own():
    return render_template("own.html")
#if __name__ == "__main__":
   #app.run()
