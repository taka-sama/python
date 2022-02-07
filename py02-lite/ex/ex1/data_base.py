import sqlite3

#データベースを新規作成 or 読み込み
db = sqlite3.connect(
    "food_types",              #ファイル名
    isolation_level=None,
)

#フィールド作成用SQL文
sql = """
    CREATE TABLE Fruit (
        id INTEGER,
        name VARCHAR(20),
        price INTEGER
    );
"""

db.execute(sql)     #sql文を実行
db.close()          #データベースを閉じる