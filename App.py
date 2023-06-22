import tkinter
from tkinter import *

root = Tk()
root.title("To-Do-List")
root.geometry("400x650+400+100")
root.resizable(False, False)
task_list = []

def addTask():
    task = entry.get()
    entry.delete(0, END)

    if task:
        with open('tasklist.txt','a') as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        listbox.insert(END, task)


def deleteTask():
    global task_list
    task = str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("tasklist.txt", 'w') as taskfie:
            for task in task_list:
                taskfie.write(task+"\n")
        listbox.delete(ANCHOR)
def openTaskfile():
    try:
        global task_list
        with open('tasklist.txt','r') as taskfile:
            tasks = taskfile.readlines()
        for task in tasks:
            if task !='\n':
                task_list.append(task)
                listbox.insert(END, task)
    except:
        file=open('tasklist.txt' , 'w')
        file.close()


# icon
Image_icon = PhotoImage(file="icon.png")
root.iconphoto(False, Image_icon)

# Top Bar
topImage = PhotoImage(file="topbar.png")
Label(root, image=topImage).pack()

#Dock image
dock = PhotoImage(file="dock.png")
Label(root, image=dock, bg="#32405b").place(x=30, y=25)

noteImage = PhotoImage(file="task.png")
Label(root, image=noteImage, bg="#32405b", width=30, height=30).place(x=340, y=25)

heading = Label(root, text="OUR TASK", font="arial 20 bold", fg="white", bg="#32405b")
heading.place(x=130, y=20)

#main
frame = Frame(root, width=400, height=50, bg="white")
frame.place(x=0, y=180)
task = StringVar()
entry = Entry(frame, width=18, font="arial 20", bd=0)
entry.place(x=10, y=7)
entry.focus()

button = Button(frame, text="ADD", font="arial 20 bold", width=6, bg="#5a95ff", fg="#fff",bd=0, command=addTask)
button.place(x=300, y=0)

#list
frame1 = Frame(root, bd=3, width=700, height=280, bg="#32405b")
frame1.pack(pady=(160, 0))

listbox = Listbox(frame1, font=('arial', 12), width=40, height=16, bg="#32405b", fg="white", cursor="hand2", selectbackground="#5a95ff")
listbox.pack(side=LEFT, fill=BOTH, padx=2)
scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT, fill=BOTH)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview())

openTaskfile()

#delete icon
delete = PhotoImage(file="delete.png")
Button(root, image=delete, bd=0, command=deleteTask).pack(side=BOTTOM,pady=13)

root.mainloop()