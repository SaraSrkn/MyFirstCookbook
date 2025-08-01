import sqlite3
import os

# 🔍 明確指定 DB 完整路徑（放桌面）
db_path = r"C:\Users\User\Desktop\sara_test.db"

print("📂 正在嘗試建立資料庫於：", db_path)

try:
    conn = sqlite3.connect(db_path)
    print("🔌 成功建立／連接 sara_test.db")

    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER
    )
    """)
    print("🧱 已建立資料表 users（或已存在）")

    cur.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Sara", 30))
    print("➕ 插入一筆資料成功")

    conn.commit()
    print("💾 commit 完成")

    cur.execute("SELECT * FROM users")
    rows = cur.fetchall()

    if rows:
        print("📊 查詢結果：")
        for row in rows:
            print(row)
    else:
        print("⚠ No data found.")

    conn.close()
    print("✅ 資料庫已關閉")

except Exception as e:
    print("❌ 出錯：", e)

# 額外提示（確認目錄）
print("📁 目前執行目錄：", os.getcwd())
