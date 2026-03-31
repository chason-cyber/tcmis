import random
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
    link += "<a href=/cup>擲茭</a><hr>"
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



@app.route('/cup', methods=["GET"])
def cup():
    # 檢查網址是否有 ?action=toss
    #action = request.args.get('action')
    action = request.values.get("action")
    result = None
    
    if action == 'toss':
        # 0 代表陽面，1 代表陰面
        x1 = random.randint(0, 1)
        x2 = random.randint(0, 1)
        
        # 判斷結果文字
        if x1 != x2:
            msg = "聖筊：表示神明允許、同意，或行事會順利。"
        elif x1 == 0:
            msg = "笑筊：表示神明一笑、不解，或者考慮中，行事狀況不明。"
        else:
            msg = "陰筊：表示神明否定、憤怒，或者不宜行事。"
            
        result = {
            "cup1": "/static/" + str(x1) + ".jpg",
            "cup2": "/static/" + str(x2) + ".jpg",
            "message": msg
        }
        
    return render_template('cup.html', result=result)




if __name__ == "__main__":
    app.run(debug=True)
