
SELECT tblExercises._id, tblExercises.Name FROM tblExercises WHERE tblExercises._id IN
(SELECT tblUserWorkoutPlans.ExerciseID FROM tblUserWorkoutPlans, tblUserSchedules WHERE tblUserWorkoutPlans.PlanID=1 AND tblUserWorkoutPlans.UserID=1 AND tblUserSchedules.WeekNumber=3 AND tblUserSchedules.DayID=1 AND tblUserSchedules.UserID=1)

SELECT tblUserSchedules.WorkoutPlanID FROM tblUserSchedules WHERE tblUserSchedules.DayID=1 AND tblUserSchedules.WeekNumber=1 AND tblUserSchedules.UserID=1

SELECT tblUserWorkoutPlans.ExerciseID, tblUserWorkoutPlans.CategoryID, tblUserWorkoutPlans.PlanID FROM tblUserWorkoutPlans WHERE tblUserWorkoutPlans.PlanID IN
(SELECT tblUserSchedules.WorkoutPlanID FROM tblUserSchedules WHERE tblUserSchedules.DayID=1 AND tblUserSchedules.WeekNumber=1 AND tblUserSchedules.UserID=1) AND tblUserWorkoutPlans.UserID=1 ORDER BY CategoryID

SELECT DISTINCT tblUserWorkoutPlans.CategoryID FROM tblUserWorkoutPlans WHERE tblUserWorkoutPlans.PlanID IN
(SELECT tblUserSchedules.WorkoutPlanID FROM tblUserSchedules WHERE tblUserSchedules.DayID=1 AND tblUserSchedules.WeekNumber=1 AND tblUserSchedules.UserID=1) AND tblUserWorkoutPlans.UserID=1 ORDER BY CategoryID

SELECT tblUserWorkoutPlans.ExerciseID, tblUserWorkoutPlans.CategoryID FROM tblUserWorkoutPlans WHERE tblUserWorkoutPlans.PlanID IN
(SELECT tblUserSchedules.WorkoutPlanID FROM tblUserSchedules WHERE tblUserSchedules.DayID=1 AND tblUserSchedules.WeekNumber=1 AND tblUserSchedules.UserID=1) AND tblUserWorkoutPlans.UserID=1 ORDER BY CategoryID

SELECT tblExercises._id, tblExercises.Name, tblExercises.CategoryID FROM tblExercises WHERE tblExercises._id IN
(SELECT tblUserWorkoutPlans.ExerciseID FROM tblUserWorkoutPlans WHERE tblUserWorkoutPlans.PlanID IN
(SELECT tblUserSchedules.WorkoutPlanID FROM tblUserSchedules WHERE tblUserSchedules.WorkoutPlanD=1 AND tblUserSchedules.WeekNumber=1 AND tblUserSchedules.UserID=1) AND tblUserWorkoutPlans.UserID=1) ORDER BY CategoryID

SELECT tblCategories._id, tblCategories.Name FROM tblCategories WHERE tblCategories._id IN
(SELECT tblExercises.CategoryID FROM tblExercises WHERE tblExercises._id IN
(SELECT tblUserWorkoutPlans.ExerciseID FROM tblUserWorkoutPlans WHERE tblUserWorkoutPlans.PlanID IN
(SELECT tblUserSchedules.WorkoutPlanID FROM tblUserSchedules WHERE tblUserSchedules.DayID=1 AND tblUserSchedules.WeekNumber=1 AND tblUserSchedules.UserID=1) AND tblUserWorkoutPlans.UserID=1) ORDER BY CategoryID)

SELECT * FROM tblUserSchedules




SELECT tblExercises._id, tblExercises.Name FROM tblExercises WHERE tblExercises._id IN
(SELECT tblUserWorkoutPlans.ExerciseID FROM tblUserWorkoutPlans WHERE tblUserWorkoutPlans.PlanID IN
(SELECT tblUserSchedules.WorkoutPlanID FROM tblUserSchedules WHERE tblUserSchedules.DayID=1 AND tblUserSchedules.WeekNumber=4 AND tblUserSchedules.UserID=1) AND tblUserWorkoutPlans.UserID=1) ORDER BY CategoryID