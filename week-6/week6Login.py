# -*- coding: utf-8 -*-
"""
Created on Sun Feb 9 02:28:48 2022

@author: ssssw
"""
from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import session
import mysql.connector
app=Flask(__name__)    
app.secret_key="week4test3"

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456789",
    database="website"
    )
mycursor=mydb.cursor()
    #static_folder="static", 
    #static_url_path="/"
# 建立 application 物件#建立路徑 / 的處理函式
@app.route("/") #函式的decorator
def index():
        return render_template("LoginHome.html")
@app.route("/signup", methods=["POST"])
def signup():
    Name=request.form["Name"]
    userName=request.form["userName"]
    passWord=request.form["passWord"]
    sql1="SELECT member.username FROM website.member WHERE username=%s"
    val1=(userName,)
    mycursor.execute(sql1,val1)
    myresult =mycursor.fetchall()
    sql2="INSERT INTO member(name,username,password)VALUES(%s,%s,%s)"
    val2=(Name,userName,passWord)
    if myresult!=[]:
        return render_template("error.html",message="帳號已經被註冊")
    else:
        mycursor.execute(sql2,val2);
        mydb.commit()
        return render_template("LoginHome.html")
@app.route("/signin", methods=["POST"]) # 代表要處裡的網路路徑
def signin():
#   Name=request.form["Name"]
    userName=request.form["userName"]
    passWord=request.form["passWord"]
    sql1="SELECT member.username FROM website.member WHERE username=%s"
    val1=(userName,)
    mycursor.execute(sql1,val1)
    myuname =mycursor.fetchone()
    sql2="SELECT member.password FROM website.member WHERE password=%s"
    val2=(passWord,)
    mycursor.execute(sql2,val2)
    mypword =mycursor.fetchone()
    if val1==myuname and val2==mypword:
        session["userName"]=userName
        return redirect("/member")
    elif userName=="" or passWord=="":
        #session["loginStatus"]="未登入"
        return render_template("error.html",message="請輸入帳號, 密碼")
    else: 
        #session["loginStatus"]="未登入"
        return render_template("error.html",message="帳號或密碼輸入錯誤")
@app.route("/signout")
def signout():
    session["userName"]=""
    return render_template("LoginHome.html")
@app.route("/member")
def member():
    if session["userName"]!="":
        msg=session["userName"]
        return render_template("member.html",message=msg+", 歡迎登入系統")
    else:
        return render_template("LoginHome.html")
#if __name__=="__main__":
app.run(port=3000)