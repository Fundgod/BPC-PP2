# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, messagebox
from tkinter import ttk
from .new_window import PopUpWindow
from .variables import *
from .data_base_connection import DBSample


class MainWindow():
    def search_button(self):
        db_search = DBSample()
        data = db_search.select_from_entry(self.entry.get())

        self.table.delete(*self.table.get_children())

        for row_data in data:
            self.table.insert(parent="", index="end", values=row_data)
        

    def create_new_item_window(self):
            self.new_window = PopUpWindow(self.window, self.update_treeview)
    
    def sort_treeview_column(self, tv, col, reverse):
            # Function to determine the key for sorting based on column index
        def get_sort_key(item):
            value, child = item
            if col == 'ID' or col == 'Year':  # Assuming the first and fourth columns
                return int(value)
            elif col == 'Rate':  # Assuming the fifth column
                return float(value)
            else:
                return value

        # Get the values from the column to sort
        data = [(tv.set(child, col), child) for child in tv.get_children("")]

        # Sort the data based on the values and data type
        data.sort(key=get_sort_key, reverse=reverse)

        # Rearrange the items in the Treeview
        for index, (_, child) in enumerate(data):
            tv.move(child, "", index)

        # Reverse the sort order for the next click
        tv.heading(col, command=lambda: self.sort_treeview_column(tv, col, not reverse))

    def update_treeview(self):
        db = DBSample()
        self.table.delete(*self.table.get_children())

        for row_data in db.get_all_lines():
            self.table.insert(parent="", index="end", values=row_data)

    def delete_row(self):
        selected_item = self.table.focus()
        if selected_item:
            # Handle the case when an item is selected
            item_data = self.table.item(selected_item, 'values')
            db_delete = DBSample()
            db_delete.delete_by_id(item_data[0])
            messagebox.showinfo("Success", "Film has been removed")
        else:
            # Handle the case when no item is selected
            messagebox.showinfo("Error", "No film selected")
        self.update_treeview()

    def correct_row(self):
        selected_item = self.table.focus()
        if selected_item:
            # Handle the case when an item is selected
            item_data = self.table.item(selected_item, 'values')
            self.new_window = PopUpWindow(self.window, self.update_treeview, item_data[1], item_data[2], item_data[3], item_data[4], True, item_data[0])
        else:
            # Handle the case when no item is selected
            messagebox.showinfo("Error", "No film selected")

    def __init__(self):
        self.window = Tk()
        self.window.title("F1lmSe4rch")

        self.window.geometry("1000x530")
        self.window.configure(bg = "#D9D9D9")

        self.canvas = Canvas(
            self.window,
            bg = "#D9D9D9",
            height = 550,
            width = 1000,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
        self.canvas.place(x = 0, y = 0)
        self.canvas.create_rectangle(
            0.0,
            0.0,
            1000.0,
            56.0,
            fill="#62AFD0",
            outline="")

        self.entry_image_1 = PhotoImage(
            file=relative_to_assets("entry.png"))
        self.entry_bg_1 = self.canvas.create_image(
            414.0,
            29.0,
            image=self.entry_image_1
        )
        self.entry = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry.place(
            x=30.0,
            y=13.0,
            width=768.0,
            height=30.0
        )

        self.button_add_image = PhotoImage(
            file=relative_to_assets("button_add.png"))
        self.button_add = Button(
            image=self.button_add_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.create_new_item_window,
            relief="flat"
        )
        self.button_add.place(
            x=951.0,
            y=11.0,
            width=34.0,
            height=34.0
        )

        self.button_search_image = PhotoImage(
            file=relative_to_assets("button_search.png"))
        self.button_search = Button(
            image=self.button_search_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.search_button,
            relief="flat"
        )
        self.button_search.place(
            x=909.0,
            y=13.0,
            width=32.0,
            height=32.0
        )

        button_delete_image = PhotoImage(
            file=relative_to_assets("button_delete.png"))
        button_delete = Button(
            image=button_delete_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.delete_row,
            relief="flat"
        )
        button_delete.place(
            x=867.0,
            y=13.0,
            width=32.0,
            height=32.0
        )

        button_edit_image = PhotoImage(
            file=relative_to_assets("button_edit.png"))
        button_edit = Button(
            image=button_edit_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.correct_row,
            relief="flat"
        )
        button_edit.place(
        x=825.0,
        y=13.0,
        width=32.0,
        height=32.0
        )

        self.table = ttk.Treeview(master=self.window, columns=table_columns, show="headings")

        # Define header of table
        for i in range(len(table_columns)):
            column = table_columns[i]
            width = table_columns_sizes[i]
            self.table.heading(column=column, text=column, command=lambda c=column: self.sort_treeview_column(self.table, c, False))
            self.table.column(column=column, width=width)

        self.update_treeview()

        self.style = ttk.Style()
        self.style.theme_use("default")
        self.style.configure("Treeview", background="#917FB3", fieldbackground="#917FB3", foreground="white")
        self.style.configure("Treeview.Heading", background="#917FB3", fieldbackground="#917FB3", foreground="white")
        self.style.map("Treeview", background=[("selected", "#E5BEEC")])

        self.table.place(x=10, y=70, height=450)

        self.window.resizable(False, False)
        print(relative_to_assets("computer.ico"))
        self.window.iconbitmap(relative_to_assets("Alecive-Flatwoken-Apps-Computer-B.ico"))
        self.window.mainloop()
