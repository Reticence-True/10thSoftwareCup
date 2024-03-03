from sqlite import Database
data = Database('videos.db')
data.initdb() #建表语句调用一次就行
data.insert('temp_vdo/2021-07-13 17.39.27.mp4', '2021-07-13 17:39:38', '99min 1s', 1.0)
print(data.search())
data.close_db()

 