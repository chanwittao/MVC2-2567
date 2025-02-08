import sqlite3
import random
from datetime import datetime, timedelta

conn = sqlite3.connect("food.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS food (
    id TEXT PRIMARY KEY,
    type TEXT,
    expiry_date TEXT
)
""")

food_types = ["อาหารสด", "อาหารดอง", "อาหารกระป๋อง"]

for _ in range(50):
    food_id = str(random.randint(100000, 999999))
    food_type = random.choice(food_types)
    expiry_date = (datetime(2015, 1, 1) + timedelta(days=random.randint(0, 15*365))).strftime("%d/%m/%Y")
    cursor.execute("INSERT INTO food VALUES (?, ?, ?)", (food_id, food_type, expiry_date))

conn.commit()
conn.close()
print("✅ ฐานข้อมูลถูกสร้างเรียบร้อยแล้ว!")