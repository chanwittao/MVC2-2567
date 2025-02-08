import tkinter as tk
from controller import FoodController
from view import FoodView

if __name__ == "__main__":
    root = tk.Tk()
    controller = FoodController()
    app = FoodView(root, controller)
    root.mainloop()