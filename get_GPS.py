from flask import Flask, render_template, request, redirect, url_for
import ssl
import json


app = Flask(__name__)
context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)    # 位置情報取得はhttps接続でなければならない
context.load_cert_chain('cert/server.crt', 'cert/server.key')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send-location', methods=['POST'])
def send():
    data = json.loads(request.data.decode('utf-8'))
    lat = data["lat"]
    lng = data["lng"]
    acc = data["acc"]
    print(lat, lng, acc)
    return ''


if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True, debug=True, \
      port=8080, ssl_context=context)