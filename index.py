from flask import Flask
import os

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World!'

# サーバ起動
port = os.getenv('VCAP_APP_PORT', '5000')
if __name__ == "__main__":
    app.secret_key = 'A0Zr98j/3yX R~Xer!jmN]LWX/,?RT'
    app.run(host='0.0.0.0', port=int(port))