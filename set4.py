import pandas as pd
# create sample student activity data
df = pd.DataFrame({
    "student_id": [1, 1, 2, 3, 4, 5, 2, 3],
    "course_id": ["C1", "C2", "C1", "C3", "C2", "C3", "C2", "C1"],
    "login_date": pd.to_datetime([
        "2026-01-20", "2026-01-10", "2026-01-05", "2026-01-18",
        "2026-01-01", "2026-01-22", "2026-01-03", "2026-01-15"
    ]),
    "minutes_spent": [30, 45, 20, 60, 15, 90, 25, 40]
})
# find the most recent login date
latest_login = df["login_date"].max()
# find each student’s last login date
last_login_per_student = df.groupby("student_id")["login_date"].max()
# students who did not login in the last 7 days
inactive_students = last_login_per_student[
    last_login_per_student < latest_login - pd.Timedelta(days=7)
].index
# calculate average session duration per course
avg_session_per_course = df.groupby("course_id")["minutes_spent"].mean()
# calculate total engagement per course
total_engagement = df.groupby("course_id")["minutes_spent"].sum()
# pick top 3 courses with highest engagement
top_3_courses = total_engagement.sort_values(ascending=False).head(3)
# print results
print("Inactive students:", list(inactive_students))
print("Average session per course:")
print(avg_session_per_course)
print("Top 3 courses by engagement:")
print(top_3_courses)
