# location-info_app
接続された端末の位置情報をMap上に表示するやつ

## Installation
## requirements
```
Flask==1.1.1
Flask-GoogleMaps==0.2.6
```
GET GoogleMap API key FROM HERE  https://cloud.google.com/maps-platform/pricing/  
AND EDIT <code>./key_conf.py</code>
```py
GOOGLE_MAP_API_KEY = 'XXXXXXXXXXXXXXXXXXXX'    # <-- overwrite here
```
### git clone & run
```bash
$ git clone https://github.com/catdance124/location-info_app.git
$ cd location-info_app
$ ./make_cert.sh
$ python3 ./init_DB.py
$ python3 ./get_GPS.py
```

## How it works
https://localhost:8080 にアクセスしユーザ名・経路を登録する(ブラウザを表示している間のみ位置情報を送信する)  
https://localhost:8080/map にアクセスし登録地を表示する  
  
登録情報はユーザ名・経路によって識別される  

## Sample
https://localhost:8080  
![IMG_2652](https://user-images.githubusercontent.com/37448236/68749301-5829d980-0641-11ea-8276-7de65dc681c0.jpg)  

https://localhost:8080/show-map  
![IMG_2653](https://user-images.githubusercontent.com/37448236/68749304-5829d980-0641-11ea-8502-2403ca7a68ad.jpg)  

保存されたデータベース  
<table><tr><th>user_name</th><th>route_name</th><th>update_time</th><th>lat</th><th>lon</th><th>IP</th><tr><tr><td>rrr</td><td>平山→吉野</td><td>2019&#x2F;11&#x2F;13 17:50:32</td><td>31.5708101373077</td><td>130.542104236261</td><td>192.168.1.137</td></tr><tr><td>いいね</td><td>鴨池→屋久島</td><td>2019&#x2F;11&#x2F;13 17:51:12</td><td>31.5709212189834</td><td>130.542012713971</td><td>192.168.1.137</td></tr><tr><td>suzuki</td><td>平山→吉野</td><td>2019&#x2F;11&#x2F;13 17:58:28</td><td>31.5706765386757</td><td>130.541960928953</td><td>192.168.1.137</td></tr><tr><td>catdance124</td><td>桜島→鹿屋</td><td>2019&#x2F;11&#x2F;13 17:58:57</td><td>31.5706616317674</td><td>130.542155000037</td><td>192.168.1.137</td></tr></table>