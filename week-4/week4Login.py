from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import session
app=Flask(__name__)    
app.secret_key="week4test3"
    #static_folder="static", 
    #static_url_path="/"
# 建立 application 物件#建立路徑 / 的處理函式
@app.route("/") #函式的decorator
def index():
        return render_template("LoginHome.html")

@app.route("/signin", methods=["POST"]) # 代表要處裡的網路路徑
def signin():
    userID=request.form["userID"]
    passWord=request.form["passWord"]
    if userID=="test" and passWord=="test":
        session["userName"]=userID
        session["loginStatus"]="已登入"
        return redirect("/member")
    elif userID=="" or passWord=="":
        session["loginStatus"]="未登入"
        return render_template("error.html",message="請輸入帳號, 密碼")
    else: 
        session["loginStatus"]="未登入"
        return render_template("error.html",message="帳號, 或密碼輸入錯誤")
@app.route("/signout")
def signout():
    session["loginStatus"]="未登入"
    return render_template("LoginHome.html")
@app.route("/member")
def member():
    if session["loginStatus"]=="已登入":
        return render_template("member.html")
    else:
        return render_template("LoginHome.html")
#if __name__=="__main__":
app.run(port=3000)