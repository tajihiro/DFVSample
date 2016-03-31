import os
import json

# 環境変数取得
vcap_config = os.environ.get('VCAP_SERVICES')
if vcap_config :
    decoded_config = json.loads(vcap_config)
    credentials = decoded_config['cleardb'][0]['credentials']
    db_host = credentials['hostname']
    db_name = credentials['name']
    db_port = credentials['port']
    db_user = credentials['username']
    db_pass = credentials['password']
    db_uri = 'mysql+pymysql://'+ db_user + ':' + db_pass+ '@'+ db_host + '/' + db_name
else:
    db_uri = 'mysql+pymysql://bluemix:bluemix@localhost/dfv_bluemix_db'
