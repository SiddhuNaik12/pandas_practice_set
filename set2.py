import pandas as pd
#read csv
df=pd.read_csv("set2_data.csv")
#Quarter wise average performance per department
avg_perf=(
    df.groupby(['department','quarter'])['performance_score']
    .mean().reset_index()
)
#sort for correct quarter order
avg_perf = avg_perf.sort_values(["department", 'quarter'])
#calculate quarter to quarter change
avg_perf["change"] = (
    avg_perf.groupby("department")['performance_score'].diff()
)
#indentify consistently improving departments
improving_departments = (
    avg_perf.groupby("department")["change"].apply(lambda x: (x.dropna()>0).all())
)
improving_departments = improving_departments[improving_departments].index.tolist()
print("Quarter wise average performance:")
print(avg_perf)
print("department with consistent improvement:")
print(improving_departments)