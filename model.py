import sqlite3
from datetime import datetime, timedelta
import logging

# ตั้งค่าระบบ Log
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("FoodModel")


class FoodModel:
    def __init__(self, db_path="food.db"):
        """ เชื่อมต่อฐานข้อมูล """
        try:
            self.conn = sqlite3.connect(db_path)
            self.cursor = self.conn.cursor()
            logger.info("เชื่อมต่อฐานข้อมูลสำเร็จ")
            # รายงานการตรวจสอบอาหาร
            self.report = {
                "อาหารสด": {"ใช้ได้": 0, "เสีย": 0},
                "อาหารดอง": {"ใช้ได้": 0, "เสีย": 0},
                "อาหารกระป๋อง": {"ใช้ได้": 0, "เสีย": 0},
            }
        except Exception as e:
            logger.error(f"เกิดข้อผิดพลาดในการเชื่อมต่อฐานข้อมูล: {e}")

    def get_food_by_id(self, food_id):
        """ ดึงข้อมูลอาหารจากฐานข้อมูลตามรหัส """
        try:
            self.cursor.execute("SELECT * FROM food WHERE id = ?", (food_id,))
            return self.cursor.fetchone()
        except Exception as e:
            logger.error(f"Error fetching food data: {e}")
            return None

    def check_expiry(self, food_type, expiry_date):
        """ ตรวจสอบว่าอาหารหมดอายุหรือไม่ """
        today = datetime.today()
        expiry = datetime.strptime(expiry_date, "%d/%m/%Y")
        expired = False

        if food_type == "อาหารสด":
            expired = today > expiry
        elif food_type == "อาหารดอง":
            expired = today.year > expiry.year or (today.year == expiry.year and today.month > expiry.month)
        elif food_type == "อาหารกระป๋อง":
            extended_expiry = expiry + timedelta(days=9*30)
            expired = today > extended_expiry

        # อัปเดตรายงาน
        if expired:
            self.report[food_type]["เสีย"] += 1
        else:
            self.report[food_type]["ใช้ได้"] += 1

        return expired

    def get_report(self):
        """ ดึงรายงานจำนวนอาหารที่ตรวจสอบแล้ว """
        return self.report

    def get_all_foods(self):
        """ ดึงรายการอาหารทั้งหมด """
        try:
            self.cursor.execute("SELECT id, type, expiry_date FROM food")
            return self.cursor.fetchall()
        except Exception as e:
            logger.error(f"Error fetching all foods: {e}")
            return []

    def close_connection(self):
        """ ปิดการเชื่อมต่อฐานข้อมูล """
        self.conn.close()
        logger.info("ปิดการเชื่อมต่อฐานข้อมูลสำเร็จ")