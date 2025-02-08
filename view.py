import tkinter as tk
from tkinter import messagebox, Toplevel, ttk


class FoodView:
    def __init__(self, root, controller):
        self.controller = controller
        self.root = root
        self.root.title("ระบบตรวจสอบคุณภาพสินค้า")

        tk.Label(root, text="กรุณาป้อนรหัสสินค้า (6 หลัก):").pack(pady=5)
        self.entry = tk.Entry(root)
        self.entry.pack(pady=5)

        self.check_button = tk.Button(root, text="ตรวจสอบสถานะสินค้า ✅", command=self.check_food)
        self.check_button.pack(pady=10)

        self.report_button = tk.Button(root, text="สรุปผลการตรวจสอบ 📊", command=self.show_report)
        self.report_button.pack(pady=10)

        self.list_button = tk.Button(root, text="แสดงรายการสินค้า 📋", command=self.show_food_list)
        self.list_button.pack(pady=10)

        self.result_label = tk.Label(root, text="", fg="blue")
        self.result_label.pack(pady=10)

    def check_food(self):
        food_id = self.entry.get()
        result = self.controller.validate_and_check(food_id)
        self.result_label.config(text=result, fg="red" if "⚠️" in result or "❌" in result else "green")

    def show_report(self):
        report = self.controller.get_summary()
        if not report:
            messagebox.showinfo("รายงาน", "ยังไม่มีการตรวจสอบสินค้า")
            return

        report_text = ""
        for food_type, counts in report.items():
            report_text += f"{food_type}:\n  ใช้ได้: {counts['ใช้ได้']} รายการ\n  เสีย: {counts['เสีย']} รายการ\n\n"
        messagebox.showinfo("สรุปผลการตรวจสอบ", report_text)

    def show_food_list(self):
        food_list_window = Toplevel(self.root)
        food_list_window.title("รายการสินค้าทั้งหมด")

        food_list = self.controller.get_all_foods()
        tree = ttk.Treeview(food_list_window, columns=("รหัสสินค้า", "ประเภท", "วันหมดอายุ"), show="headings")
        tree.heading("รหัสสินค้า", text="รหัสสินค้า")
        tree.heading("ประเภท", text="ประเภท")
        tree.heading("วันหมดอายุ", text="วันหมดอายุ")
        tree.pack(fill=tk.BOTH, expand=True)

        for food in food_list:
            tree.insert("", "end", values=food)