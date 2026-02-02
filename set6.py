import pandas as pd
import numpy as np

# sample patient vitals data
df = pd.DataFrame({
    "patient_id": [1, 1, 1, 2, 2, 3, 3, 4],
    "timestamp": pd.to_datetime([
        "2026-01-01 10:00", "2026-01-01 11:00", "2026-01-01 12:00",
        "2026-01-01 10:00", "2026-01-01 11:00",
        "2026-01-01 10:00", "2026-01-01 11:00",
        "2026-01-01 10:00"
    ]),
    "heart_rate": [72, 75, 120, 68, 70, 80, 82, 140],
    "ward": ["A", "A", "A", "B", "B", "A", "A", "C"]
})

# compute average heart rate per ward
avg_hr_per_ward = df.groupby("ward")["heart_rate"].mean()

# sort data by patient and time (important for spike detection)
df = df.sort_values(["patient_id", "timestamp"])

# calculate change in heart rate for each patient
df["hr_change"] = df.groupby("patient_id")["heart_rate"].diff()

# identify sudden spikes (change greater than 30 bpm)
sudden_spikes = df[df["hr_change"] > 30]

# extract critical cases (very high heart rate)
critical_cases = df[df["heart_rate"] > 120]

# print results
print("Average heart rate per ward:")
print(avg_hr_per_ward)

print("\nPatients with sudden heart rate spikes:")
print(sudden_spikes)

print("\nCritical cases:")
print(critical_cases)
