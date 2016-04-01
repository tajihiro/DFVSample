from flask import Flask, request, render_template
from config import appHost, appPort
from models import UserAgent
from database import db_session

import woothee

app = Flask(__name__)

@app.route('/')
def index():
    #パラメータ取得
    agent_cd = '211132'.encode('utf-8')
    agent_name = '田島'.encode('utf-8')

    #UserAgent取得
    header = request.headers.get('User-Agent')
    ua = woothee.parse(header)
    category = ua.get('category')
    name = ua.get('name')
    version = ua.get('version')
    os_name = ua.get('os_name')
    vendor = ua.get('vendor')
    os_version = ua.get('os_version')

    #DB登録処理
    user_agent = UserAgent(agent_cd=agent_cd, agent_name=agent_name, category=category, name=name,
                         version=version, os_name=os_name, vendor=vendor, os_version=os_version)

    db_session.add(user_agent)
    db_session.commit()

    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():

    return render_template('register.html')

# サーバ起動
if __name__ == "__main__":
    app.secret_key = 'A0Zr98j/3yX R~Xer!jmN]LWX/,?RT'
    app.run(host=appHost, port=int(appPort))