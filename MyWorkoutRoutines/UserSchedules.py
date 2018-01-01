import sqlite3
import DataListBox
try:
    import tkinter
except ImportError:
    import Tkinter as tkinter

conn = sqlite3.connect('E:\\Moses\\prgm\\AndroidProjects\\GymBuddy\\app\src\\main\\assets\\GymWizard.sqlite')


class UserWeeksListBox(DataListBox.DataListBox):

    def __init__(self, window, connection, **kwargs):
        # ScrollBox.__init__(self, window, **kwargs) # Python 2
        super().__init__(window, connection, "tblWeeks", "_id", **kwargs)

        self.user_id = ""
        self.sql_select = "SELECT DISTINCT tblWeeks._id, tblWeeks.Name FROM tblWeeks WHERE tblWeeks._id IN "\
            "(SELECT tblUserSchedules.WeekNumber FROM tblUserSchedules WHERE tblUserSchedules.UserID=?) "\
            "ORDER BY tblWeeks._id"

    def update(self, link_value):
       # print("Why not here?")
        print("sql_select={}".format(self.sql_select))  # TODO delete
        print("link_value={}".format(link_value))   # TODO delete

        self.user_id = link_value
        self.cursor.execute(self.sql_select, (self.user_id,))

        # clear the listbox before reloading
        self.clear()
        for value in self.cursor:
            self.insert(tkinter.END, value[1])
            self.data.append((value[0], value[1]))


def get_user_weeks(event):
    lb = event.widget
    index = lb.curselection()[0]
    user_id = lb.data[index][0]

    print("User ID selected: {}".format(user_id))  # TODO delete

    weeksLB.update(user_id)


class UserDaysListBox(DataListBox.DataListBox):

    def __init__(self, window, connection, **kwargs):
        # ScrollBox.__init__(self, window, **kwargs) # Python 2
        super().__init__(window, connection, "tblDays", "_id", **kwargs)

        self.user_id = ""
        self.week_id = ""
        self.sql_select = "SELECT tblDays._id, tblDays.Name FROM tblDays WHERE tblDays._id IN "\
            "(SELECT tblUserSchedules.DayID FROM tblUserSchedules WHERE "\
            "tblUserSchedules.UserID=? AND tblUserSchedules.WeekNumber=?)"

    def update(self, link_value, user_id):
        self.user_id = user_id
        self.week_id = link_value

        print("sql_select={}".format(self.sql_select))  # TODO delete
        print("week_id={}".format(link_value))   # TODO delete
        print("user_id={}".format(user_id))     # TODO delete

        self.cursor.execute(self.sql_select, (self.user_id, self.week_id))

        # clear the listbox before reloading
        self.clear()
        for value in self.cursor:
            self.insert(tkinter.END, value[1])
            self.data.append((value[0], value[1]))


def get_user_days(event):
    lb = event.widget
    index = lb.curselection()[0]
    week_id = lb.data[index][0]

    print("Week ID selected: {}".format(week_id))  # TODO delete

    daysLB.update(week_id, lb.user_id)


class UserSchedulePlansListBox(DataListBox.DataListBox):

    def __init__(self, window, connection, **kwargs):
        # ScrollBox.__init__(self, window, **kwargs) # Python 2
        super().__init__(window, connection, "tblUserSchedules", "_id", **kwargs)

        self.user_id = ""
        self.week_id = ""
        self.day_id = ""
        self.sql_select = "SELECT tblPlans._id, tblPlans.Name FROM tblPlans WHERE tblPlans._id IN "\
            "(SELECT tblUserWorkoutPlans.PlanID FROM tblUserWorkoutPlans WHERE tblUserWorkoutPlans.PlanID IN "\
            "(SELECT tblUserSchedules.WorkoutPlanID FROM tblUserSchedules WHERE "\
            "tblUserSchedules.UserID=? AND tblUserSchedules.WeekNumber=? AND tblUserSchedules.DayID=?))"

    def update(self, link_value, user_id, week_id):
        self.user_id = user_id
        self.week_id = week_id
        self.day_id = link_value

        print("sql_select={}".format(self.sql_select))  # TODO delete
        print("day_id={}".format(link_value))   # TODO delete
        print("user_id={}".format(user_id))     # TODO delete
        print("week_id={}".format(week_id))     # TODO delete

        self.user_id = user_id
        self.week_id = week_id
        self.day_id = link_value
        self.cursor.execute(self.sql_select, (self.user_id, self.week_id, self.day_id))

        # clear the listbox before reloading
        self.clear()
        for value in self.cursor:
            self.insert(tkinter.END, value[1])
            self.data.append((value[0], value[1]))


def get_user_schedule_plans(event):
    lb = event.widget
    index = lb.curselection()[0]
    day_id = lb.data[index][0]

    print("Day ID selected: {}".format(day_id))  # TODO delete

    workout_plansLB.update(day_id, lb.user_id, lb.week_id)


class UserExercisesByPlansListBox(DataListBox.DataListBox):

    def __init__(self, window, connection, **kwargs):
        # ScrollBox.__init__(self, window, **kwargs) # Python 2
        super().__init__(window, connection, "tblUserSchedules", "_id", **kwargs)

        self.user_id = ""
        self.week_id = ""
        self.day_id = ""
        self.sql_select = "SELECT tblExercises._id, tblExercises.Name FROM tblExercises " \
                          "WHERE tblExercises._id IN " \
                          "(SELECT tblUserWorkoutPlans.ExerciseID FROM tblUserWorkoutPlans "\
                          "WHERE tblUserWorkoutPlans.PlanID IN "\
                          "(SELECT tblUserSchedules.WorkoutPlanID FROM tblUserSchedules "\
                          "WHERE tblUserSchedules.WorkoutPlanID=? AND " \
                          "tblUserSchedules.WeekNumber=? AND tblUserSchedules.UserID=?) "\
                          "AND tblUserWorkoutPlans.UserID=?) " \
                          "ORDER BY CategoryID"

    def update(self, link_value, user_id, week_id):
        self.user_id = user_id
        self.week_id = week_id
        self.day_id = link_value

        print("sql_select={}".format(self.sql_select))  # TODO delete
        print("plan_id={}".format(link_value))   # TODO delete
        print("user_id={}".format(user_id))     # TODO delete
        print("week_id={}".format(week_id))     # TODO delete

        self.user_id = user_id
        self.week_id = week_id
        self.plan_id = link_value
        self.cursor.execute(self.sql_select, (self.plan_id, self.week_id, self.user_id, self.user_id))

        # clear the listbox before reloading
        self.clear()
        for value in self.cursor:
            self.insert(tkinter.END, value[1])
            self.data.append((value[0], value[1]))


def get_user_exercise_by_plan(event):
    lb = event.widget
    index = lb.curselection()[0]
    day_id = lb.data[index][0]

    print("Day ID selected: {}".format(day_id))  # TODO delete

    workout_exercisesLB.update(day_id, lb.user_id, lb.week_id)


mainWindow = tkinter.Tk()
mainWindow.title('My Workout Schedules Browser')
mainWindow.geometry('1600x900')

mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=4)
mainWindow.columnconfigure(2, weight=4)
mainWindow.columnconfigure(3, weight=4)
mainWindow.columnconfigure(4, weight=4)
mainWindow.columnconfigure(5, weight=1)

mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=5)
mainWindow.rowconfigure(2, weight=1)

# ===- Labels ====
tkinter.Label(mainWindow, text="Users").grid(row=0, column=0)
tkinter.Label(mainWindow, text="Week").grid(row=0, column=1)
tkinter.Label(mainWindow, text="Day").grid(row=0, column=2)
tkinter.Label(mainWindow, text="Plan").grid(row=0, column=3)
tkinter.Label(mainWindow, text="Exercises").grid(row=0, column=4)

# ==== Users Listbox ====
usersLB = DataListBox.DataListBox(mainWindow, conn, "tblUsers", "Username")
usersLB.grid(row=1, column=0, sticky='nsew', padx=(30, 0))
usersLB.config(border=2, relief='sunken')
usersLB.update()
usersLB.bind("<<ListboxSelect>>", get_user_weeks)

# ==== Weeks Listbox ====
weeksLB = UserWeeksListBox(mainWindow, conn)
weeksLB.grid(row=1, column=1, sticky='nsew', padx=(30, 0))
weeksLB.config(border=2, relief='sunken')
weeksLB.bind("<<ListboxSelect>>", get_user_days)

# ==== Days Listbox ====
daysLB = UserDaysListBox(mainWindow, conn)
daysLB.grid(row=1, column=2, sticky='nsew', padx=(30, 0))
daysLB.config(border=2, relief='sunken')
daysLB.bind("<<ListboxSelect>>", get_user_schedule_plans)

# ==== Plans Listbox ====
workout_plansLB = UserSchedulePlansListBox(mainWindow, conn)
workout_plansLB.grid(row=1, column=3, sticky='nsew', padx=(30, 0))
workout_plansLB.config(border=2, relief='sunken')
workout_plansLB.bind("<<ListboxSelect>>", get_user_exercise_by_plan)

# ==== Exercises Listbox ====
workout_exercisesLB = UserExercisesByPlansListBox(mainWindow, conn)
workout_exercisesLB.grid(row=1, column=4, sticky='nsew', padx=(30, 0))
workout_exercisesLB.config(border=2, relief='sunken')


# ==== Main Loop ====
mainWindow.mainloop()

conn.close()