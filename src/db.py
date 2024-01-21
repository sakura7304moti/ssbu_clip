import sqlite3

def insert_nameList(dbname:str):
    # データベースに接続する
    conn = sqlite3.connect(dbname)
    cursor = conn.cursor()
    # SELECTクエリを実行
    cursor.execute("INSERT INTO nameList(key,val) select name,ssbu_name from nameList2 as n2 where not exists(select key from nameList as n1 where n1.key = n2.name)")
    conn.commit()
    conn.close()