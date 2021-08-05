import tkinter
import tkinter.font as font
import turtle
import time

root = tkinter.Tk()
root.title("Control panel")
root.option_add('*Font', 'Times')
root.configure(bg="#64C9CF")
used = font.Font(size=15, family="Small Fonts")
entry1 = tkinter.Entry(root, width=40, font=used, bg="#F0F0CB")
entry2 = tkinter.Entry(root, width=40, font=used, bg="#F0F0CB")
entry3 = tkinter.Entry(root, width=40, font=used, bg="#F0F0CB")
entry4 = tkinter.Entry(root, width=40, font=used, bg="#F0F0CB")
entry5 = tkinter.Entry(root, width=40, font=used, bg="#F0F0CB")
total_list = []
move_list = []
num = []


def moves(cmd):
    if cmd[:7] == "forward":
        move_list.append("forward")
        num.append(int(cmd[8:]))
    if cmd[:5] == "right":
        move_list.append("right")
        num.append(int(cmd[6:]))
    if cmd[:4] == "left":
        move_list.append("left")
        num.append(int(cmd[5:]))
    if cmd[:4] == "back":
        move_list.append("back")
        num.append(int(cmd[5:]))
    if cmd[:6] == "circle":
        move_list.append("circle")
        num.append(int(cmd[7:]))


def check(line):
    if line:
        moves(line)


def execute():
    step1 = entry1.get()
    check(step1)
    step2 = entry2.get()
    check(step2)
    step3 = entry3.get()
    check(step3)
    step4 = entry4.get()
    check(step4)
    step5 = entry5.get()
    step5 = int(step5)

    counter = 0
    while counter != step5:
        turtle.title("Y Logo")
        for index, i in enumerate(move_list):
            if i == "right":
                turtle.right(num[index])
            if i == "forward":
                turtle.forward(num[index])
            if i == "left":
                turtle.left(num[index])
            if i == "back":
                turtle.back(num[index])
            if i == "circle":
                turtle.circle(num[index])
        counter += 1
    move_list.clear()
    num.clear()
    entry1.delete(0, tkinter.END)
    entry2.delete(0, tkinter.END)
    entry3.delete(0, tkinter.END)
    entry4.delete(0, tkinter.END)
    entry5.delete(0, tkinter.END)
    turtle.done()




runner = tkinter.Button(root, padx=130, text="execute", bg="#FDE49C", command=execute).grid(row=5, column=0)
entry1.grid(row=0, column=0, pady=10, padx=10)
entry2.grid(row=1, column=0, pady=10, padx=10)
entry3.grid(row=2, column=0, pady=10, padx=10)
entry4.grid(row=3, column=0, pady=10, padx=10)
entry5.grid(row=4, column=0, pady=10, padx=10)

root.mainloop()
