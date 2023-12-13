from tkinter import Tk, Canvas, Entry, Button, PhotoImage
import tkinter as tk
from .data import *
from .variables import *


class PopUpWindow:
    def __init__(self, master_window):
        new_item_window = tk.Toplevel(master_window)
        new_item_window.title("New Item")
        new_item_window.geometry("320x330")
        new_item_window.configure(bg = "#FFFFFF")


        item_canvas = Canvas(
            new_item_window,
            bg = "#FFFFFF",
            height = 330,
            width = 320,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        item_canvas.place(x = 0, y = 0)
        entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1_1.png"))
        entry_bg_1 = item_canvas.create_image(
            162.5,
            80.5,
            image=entry_image_1
        )
        entry_1 = Entry(
            new_item_window,
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        entry_1.place(
            x=36.5,
            y=69.0,
            width=252.0,
            height=21.0
        )

        item_canvas.create_rectangle(
            0.0,
            0.0,
            320.0,
            40.0,
            fill="#63AFD0",
            outline="")

        item_canvas.create_text(
            11.0,
            5.0,
            anchor="nw",
            text="Information about new film",
            fill="#070633",
            font=("Jokerman Regular", 20 * -1)
        )

        item_canvas.create_text(
            137.0,
            51.0,
            anchor="nw",
            text="film title",
            fill="#000000",
            font=("Jomolhari Regular", 12 * -1)
        )

        entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_2_1.png"))
        entry_bg_2 = item_canvas.create_image(
            162.5,
            246.5,
            image=entry_image_2
        )
        entry_2 = Entry(
            new_item_window,
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        entry_2.place(
            x=36.5,
            y=235.0,
            width=252.0,
            height=21.0
        )

        item_canvas.create_text(
            126.0,
            217.0,
            anchor="nw",
            text="review (0-10.0)",
            fill="#000000",
            font=("Jomolhari Regular", 12 * -1)
        )

        entry_image_3 = PhotoImage(
            file=relative_to_assets("entry_3_1.png"))
        entry_bg_3 = item_canvas.create_image(
            162.5,
            189.5,
            image=entry_image_3
        )
        entry_3 = Entry(
            new_item_window,
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        entry_3.place(
            x=36.5,
            y=178.0,
            width=252.0,
            height=21.0
        )

        item_canvas.create_text(
            148.0,
            160.0,
            anchor="nw",
            text="year",
            fill="#000000",
            font=("Jomolhari Regular", 12 * -1)
        )

        entry_image_4 = PhotoImage(
            file=relative_to_assets("entry_4_1.png"))
        entry_bg_4 = item_canvas.create_image(
            162.5,
            132.5,
            image=entry_image_4
        )
        entry_4 = Entry(
            new_item_window,
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        entry_4.place(
            x=36.5,
            y=121.0,
            width=252.0,
            height=21.0
        )

        item_canvas.create_text(
            143.0,
            103.0,
            anchor="nw",
            text="author",
            fill="#000000",
            font=("Jomolhari Regular", 12 * -1)
        )

        new_item_window.button_image_1_1 = PhotoImage(
            file=relative_to_assets("button_1_1.png"))
        button_1_1 = Button(
            new_item_window,
            image=new_item_window.button_image_1_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1_1 clicked"),
            relief="flat"
        )
        button_1_1.place(
            x=85.0,
            y=274.0,
            width=150.0,
            height=40.0
        )