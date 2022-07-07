from tkinter import *
from tkinter import messagebox as msg
import pandas as pd
import calendar
from datetime import date

win = Tk()
win.resizable(False,False)
win.geometry("1200x585")
win.title("Expenses")
win.config(bg = "black")


a,b,c,d,e,f = [],[],[],[],[],[]

def reset():
    item_entry.delete(0, END)
    type_entry.delete(0, END)
    quantity_entry.delete(0, END)
    price_entry.delete(0, END)
    discount_entry.delete(0, END)
    graph_entry.config(graph.set("None"))
    if list_label.index(0) == False:
        pass
    else:
        list_label.delete(ANCHOR)

def clear():
    list_label.delete(1,END)

def submit():
    global ITEM,TYPE,QUANTITY,PRICE,DISCOUNT,MONTH,a,b,c,d,e,f

    ITEM = item_entry.get()
    TYPE = type_entry.get()
    QUANTITY = quantity_entry.get()
    PRICE = price_entry.get()
    DISCOUNT = discount_entry.get()
    MONTH = calendar.month_name[date.today().month]

    a.append(MONTH)
    b.append(ITEM)
    c.append(TYPE)
    d.append(QUANTITY)
    e.append(PRICE)
    f.append(DISCOUNT)


    if (item_entry.get == "") or (type_entry.get() == "") or (quantity_entry.get() == ""):
        msg.showerror("Error","Please fill the info")
    else:
        try:
            list_label.insert(END,[calendar.month_name[date.today().month],item_entry.get(),type_entry.get(),int(quantity_entry.get()),int(price_entry.get()),int(discount_entry.get())])
        except ValueError:
            msg.showerror("ERROR","quantity, price or discount should be integer values")
    reset()

def main():
    global df,file,file_name

    data = {
        "Month":a,
        "Item":b,
        "Type":c,
        "Quantity":d,
        "Price":e,
        "Discount":f
        }
    df = pd.DataFrame(data = data)

    top_1 = Toplevel()
    top_1.geometry("500x300")
    top_1.resizable(False,False)
    top_1.config(bg = "black")

    def save_file():
        global file_name

        file_name = str(entry.get())
        df.to_csv(f"{file_name}.csv",index = False)

        top_1.destroy()

    frame = Frame(top_1,bd = 0, relief = SUNKEN)
    frame.pack(fill = BOTH,padx = 5)
    label = Label(frame,font = ("Cascadia code",13),text = "File Name", bd = 0, relief = SUNKEN)
    label.pack(fill = BOTH, padx = 5, pady = 5)
    entry = Entry(frame, font = ("Cascadia code",13), bd = 3, relief = GROOVE, width = 30)
    entry.pack(fill = BOTH, padx = 5, pady = 5)

    btn_frame = Frame(top_1, bd = 0, relief = SUNKEN)
    btn_frame.pack(fill = BOTH, padx = 5, pady = 5)
    btn = Button(btn_frame, font = ("Cascadia code",13), text = "Submit", fg = "#ffffff", bg = "#000000", command = save_file)
    btn.pack(fill = BOTH, padx = 5, pady = 5)
    
def edit():
    pass

def create():
    pass


heading_frame = Frame(win, bd = 0, relief = SUNKEN)
heading_frame.pack(fill = BOTH)
heading_label = Label(heading_frame, bd = 0, relief = SUNKEN, text = "Expenses", font = ("Cascadia code",17))
heading_label.pack(fill = BOTH, pady = 5)

main_frame = Frame(win, bd = 0, relief = SUNKEN)
main_frame.pack(fill = BOTH, pady = 5, side = "left")

list_frame = Frame(win, bd = 0, relief = SUNKEN)
list_frame.pack(fill = Y)
list_label = Listbox(list_frame, font = ("Cascadia code",13), relief = SUNKEN, bd = 0, bg = "black", fg = "white", height = 21, width = 75)
list_label.pack(fill = BOTH)
list_label.insert(0,["Month","Item","Type","Quantity","Price","Discount"])

item_label = Label(main_frame, bd = 0, relief = SUNKEN, text = "Item", font = ("Cascadia code",13))
item_label.grid(row = 0, column = 0, pady = 5)
item_entry = Entry(main_frame, bd = 3, relief = GROOVE, width = 30, font = ("Cascadia code",13))
item_entry.grid(row = 0, column = 1, pady = 5, padx = 5)

type_label = Label(main_frame, bd = 0, relief = SUNKEN, text = "Type", font = ("Cascadia code",13))
type_label.grid(row = 1, column = 0, pady = 5)
type_entry = Entry(main_frame, bd = 3, relief = GROOVE, width = 30, font = ("Cascadia code",13))
type_entry.grid(row = 1, column = 1, pady = 5)

quantity_label = Label(main_frame, bd = 0, relief = SUNKEN, text = "Quantity", font = ("Cascadia code",13))
quantity_label.grid(row = 2, column = 0, pady = 5)
quantity_entry = Entry(main_frame, bd = 3, relief = GROOVE, width = 30, font = ("Cascadia code",13))
quantity_entry.grid(row = 2, column = 1, pady = 5)

price_label = Label(main_frame, bd = 0, relief = SUNKEN, text = "Price", font = ("Cascadia code",13))
price_label.grid(row = 3, column = 0, pady = 5)
price_entry = Entry(main_frame, bd = 3, relief = GROOVE, width = 30, font = ("Cascadia code",13))
price_entry.grid(row = 3, column = 1, pady = 5, padx = 5)

discount_label = Label(main_frame, bd = 0, relief = SUNKEN, text = "Discount(%)", font = ("Cascadia code",13))
discount_label.grid(row = 4, column = 0, pady = 5)
discount_entry = Entry(main_frame, bd = 3, relief = GROOVE, width = 30, font = ("Cascadia code",13))
discount_entry.grid(row = 4, column = 1, pady = 5)

cmd_label = Label(main_frame, bd = 0, relief = SUNKEN, font = ("Cascadia code",13), text = "Graphs")
cmd_label.grid(row = 5, column = 0, pady = 5)
graph = StringVar()
graph.set("None")
graphs = ["bargraph","histogram","boxplot"]
graph_entry = OptionMenu(main_frame, graph, *graphs)
graph_entry.grid(row = 5, column = 1, padx = 5, pady = 5)

button_frame = Frame(win, bd = 0, relief = SUNKEN)
button_frame.pack(fill = BOTH,pady = 5)

submit_btn = Button(button_frame, font = ("Cascadia code",13), text = "Submit", fg = "#ffffff", bg = "#000000", command = submit)
submit_btn.grid(row = 0, column = 0, padx = 5, pady = 5)
save_btn = Button(button_frame, font = ("Cascadia code",13), text = "Save", fg = "#ffffff", bg = "#000000", command = main)
save_btn.grid(row = 0, column = 1, padx = 5, pady = 5)
clear_btn = Button(button_frame, font = ("Cascadia code",13), text = "Clear", fg = "#ffffff", bg = "#000000", command = clear)
clear_btn.grid(row = 0, column = 2, padx = 5, pady = 5)
create_btn = Button(button_frame, font = ("Cascadia code",13), text = "Create", fg = "#ffffff", bg = "#000000", command = create)
create_btn.grid(row = 0, column = 3, padx = 5, pady = 5)
reset_btn = Button(button_frame, font = ("Cascadia code",13), text = "Reset", fg = "#ffffff", bg = "#000000", command = reset)
reset_btn.grid(row = 0, column = 4, padx = 5, pady = 5)

win.mainloop()
