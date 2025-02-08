class FoodController:
    def __init__(self, model):
        self.model = model

    def validate_and_check(self, food_id):
        """ ตรวจสอบรหัสอาหาร และเช็ควันหมดอายุ """
        if not food_id.isdigit() or len(food_id) != 6:
            return "⚠️ รหัสสินค้าไม่ถูกต้อง! กรุณากรอกตัวเลข 6 หลัก"
        if food_id[0] == "0":
            return "⚠️ รหัสสินค้าไม่ถูกต้อง! รหัสห้ามขึ้นต้นด้วยเลข 0"

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