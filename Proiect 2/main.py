import tkinter as tk
from tkinter import ttk
import math


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Proiect 2")
        self.iconbitmap('draw.ico')

        # Frame pentru zona verticala 1
        frame1 = ttk.Frame(self)
        frame1.grid(row=0, column=0, padx=10, pady=10)

        self.listbox1 = tk.Listbox(frame1, height=10)
        self.listbox1.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)


        self.listbox2 = tk.Listbox(frame1, height=10)
        self.listbox2.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)


        # Frame pentru zona 2 (desenul figurii selectate)
        frame_draw1 = ttk.Frame(self)
        frame_draw1.grid(row=0, column=1, padx=10, pady=10)

        self.canvas1 = tk.Canvas(frame_draw1, width=200, height=200, bg="white")
        self.canvas1.pack(fill=tk.BOTH, expand=True)

        # Frame pentru zona vericala 3 (rezultatul)
        frame_draw2 = ttk.Frame(self)
        frame_draw2.grid(row=0, column=2, padx=10, pady=10)

        self.canvas2 = tk.Canvas(frame_draw2, width=200, height=200, bg="white")
        self.canvas2.pack(fill=tk.BOTH, expand=True)

        self.populate_list()
        self.current_figure_coords = None

    def populate_list(self):
        items = ["Segment", "Triunghi", "Patrat","Hexagon", "Cerc"]
        items2 = ["Translatie", "Omotetie", "Rotatie", "Simetrie"]

        for item in items:
            self.listbox1.insert(tk.END, item)

        self.listbox1.bind('<<ListboxSelect>>', self.draw_figure)

        for item in items2:
            self.listbox2.insert(tk.END, item)

        self.listbox2.bind('<<ListboxSelect>>', self.draw_transformare)


    def draw_figure(self, event):
        selection = self.listbox1.get(tk.ACTIVE)
        self.canvas1.delete("all")
        self.current_figure_coords = None

        # Desenează reperul xOy
        self.draw_axes(self.canvas1)

        if selection == "Segment":
            self.current_figure_coords = self.draw_segment(self.canvas1)
        elif selection == "Patrat":
            self.current_figure_coords = self.draw_square(self.canvas1)
        elif selection == "Cerc":
            self.current_figure_coords = self.draw_circle(self.canvas1)
        elif selection == "Triunghi":
            self.current_figure_coords = self.draw_itriangle(self.canvas1)
        elif selection == "Hexagon":
            self.current_figure_coords = self.draw_hexagon(self.canvas1)

    def draw_axes(self, canvas):
        width = canvas.winfo_width()
        height = canvas.winfo_height()
        canvas.create_line(width // 2, 0, width // 2, height, fill="gray")  # Axa Y
        canvas.create_line(0, height // 2, width, height // 2, fill="gray")  # Axa X

    def draw_segment(self, canvas):
        center_x = canvas.winfo_width() // 2
        center_y = canvas.winfo_height() // 2
        return canvas.create_line(center_x - 50, center_y, center_x + 50, center_y, fill="black")

    def draw_square(self, canvas):
        center_x = canvas.winfo_width() // 2
        center_y = canvas.winfo_height() // 2
        return canvas.create_rectangle(center_x - 50, center_y - 50, center_x + 50, center_y + 50, outline="blue")

    def draw_circle(self, canvas):
        center_x = canvas.winfo_width() // 2
        center_y = canvas.winfo_height() // 2
        return canvas.create_oval(center_x - 50, center_y - 50, center_x + 50, center_y + 50, outline="blue")

    def draw_itriangle(self, canvas):
        center_x = canvas.winfo_width() // 2
        center_y = canvas.winfo_height() // 2
        x1, y1 = center_x - 50, center_y
        x2, y2 = center_x, center_y - 50
        x3, y3 = center_x + 50, center_y
        return canvas.create_polygon(x1, y1, x2, y2, x3, y3, fill="", outline="blue")

    def draw_hexagon(self, canvas):
        center_x = canvas.winfo_width() // 2
        center_y = canvas.winfo_height() // 2
        x1, y1 = center_x + 50, center_y
        x2, y2 = center_x + 25, center_y + 25*math.sqrt(3)
        x3, y3 = center_x - 25, center_y + 25*math.sqrt(3)
        x4, y4 = center_x - 50, center_y
        x5, y5 = center_x - 25, center_y - 25*math.sqrt(3)
        x6, y6 = center_x + 25, center_y - 25*math.sqrt(3)
        return canvas.create_polygon(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6, fill="", outline="blue")

    def draw_transformare(self, event):
        self.canvas2.delete("all")
        # Desenează axele X și Y pe canvas2
        self.draw_axes(self.canvas2)
        center_x = self.canvas2.winfo_width() // 2
        center_y = self.canvas2.winfo_height() // 2
        figura = self.listbox1.curselection()
        transforare= self.listbox2.curselection()
        if figura == "Segment":
            if transforare == "Translatie":
                return self.canvas2.create_line(center_x - 45, center_y, center_x + 55, center_y, fill="blue")
            elif transforare == "Omotetie":
                return self.canvas2.create_line((center_x - 50) * 2, center_y * 2, (center_x + 50) * 2, center_y * 2,fill="black")
            elif transforare == "Simetrie":
                return self.canvas2.create_line(center_x - 50, -center_y, center_x + 50, -center_y, fill="black")
        elif figura == "Hexagon":
                if transforare == "Translatie":
                    x1, y1 = center_x + 55, center_y + 5
                    x2, y2 = center_x + 30, center_y + 25 * math.sqrt(3) + 5
                    x3, y3 = center_x - 20, center_y + 25 * math.sqrt(3) + 5
                    x4, y4 = center_x - 45, center_y + 5
                    x5, y5 = center_x - 20, center_y - 25 * math.sqrt(3) + 5
                    x6, y6 = center_x + 55, center_y - 25 * math.sqrt(3) + 5
                    return self.canvas2.create_polygon(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6, fill="", outline="blue")
                elif transforare == "Omotetie":
                    x1, y1 = center_x + 50, center_y
                    x2, y2 = center_x + 25, center_y + 25 * math.sqrt(3)
                    x3, y3 = center_x - 25, center_y + 25 * math.sqrt(3)
                    x4, y4 = center_x - 50, center_y
                    x5, y5 = center_x - 25, center_y - 25 * math.sqrt(3)
                    x6, y6 = center_x + 25, center_y - 25 * math.sqrt(3)
                    return self.canvas2.create_polygon(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6, fill="", outline="blue")
        elif figura == "Cerc":
            if transforare == "Translatie":
                return self.canvas2.create_oval(center_x - 45, center_y - 45, center_x + 55, center_y + 55, outline="blue")
            elif transforare == "Omotetie":
                return self.canvas2.create_oval((center_x - 50)*2, (center_y - 50)*2, (center_x + 50)*2, (center_y + 50)*2, outline="blue")
        elif figura == "Triunghi":
            if transforare == "Translatie":
                return self.canvas2.create_polygon(center_x - 45, center_y+5, center_x + 55, center_y+5, center_x - 45, center_y+5, center_x+5, center_y - 45, center_x + 55, center_y+5, center_x+5, center_y - 45 , outline="blue")
            elif transforare == "Omotetie":
                return self.canvas2.create_line((center_x - 50) * 2, center_y * 2, (center_x + 50) * 2, center_y * 2, fill="black")
            elif transforare == "Simetrie":
                return self.canvas2.create_oval(center_x - 50, center_y + 50, center_x + 50, center_y - 50, outline="blue")

        elif figura== "Patrat":
            if transforare == "Translatie":
                return self.canvas2.create_rectangle(center_x - 45, center_y - 45, center_x + 55, center_y + 55, outline="blue")
            elif transforare == "Omotetie":
                return self.canvas2.create_rectangle((center_x - 50) * 2, (center_y - 50) * 2, (center_x + 50) * 2,(center_y + 50) * 2, outline="blue")
            elif transforare == "Simetrie":
                return self.canvas2.create_rectangle(center_x - 50, center_y + 50, center_x + 50, center_y - 50, outline="blue")


    def apply_translatie(self, canvas):
        self.canvas2.delete("all")
        # Desenează axele X și Y pe canvas2
        self.draw_axes(self.canvas2)
        center_x = canvas.winfo_width() // 2
        center_y = canvas.winfo_height() // 2
        if self.current_figure_coords:
            selection = self.listbox1.get(tk.ACTIVE)
            if selection == "Segment":
                return canvas.create_line(center_x - 45, center_y+5, center_x + 55, center_y+5, fill="black")
            elif selection == "Pătrat":
                self.transform_square(self.canvas2)
            elif selection == "Cerc":
                self.transform_circle(self.canvas2)

    def apply_rotatie(self):
        formula = self.entry.get()
        self.canvas2.delete("all")

        # Desenează axele X și Y pe canvas2
        self.draw_axes(self.canvas2)

        if self.current_figure_coords:
            selection = self.listbox1.get(tk.ACTIVE)
            if selection == "Segment":
                self.transform_segment(self.canvas2, formula)
            elif selection == "Pătrat":
                self.transform_square(self.canvas2, formula)
            elif selection == "Cerc":
                self.transform_circle(self.canvas2, formula)

    def apply_omotetie(self):
        self.canvas2.delete("all")

        # Desenează axele X și Y pe canvas2
        self.draw_axes(self.canvas2)

        if self.current_figure_coords:
            selection = self.listbox1.get(tk.ACTIVE)
            if selection == "Segment":
                self.transform_segment(self.canvas2)
            elif selection == "Pătrat":
                self.transform_square(self.canvas2)
            elif selection == "Cerc":
                self.transform_circle(self.canvas2)

    def apply_simetrie(self):
        self.canvas2.delete("all")

        # Desenează axele X și Y pe canvas2
        self.draw_axes(self.canvas2)

        if self.current_figure_coords:
            selection = self.listbox1.get(tk.ACTIVE)
            if selection == "Segment":
                self.transform_segment(self.canvas2)
            elif selection == "Pătrat":
                self.transform_square(self.canvas2)
            elif selection == "Cerc":
                self.transform_circle(self.canvas2)

    def apply_transformation(self):
        formula = self.entry.get()
        self.canvas2.delete("all")

        # Desenează axele X și Y pe canvas2
        self.draw_axes(self.canvas2)

        if self.current_figure_coords:
            selection = self.listbox1.get(tk.ACTIVE)
            if selection == "Segment":
                self.transform_segment(self.canvas2, formula)
            elif selection == "Pătrat":
                self.transform_square(self.canvas2, formula)
            elif selection == "Cerc":
                self.transform_circle(self.canvas2, formula)

    def transform_segment(self, canvas, formula):
        try:
            x1, y1, x2, y2 = -50, 0, 50, 0
            exec(formula)
            center_x = canvas.winfo_width() // 2
            center_y = canvas.winfo_height() // 2
            canvas.create_line(center_x + x1, center_y - y1, center_x + x2, center_y - y2, fill="black")
        except Exception as e:
            print("Error in formula:", e)

    def transform_square(self, canvas, formula):
        try:
            x1, y1, x2, y2 = -50, -50, 50, 50
            exec(formula)
            center_x = canvas.winfo_width() // 2
            center_y = canvas.winfo_height() // 2
            canvas.create_rectangle(center_x + x1, center_y - y1, center_x + x2, center_y - y2, outline="black")
        except Exception as e:
            print("Error in formula:", e)

    def transform_circle(self, canvas, formula):
        try:
            x1, y1, x2, y2 = -50, -50, 50, 50
            exec(formula)
            center_x = canvas.winfo_width() // 2
            center_y = canvas.winfo_height() // 2
            canvas.create_oval(center_x + x1, center_y - y1, center_x + x2, center_y - y2, outline="black")
        except Exception as e:
            print("Error in formula:", e)

    def transform_triangle(self, canvas, formula):
        try:
            x1, y1, x2, y2, x3, y3 = 0, -50, -50, 50, 50, 50
            exec(formula)
            center_x = canvas.winfo_width() // 2
            center_y = canvas.winfo_height() // 2
            canvas.create_polygon(center_x + x1, center_y - y1, center_x + x2, center_y - y2, center_x + x3,
                                  center_y - y3, outline="black", fill='')
        except Exception as e:
            print("Error in formula:", e)


if __name__ == "__main__":
    app = Application()
    app.mainloop()
