import sqlite3


con = sqlite3.connect('flask-app.db')
cursor = con.cursor()

# テーブル作成
cursor.executescript("""
DROP TABLE IF EXISTS location_info;
CREATE TABLE IF NOT EXISTS location_info(user_name, route_name, update_time, lat, lon, IP, PRIMARY KEY(user_name, route_name));
""")
cursor.executescript("""
DROP TABLE IF EXISTS routes;
CREATE TABLE routes(id, name)
""")

# route情報を初期化
data = [
    (1, "平山→吉野"),
    (2, "唐湊→郡元"),
    (3, "志布志→曽於"),
    (4, "桜島→鹿屋"),
    (5, "鴨池→屋久島"),
]
p = "INSERT INTO routes(id, name) VALUES(?, ?)"
cursor.executemany(p, data)

con.commit()