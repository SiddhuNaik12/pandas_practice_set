import pandas as pd
import numpy as np

# sample server performance data
df = pd.DataFrame({
    "timestamp": pd.to_datetime([
        "2026-01-01 10:00", "2026-01-01 10:01", "2026-01-01 10:02",
        "2026-01-01 10:03", "2026-01-01 10:04",
        "2026-01-01 10:00", "2026-01-01 10:01", "2026-01-01 10:02"
    ]),
    "endpoint": ["/login", "/login", "/login", "/search", "/search",
                 "/search", "/search", "/search"],
    "response_time": [200, 250, 900, 300, 320, 850, 780, 400]
})

# compute average response time per endpoint
avg_response_per_endpoint = (
    df.groupby("endpoint")["response_time"]
      .mean()
)

# identify endpoints exceeding SLA threshold
sla_threshold = 500
sla_violations = avg_response_per_endpoint[
    avg_response_per_endpoint > sla_threshold
]

# group data into 5-minute time windows
df = df.set_index("timestamp")

window_avg = (
    df["response_time"]
      .resample("5T")
      .mean()
)

# detect performance degradation
# window average much higher than normal
degradation_threshold = window_avg.mean() + 2 * window_avg.std()
degraded_windows = window_avg[
    window_avg > degradation_threshold
]

# print results
print("Average response time per endpoint:")
print(avg_response_per_endpoint)

print("\nEndpoints exceeding SLA threshold:")
print(sla_violations)

print("\nTime windows with performance degradation:")
print(degraded_windows)
