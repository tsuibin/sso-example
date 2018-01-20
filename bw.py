#coding: utf8
import os
from datetime import timedelta
from flask import Flask, session, redirect, url_for, request
import urllib

app = Flask(__name__)

app.secret_key = os.urandom(24)
app.permanent_session_lifetime = timedelta(seconds=24 * 60 * 60)

@app.route('/')
def index():
    #表示存活期为浏览器进程的存活期
    session.permanent = False
    ticket = request.args.get('ticket', None)
    if ticket is not None:
        session['name'] = ticket.strip()
    #检测登录态
    if 'name' in session:
        return '登录成功'
    else:
        referer = urllib.quote('http://127.0.0.1:5002/')
        return redirect('http://127.0.0.1:5000/login?referer=' + referer)

if __name__ == '__main__':
    app.run(
        host="127.0.0.1",
        port=int("5002"),
        debug=True
    )
