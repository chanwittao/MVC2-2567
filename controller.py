from model import FoodModel

class FoodController:
    def __init__(self):
        self.model = FoodModel()

    def validate_and_check(self, food_id):
        """ ตรวจสอบรหัสอาหาร และเช็ควันหมดอายุ """
        food = self.model.get_food_by_id(food_id)
        if not food:
            return "❌ ไม่พบข้อมูลอาหารนี้ในระบบ"

        _, food_type, expiry_date = food
        expired = self.model.check_expiry(food_type, expiry_date)
        return f"✅ อาหารยังใช้ได้" if not expired else f"⚠️ อาหารประเภท {food_type} หมดอายุแล้ว"

    def get_summary(self):
        """ ดึงข้อมูลรายงาน """
        return self.model.get_report()

    def get_all_foods(self):
        """ ดึงรายการอาหารทั้งหมด """
        return self.model.get_all_foods()