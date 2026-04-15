import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("toy_hr_data.csv")

mean_salary = df["salary"].mean()
median_salary = df["salary"].median()

fig, ax = plt.subplots(figsize=(10, 6))

ax.hist(df["salary"], bins=15, color="steelblue", edgecolor="white", alpha=0.85)

ax.axvline(mean_salary, color="red", linewidth=2, label=f"Mean: ${mean_salary:,.0f}")
ax.axvline(median_salary, color="blue", linewidth=2, linestyle="--", label=f"Median: ${median_salary:,.0f}")

ax.text(mean_salary + 1500, 0.95, f"Mean\n${mean_salary:,.0f}", color="red", fontsize=10, va="top", transform=ax.get_xaxis_transform())
ax.text(median_salary + 1500, 0.82, f"Median\n${median_salary:,.0f}", color="blue", fontsize=10, va="top", transform=ax.get_xaxis_transform())

ax.set_xlabel("Salary ($)", fontsize=12)
ax.set_ylabel("Number of Employees", fontsize=12)
ax.set_title("Distribution of Salary", fontsize=14)
ax.legend(fontsize=11)

plt.tight_layout()
plt.savefig("salary_distribution.png", dpi=150)
print(f"Saved salary_distribution.png  |  Mean: ${mean_salary:,.0f}  |  Median: ${median_salary:,.0f}")
