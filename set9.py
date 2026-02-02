import pandas as pd

# sample student exam data
df = pd.DataFrame({
    "student_id": [1, 1, 1, 2, 2, 3, 3, 4, 4],
    "subject": ["Math", "Science", "English",
                "Math", "Science",
                "Math", "English",
                "Science", "English"],
    "marks": [78, 35, 66, 30, 42, 55, 20, 88, 92],
    "exam_date": pd.to_datetime([
        "2026-01-10", "2026-01-10", "2026-01-10",
        "2026-01-10", "2026-01-10",
        "2026-01-10", "2026-01-10",
        "2026-01-10", "2026-01-10"
    ])
})

pass_mark = 40

# mark each record as pass or fail
df["passed"] = df["marks"] >= pass_mark

# compute subject-wise pass percentage
subject_pass_percentage = (
    df.groupby("subject")["passed"]
      .mean() * 100
)

# count failed subjects per student
failed_count = (
    df[~df["passed"]]
    .groupby("student_id")
    .size()
)

# students failing in more than one subject
students_failing_multiple = failed_count[
    failed_count > 1
].index

# generate performance summary per student
performance_summary = (
    df.groupby("student_id")
      .agg(
          total_subjects=("subject", "count"),
          subjects_passed=("passed", "sum"),
          subjects_failed=("passed", lambda x: (~x).sum()),
          average_marks=("marks", "mean")
      )
)

# print results
print("Subject-wise pass percentage:")
print(subject_pass_percentage)

print("\nStudents failing in more than one subject:")
print(list(students_failing_multiple))

print("\nPerformance summary report:")
print(performance_summary)
