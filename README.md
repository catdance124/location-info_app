# location-info_app
接続された端末の位置情報をMap上に表示するやつ

## Installation
GET GoogleMap API key FROM HERE  https://cloud.google.com/maps-platform/pricing/
```bash
$ git clone https://github.com/catdance124/location-info_app.git
$ cd location-info_app
$ ./make_cert.sh
$ python3 ./get_GPS.py
```

## How it works
https://localhost:8080 にアクセスし現在地を登録する  
https://localhost:8080/show-map にアクセスし登録地を表示  
  
登録情報は各経路・IPアドレスによって識別される  

## Screenshots
https://localhost:8080  
![image](https://user-images.githubusercontent.com/37448236/66890234-59ef8580-f020-11e9-836c-4c4648df0028.jpg)  
https://localhost:8080/show-map  
![image](https://user-images.githubusercontent.com/37448236/66890059-a6869100-f01f-11e9-9360-03a708781e43.png)  