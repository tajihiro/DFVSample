import os
import json

# ホスト名
if 'VCAP_APP_HOST' in os.environ:
    appHost = os.environ['VCAP_APP_HOST']
else:
    appHost = '0.0.0.0'

# ポート番号
if 'VCAP_APP_PORT' in os.environ:
    appPort = os.environ['VCAP_APP_PORT']
else:
    appPort = 9000

# DBサーバ
vcap_config = os.environ.get('VCAP_SERVICES')
if vcap_config :
    #DBサーバ環境
    decoded_config = json.loads(vcap_config)
    credentials = decoded_config['cleardb'][0]['credentials']
    db_host = credentials['hostname']
    db_name = credentials['name']
    db_port = credentials['port']
    db_user = credentials['username']
    db_pass = credentials['password']
    db_uri = 'mysql+pymysql://'+ db_user + ':' + db_pass+ '@'+ db_host + '/' + db_name + '?charset=utf8'
else:
    #DBローカル開発環境
    db_uri = 'mysql+pymysql://bluemix:bluemix@localhost/dfv_bluemix_db?charset=utf8'
