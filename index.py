from flask import Flask, request, redirect, url_for, render_template, flash
from config import appHost, appPort
from models import UserAgent
from database import db_session

import woothee

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register', methods=['POST'])
def register():
    #パラメータ取得
    agent_cd = request.form['agent_cd']
    agent_name = request.form['agent_name']

    #パラメータチェック
    if not agent_cd or not agent_name:
        flash('入力してください。')
        return redirect(url_for('login'))

    #UserAgent取得
    header = request.headers.get('User-Agent')
    ua = woothee.parse(header)
    category = ua.get('category')
    name = ua.get('name')
    version = ua.get('version')
    os_name = ua.get('os')
    vendor = ua.get('vendor')
    os_version = ua.get('os_version')

    #DB登録処理
    user_agent = UserAgent(agent_cd=agent_cd, agent_name=agent_name, category=category, name=name,
                         version=version, os_name=os_name, vendor=vendor, os_version=os_version)
    try:
        db_session.add(user_agent)
        db_session.commit()
    except Exception as e:
        db_session.rollback()
        flash('既に登録済みです。')
        return redirect(url_for('login'))
    finally:
        db_session.close()

    return render_template('register.html')

# サーバ起動
if __name__ == "__main__":
    app.secret_key = 'A0Zr98j/3yX R~Xer!jmN]LWX/,?RT'
    app.run(host=appHost, port=int(appPort))