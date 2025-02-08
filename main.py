import tkinter as tk
from model import FoodModel
from controller import FoodController
from view import FoodView

if __name__ == "__main__":
    root = tk.Tk()
    model = FoodModel()
    controller = FoodController(model)
    app = FoodView(root, controller)
    root.mainloop()