from flask import Flask, render_template, request, redirect, url_for
from flask_googlemaps import GoogleMaps, Map
import ssl, datetime, json
import sqlite3
from contextlib import closing
## GOOGLE_MAP_API_KEY
from key_conf import *


# 初期設定
app = Flask(__name__)
GoogleMaps(app, key=GOOGLE_MAP_API_KEY)
context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)    # 位置情報取得はhttps接続でなければならない
context.load_cert_chain('cert/server.crt', 'cert/server.key')
dbname = 'flask-app.db'

# 位置情報を送信させるページ
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        with closing(sqlite3.connect(dbname)) as con:
            cursor = con.cursor()
            cursor.execute('SELECT * FROM routes')
            routes = cursor.fetchall()
        return render_template('index.html', routes=routes)
    else:
        return render_template('status.html', user_name=request.form["user_name"], route_name=request.form["route_select"])

# POSTされた情報を受け取るページ
@app.route('/send-location', methods=['POST'])
def send():
    data = json.loads(request.data.decode('utf-8'))
    addr = request.remote_addr
    lat = data["lat"]
    lon = data["lon"]
    user_name = data["user_name"]
    route_name = data["route_name"]
    update_time = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    # add DB
    with closing(sqlite3.connect(dbname)) as con:
        cursor = con.cursor()
        cursor.execute("REPLACE INTO location_info VALUES (?, ?, ?, ?, ?, ?)", \
            (user_name, route_name, update_time, lat, lon, addr))
        con.commit()
    return ''

# POSTされた情報を地図に描画するページ
@app.route('/map')
def mapview():
    with closing(sqlite3.connect(dbname)) as con:
        cursor = con.cursor()
        cursor.execute('SELECT lat, lon, route_name FROM location_info')
        location_info = cursor.fetchall()
    # location_info
    # df = pd.read_pickle('./df.pkl')
    # subset = df[['lat', 'lon', 'route_name']]
    # locations = [tuple(x) for x in subset.values]
    locations = location_info
    # マップを作成
    mymap = Map(
        identifier = "view",
        lat = 31.581319,
        lng = 130.544519,
        markers = locations,#[(loc[0], loc[1], loc[2]) for loc in locations],
        fit_markers_to_bounds = len(locations) > 1,
        style = "height:800px; width:80%; margin:auto; text-align:center;",
        region = "JPN"
    )
    return render_template('map.html', mymap=mymap)

if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True, debug=True, port=8080, ssl_context=context)