from tkinter import Canvas, Entry, Button, PhotoImage
import tkinter as tk
from tkinter import messagebox
from .variables import *
from .data_base_connection import DBSample


class PopUpWindow:
    def input_new_film(self):
        title, author, year, rate = self.entry_title.get(), self.entry_author.get(), self.entry_year.get(), self.entry_rate.get()
        check, description = self.validate_entry(title, author, year, rate)
        if check is True:
            input = DBSample()
            input.create_new_row(title, author, int(year), float(rate))
            messagebox.showinfo("Success", description)
            self.callback_function()
            self.new_item_window.destroy()
            
        else:
            messagebox.showinfo("Error", description)
    
    def change_film(self):
        title, author, year, rate = self.entry_title.get(), self.entry_author.get(), self.entry_year.get(), self.entry_rate.get()
        check, description = self.validate_entry(title, author, year, rate)
        if check is True:
            change_db = DBSample()
            change_db.change_by_id(self.id, title, author, int(year), float(rate))
            messagebox.showinfo("Success", description)
            self.callback_function()
            self.new_item_window.destroy()
            
        else:
            messagebox.showinfo("Error", description)

    def validate_entry(self, title, author, year, rate):
        # Check if title and author are not blank
        if not title or not author:
            return False, "Title and author cannot be blank"

        # Check if year is a valid number
        try:
            year = int(year)
            if year < 0:
                raise ValueError("Year must be a positive number")
        except ValueError:
            return False, "Invalid year"

        # Check if rate is a valid number between 0 and 10.0
        try:
            rate = float(rate)
            if not 0 <= rate <= 10.0:
                raise ValueError("Rate must be between 0 and 10.0")
        except ValueError:
            return False, "Invalid rate"

        # All conditions passed
        return True, "Validation successful"

    def __init__(self, master_window, callback_function, title=None, author=None, year=None, rate=None, func=False, id=None):
        # This one is for change function
        self.id = id 
        
        self.new_item_window = tk.Toplevel(master_window)

        self.new_item_window.attributes('-topmost', True)
        self.callback_function = callback_function

        self.new_item_window.title("New Item")
        self.new_item_window.geometry("320x330")
        self.new_item_window.configure(bg = "#FFFFFF")


        self.item_canvas = Canvas(
            self.new_item_window,
            bg = "#FFFFFF",
            height = 330,
            width = 320,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.item_canvas.place(x = 0, y = 0)
        self.entry_image_1 = PhotoImage(
            file=relative_to_assets("smaller_entry.png"))
        self.entry_bg_1 = self.item_canvas.create_image(
            162.5,
            80.5,
            image=self.entry_image_1
        )
        self.entry_title = Entry(
            self.new_item_window,
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        if title:
            self.entry_title.insert(0, title)
        self.entry_title.place(
            x=36.5,
            y=69.0,
            width=252.0,
            height=21.0
        )

        self.item_canvas.create_rectangle(
            0.0,
            0.0,
            320.0,
            40.0,
            fill="#63AFD0",
            outline="")

        if func:
            self.item_canvas.create_text(
                11.0,
                5.0,
                anchor="nw",
                text="Change film info",
                fill="#070633",
                font=("Jokerman Regular", 20 * -1)
            )
        else:
            self.item_canvas.create_text(
                11.0,
                5.0,
                anchor="nw",
                text="Information about new film",
                fill="#070633",
                font=("Jokerman Regular", 20 * -1)
            )

        self.item_canvas.create_text(
            137.0,
            51.0,
            anchor="nw",
            text="film title",
            fill="#000000",
            font=("Jomolhari Regular", 12 * -1)
        )

        self.entry_image_2 = PhotoImage(
            file=relative_to_assets("smaller_entry.png"))
        self.entry_bg_2 = self.item_canvas.create_image(
            162.5,
            246.5,
            image=self.entry_image_2
        )
        self.entry_rate = Entry(
            self.new_item_window,
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        if rate:
            self.entry_rate.insert(0, rate)
        self.entry_rate.place(
            x=36.5,
            y=235.0,
            width=252.0,
            height=21.0
        )

        self.item_canvas.create_text(
            126.0,
            217.0,
            anchor="nw",
            text="review (0-10.0)",
            fill="#000000",
            font=("Jomolhari Regular", 12 * -1)
        )

        self.entry_image_3 = PhotoImage(
            file=relative_to_assets("smaller_entry.png"))
        self.entry_bg_3 = self.item_canvas.create_image(
            162.5,
            189.5,
            image=self.entry_image_3
        )
        self.entry_year = Entry(
            self.new_item_window,
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        if year:
            self.entry_year.insert(0, year)
        self.entry_year.place(
            x=36.5,
            y=178.0,
            width=252.0,
            height=21.0
        )

        self.item_canvas.create_text(
            148.0,
            160.0,
            anchor="nw",
            text="year",
            fill="#000000",
            font=("Jomolhari Regular", 12 * -1)
        )

        self.entry_image_4 = PhotoImage(
            file=relative_to_assets("smaller_entry.png"))
        self.entry_bg_4 = self.item_canvas.create_image(
            162.5,
            132.5,
            image=self.entry_image_4
        )
        self.entry_author = Entry(
            self.new_item_window,
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        if author:
            self.entry_author.insert(0, author)
        self.entry_author.place(
            x=36.5,
            y=121.0,
            width=252.0,
            height=21.0
        )

        self.item_canvas.create_text(
            143.0,
            103.0,
            anchor="nw",
            text="author",
            fill="#000000",
            font=("Jomolhari Regular", 12 * -1)
        )

        if func:
            self.new_item_window.title("Editor")
            self.new_item_window.button_image_1_1 = PhotoImage(
                file=relative_to_assets("button_submit.png"))
            button_1_1 = Button(
                self.new_item_window,
                image=self.new_item_window.button_image_1_1,
                borderwidth=0,
                highlightthickness=0,
                command=self.change_film,
                relief="flat"
            )
        else:
            self.new_item_window.title("Creator")
            self.new_item_window.button_image_1_1 = PhotoImage(
                file=relative_to_assets("button_create.png"))
            button_1_1 = Button(
                self.new_item_window,
                image=self.new_item_window.button_image_1_1,
                borderwidth=0,
                highlightthickness=0,
                command=self.input_new_film,
                relief="flat"
            )
        button_1_1.place(
            x=85.0,
            y=274.0,
            width=150.0,
            height=40.0
        )
        self.new_item_window.resizable(False, False)