from flask import Flask, render_template,request
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    link = "<h1>歡迎進入陳宇謙的網站網頁</h1>"
    link += "<a href='/mis'>課程</a>"
    link += "<hr>"  # 分隔線
    link += "<a href='/today'>今天日期</a>"
    link += "<hr>"  # 分隔線
    link += "<a href='/about'>關於宇謙</a>"
    link += "<hr>"
    link +="<a href=/welcome?nick=宇謙>GET傳值</a>"
    link +="<hr>"
    link +="<a href=/account>POST傳值(帳號密碼)</a>"
    link +="<hr>"
    link +="<a href=/operation>數學運算</a>"
    link +="<hr>"
    return link


@app.route("/mis")
def course():
    return "<h1>資訊管理導論</h1>"

@app.route("/today")
def today():
    now = datetime.now()
    year = str(now.year)
    month = str(now.month)
    day = str(now.day)
    now = year + "/" + month + "/" +day
    return render_template("today.html", datetime = (now))

@app.route("/about")
def about():
    return  render_template("my.html")

@app.route("/welcome", methods=["GET"])
def welcome():
    user = request.values.get("nick")
    return render_template("welcome.html", name=user)

@app.route("/account", methods=["GET", "POST"])
def account():
    if request.method == "POST":
        user = request.form["user"]
        pwd = request.form["pwd"]
        result = "您輸入的帳號是：" + user + "; 密碼為：" + pwd 
        return result
    else:
        return render_template("account.html")

@app.route("/operation", methods=["GET", "POST"])
def operation():
    if request.method == "POST":
        x = float(request.form["x"])
        y = float(request.form["y"])
        opt = request.form["opt"]

        if opt == "+":
            result = x + y
        elif opt == "-":
            result = x - y
        elif opt == "*":
            result = x * y
        elif opt == "/":
            if y == 0:
                result = "不能除以0"
            else:
                result = x / y
        else:
            result = "運算子錯誤"

        return render_template("operation.html", result=result)
    else:
        return render_template("operation.html", result=None)




if __name__ == "__main__":
    app.run(debug=True)
