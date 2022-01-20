from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import session
app=Flask(__name__)    
app.secret_key="week4test3"
@app.route("/")
def index():
        return render_template("LoginHome.html") # 首頁:LoginHome.html; 成功登入頁面:member.html; 失敗登入頁面:error.html
@app.route("/signin", methods=["POST"])
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
@app.route("/member")  # 檢查登入狀態 loginStatus
def member():
    if session["loginStatus"]=="已登入":
        return render_template("member.html")
    else:
        return render_template("LoginHome.html")
app.run(port=3000)
