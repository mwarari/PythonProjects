import sqlite3
import DataListBox
try:
    import tkinter
except ImportError:
    import Tkinter as tkinter

conn = sqlite3.connect('E:\\Moses\\prgm\\AndroidProjects\\GymBuddy\\app\src\\main\\assets\\GymWizard.sqlite')


class UserPlansListBox(DataListBox.DataListBox):

    def __init__(self, window, connection, **kwargs):
        # ScrollBox.__init__(self, window, **kwargs) # Python 2
        super().__init__(window, connection, "tblUserWorkoutPlans", "UserID", **kwargs)

        self.user_id = ""
        self.sql_select = "Select tblPlans._id, tblPlans.Name FROM tblPlans WHERE tblPlans._id in "\
            "(SELECT Distinct tblUserWorkoutPlans.PlanID from tblUserWorkoutPlans WHERE tblUserWorkoutPlans.UserID=?) "\
            "ORDER BY tblPlans.Name"

    def update(self, link_value):
        print("sql_select={}".format(self.sql_select))  # TODO delete
        print("link_value={}".format(link_value))   # TODO delete

        self.user_id = link_value
        self.cursor.execute(self.sql_select, (self.user_id,))

        # clear the listbox before reloading
        self.clear()
        for value in self.cursor:
            self.insert(tkinter.END, value[1])
            self.data.append((value[0], value[1]))


def get_user_plans(event):
    lb = event.widget
    index = lb.curselection()[0]
    user_id = lb.data[index][0]

    print("User ID selected: {}".format(user_id))  # TODO delete

    plansLB.update(user_id)


class UserCategoryPlansListBox(DataListBox.DataListBox):

    def __init__(self, window, connection, **kwargs):
        # ScrollBox.__init__(self, window, **kwargs) # Python 2
        super().__init__(window, connection, "tblUserWorkoutPlans", "UserID", **kwargs)

        self.user_id = ""
        self.plan_id = ""
        self.sql_select = "SELECT tblCategories._id, tblCategories.Name FROM tblCategories WHERE tblCategories._id IN "\
            "(SELECT tblUserWorkoutPlans.CategoryID FROM tblUserWorkoutPlans WHERE tblUserWorkoutPlans.UserID = ? "\
            "AND tblUserWorkoutPlans.PlanID = ?) ORDER BY tblCategories.Name"

    def update(self, link_value, user_id):
        print("sql_select={}".format(self.sql_select))  # TODO delete
        print("link_value={}".format(link_value))   # TODO delete
        print("user_id={}".format(user_id))    # TODO delete

        self.user_id = user_id
        self.plan_id = link_value
        self.cursor.execute(self.sql_select, (user_id, link_value))

        # clear the listbox before reloading
        self.clear()
        for value in self.cursor:
            self.insert(tkinter.END, value[1])
            self.data.append((value[0], value[1]))

def get_user_categories(event):
    lb = event.widget
    index = lb.curselection()[0]
    plan_id = lb.data[index][0]

    print("Plan ID selected: {}".format(plan_id))   # TODO delete

    categoriesLB.update(plan_id, lb.user_id)


class UserExercisesByCategoryListBox(DataListBox.DataListBox):

    def __init__(self, window, connection, **kwargs):
        # ScrollBox.__init__(self, window, **kwargs) # Python 2
        super().__init__(window, connection, "tblUserWorkoutPlans", "UserID", **kwargs)

        self.user_id = ""
        self.plan_id = ""
        self.category_id = ""
        self.sql_select = "SELECT tblExercises._id, tblExercises.Name FROM tblExercises WHERE tblExercises._id IN "\
            "(SELECT tblUserWorkoutPlans.ExerciseID FROM tblUserWorkoutPlans WHERE tblUserWorkoutPlans.UserID=? "\
            "AND tblUserWorkoutPlans.PlanID=? and tblUserWorkoutPlans.CategoryID=?)"

    def update(self, link_value, user_id, plan_id):
        print("sql_select={}".format(self.sql_select))  # TODO delete
        print("link_value={}".format(link_value))   # TODO delete
        print("user_id={}".format(user_id))    # TODO delete
        print("plan_id={}".format(plan_id))  # TODO delete
        print("category_id={}".format(link_value))  # TODO delete

        self.user_id = user_id
        self.plan_id = plan_id
        self.category_id = link_value
        self.cursor.execute(self.sql_select, (user_id, plan_id, link_value))

        # clear the listbox before reloading
        self.clear()
        for value in self.cursor:
            self.insert(tkinter.END, value[1])
            self.data.append((value[0], value[1]))


def get_user_exercises_by_category(event):
    lb = event.widget
    index = lb.curselection()[0]
    category_id = lb.data[index][0]

    print("Category ID selected: {}".format(category_id))   # TODO delete

    exercisesLB.update(category_id, lb.user_id, lb.plan_id)


class UserSetsByExerciseListBox(DataListBox.DataListBox):

    def __init__(self, window, connection, **kwargs):
        # ScrollBox.__init__(self, window, **kwargs) # Python 2
        super().__init__(window, connection, "tblUserWorkoutPlans", "UserID", **kwargs)

        self.user_id = ""
        self.plan_id = ""
        self.category_id = ""
        self.exercise_id = ""
        self.sql_select = "SELECT tblSets._id, tblSets.Name FROM tblSets WHERE tblSets.SetID IN "\
            "(SELECT tblUserWorkoutPlans.SetID FROM tblUserWorkoutPlans WHERE tblUserWorkoutPlans.UserID=? "\
            "AND tblUserWorkoutPlans.PlanID=? AND tblUserWorkoutPlans.CategoryID=? AND "\
            "tblUserWorkoutPlans.ExerciseID=?)"

    def update(self, link_value, user_id, plan_id, category_id):
        print("sql_select={}".format(self.sql_select))  # TODO delete
        print("link_value={}".format(link_value))   # TODO delete
        print("user_id={}".format(user_id))    # TODO delete
        print("plan_id={}".format(plan_id))  # TODO delete
        print("category_id={}".format(category_id))  # TODO delete
        print("exercise_id={}".format(link_value))   # TODO delete

        self.user_id = user_id
        self.plan_id = plan_id
        self.category_id = category_id
        self.exercise_id = link_value
        self.cursor.execute(self.sql_select, (user_id, plan_id, category_id, link_value))

        # clear the listbox before reloading
        self.clear()
        for value in self.cursor:
            self.insert(tkinter.END, value[1])
            self.data.append((value[0], value[1]))


def get_user_sets_by_exercise(event):
    lb = event.widget
    index = lb.curselection()[0]
    exercise_id = lb.data[index][0]

    print("Exercise ID selected: {}".format(exercise_id))   # TODO delete

    setsLB.update(exercise_id, lb.user_id, lb.plan_id, lb.category_id)


mainWindow = tkinter.Tk()
mainWindow.title('My Workout Routines Workout Plan Browser')
mainWindow.geometry('1024x768')

mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=4)
mainWindow.columnconfigure(2, weight=4)
mainWindow.columnconfigure(3, weight=4)
mainWindow.columnconfigure(4, weight=2)
mainWindow.columnconfigure(5, weight=1)

mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=5)
mainWindow.rowconfigure(2, weight=1)

# ===- Labels ====
tkinter.Label(mainWindow, text="Users").grid(row=0, column=0)
tkinter.Label(mainWindow, text="Plans").grid(row=0, column=1)
tkinter.Label(mainWindow, text="Categories").grid(row=0, column=2)
tkinter.Label(mainWindow, text="Exercises").grid(row=0, column=3)
tkinter.Label(mainWindow, text="Sets").grid(row=0, column=4)

# ==== Users Listbox ====
usersLB = DataListBox.DataListBox(mainWindow, conn, "tblUsers", "Username")
usersLB.grid(row=1, column=0, sticky='nsew', padx=(30, 0))
usersLB.config(border=2, relief='sunken')
usersLB.update()
usersLB.bind("<<ListboxSelect>>", get_user_plans)

# ==== Plans Listbox ====
plansLB = UserPlansListBox(mainWindow, conn)
plansLB.grid(row=1, column=1, sticky='nsew', padx=(30, 0))
plansLB.config(border=2, relief='sunken')
plansLB.bind("<<ListboxSelect>>", get_user_categories)

# ==== Categories Listbox ====
categoriesLB = UserCategoryPlansListBox(mainWindow, conn)
categoriesLB.grid(row=1, column=2, sticky='nsew', padx=(30, 0))
categoriesLB.config(border=2, relief='sunken')
categoriesLB.bind("<<ListboxSelect>>", get_user_exercises_by_category)

# ==== Exercises Listbox ====
exercisesLB = UserExercisesByCategoryListBox(mainWindow, conn)
exercisesLB.grid(row=1, column=3, sticky='nsew', padx=(30, 0))
exercisesLB.config(border=2, relief='sunken')
exercisesLB.bind("<<ListboxSelect>>", get_user_sets_by_exercise)

# ==== Sets Listbox ====
setsLB = UserSetsByExerciseListBox(mainWindow, conn)
setsLB.grid(row=1, column=4, sticky='nsew', padx=(30, 0))
setsLB.config(border=2, relief='sunken')


# ==== Main Loop ====
mainWindow.mainloop()

conn.close()
