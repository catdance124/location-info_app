from flask import Flask, render_template, request, redirect, url_for
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map
import ssl
import json
import os
import pandas as pd
## GOOGLE_MAP_API_KEY
from key_conf import *


# 初期設定
app = Flask(__name__)
GoogleMaps(app, key=GOOGLE_MAP_API_KEY)
context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)    # 位置情報取得はhttps接続でなければならない
context.load_cert_chain('cert/server.crt', 'cert/server.key')
if not os.path.exists('./df.pkl'):
    df = pd.DataFrame(index=[], columns=['addr', 'route_id', 'route_name','lat', 'lng'])
    df.to_pickle(f'./df.pkl')


# 位置情報を送信させるページ
@app.route('/')
def index():
    return render_template('index.html')

# POSTされた情報を受け取るページ
@app.route('/send-location', methods=['POST'])
def send():
    data = json.loads(request.data.decode('utf-8'))
    addr = request.remote_addr
    lat = data["lat"]
    lng = data["lng"]
    acc = data["acc"]
    route_id = data["route_id"]
    route_name = data["route_name"]
    # load pkl
    df = pd.read_pickle('./df.pkl')
    record = pd.Series([addr, route_id, route_name, lat, lng], index=df.columns)
    df = df.append(record, ignore_index=True)
    df = df.drop_duplicates(keep=False, subset=['addr', 'route_id'])
    df.to_pickle('./df.pkl')
    return ''

# POSTされた情報を地図に描画するページ
@app.route('/show-map')
def mapview():
    df = pd.read_pickle('./df.pkl')
    subset = df[['lat', 'lng', 'route_name']]
    locations = [tuple(x) for x in subset.values]
    # マップを作成
    mymap = Map(
        identifier = "view",
        lat = 31.581319,
        lng = 130.544519,
        markers = [(loc[0], loc[1], loc[2]) for loc in locations],
        fit_markers_to_bounds = len(locations) > 1,
        style = "height:800px; width:80%; margin:auto; text-align:center;",
        region = "JPN"
    )
    return render_template('map.html', mymap=mymap)

if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True, debug=True, port=8080, ssl_context=context)