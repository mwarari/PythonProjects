import sqlite3
import DataListBox
try:
    import tkinter
except ImportError:
    import Tkinter as tkinter

conn = sqlite3.connect('E:\\Moses\\prgm\\AndroidProjects\\GymBuddy\\app\src\\main\\assets\\GymWizard.sqlite')

def get_exercises(event):
    lb = event.widget
    index = lb.curselection()[0]
    category_id = lb.data[index][0]

    print("Category ID selected: {}".format(category_id))

    exercisesLB.update("CategoryID", category_id)
    # exercises = []
    # for row in conn.execute("SELECT tblExercises.Name from tblExercises WHERE tblExercises.CategoryID = ?"
    #                         "ORDER BY tblExercises.Name", category_id):
    #     exercises.append(row[0])
    # exercisesLV.set(tuple(exercises))


mainWindow = tkinter.Tk()
mainWindow.title('My Workout Routines Exercises Browser')
mainWindow.geometry('1024x768')

mainWindow.columnconfigure(0, weight=2)
mainWindow.columnconfigure(1, weight=4)
mainWindow.columnconfigure(2, weight=1)

mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=5)
mainWindow.rowconfigure(2, weight=1)

# ===- Labels ====
tkinter.Label(mainWindow, text="Categories").grid(row=0, column=0)
tkinter.Label(mainWindow, text="Exercises").grid(row=0, column=1)

# ==== Categories Listbox ====
categoriesLB = DataListBox.DataListBox(mainWindow, conn, "tblCategories", "Name")
categoriesLB.grid(row=1, column=0, sticky='nsew', padx=(30, 0))
categoriesLB.config(border=2, relief='sunken')
categoriesLB.update()
categoriesLB.bind("<<ListboxSelect>>", get_exercises)

# ==== Exercises Listbox ====
exercisesLV = tkinter.Variable(mainWindow)
exercisesLV.set(("Choose a category",))
exercisesLB = DataListBox.DataListBox(mainWindow, conn, "tblExercises", "Name", sort_order=("Name",))
exercisesLB.grid(row=1, column=1, sticky='nsew', padx=(30, 0))
exercisesLB.config(border=2, relief='sunken')


# ==== Main Loop ====
mainWindow.mainloop()

conn.close()


