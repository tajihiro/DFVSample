from flask import Flask, render_template
import os

app = Flask(__name__)

#環境変数取得
if 'VCAP_APP_PORT' in os.environ:
    appPort = os.environ['VCAP_APP_PORT']
else:
    appPort = 9000

if 'VCAP_APP_HOST' in os.environ:
    appHost = os.environ['VCAP_APP_HOST']
else:
    appHost = '0.0.0.0'

@app.route('/')
def index():

    return render_template('index.html')

# サーバ起動
port = os.getenv('VCAP_APP_PORT', '5000')
if __name__ == "__main__":
    app.secret_key = 'A0Zr98j/3yX R~Xer!jmN]LWX/,?RT'
    app.run(host='0.0.0.0', port=int(port))