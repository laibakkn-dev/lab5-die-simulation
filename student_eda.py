import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ---- Create dataset: 12 rows, 2 missing Marks, 1 exact duplicate ----
data = {
    "StudentID":     [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 11],
    "Gender":        ["Female", "Male", "Female", "Male", "Female", "Male",
                      "Female", "Male", "Female", "Male", "Female", "Female"],
    "StudyHours":    [6, 4, 8, 3, 5, 7, 2, 6, 7, 5, 4, 4],
    "Attendance(%)": [90, 80, 95, 70, 85, 88, 75, 82, 92, 78, 80, 80],
    "Marks":         [82, 65, 91, 55, np.nan, 78, 50, np.nan, 85, 68, 62, 62],
}
pd.DataFrame(data).to_csv("student_performance.csv", index=False)

# (a) load, shape, info
df = pd.read_csv("student_performance.csv")
print("Shape:", df.shape)
df.info()

# (b) missing + duplicates, then clean
print("Missing values per column:")
print(df.isnull().sum())
print("Duplicate rows:", df.duplicated().sum())

df = df.drop_duplicates()
df["Marks"] = df["Marks"].fillna(df["Marks"].median())
print("After cleaning:", df.shape)

# (c) histogram + boxplot of Marks
plt.figure(figsize=(6, 4))
plt.hist(df["Marks"], bins=6, color="steelblue", edgecolor="black")
plt.xlabel("Marks"); plt.ylabel("Frequency"); plt.title("Marks Distribution")
plt.tight_layout()
plt.savefig("marks_histogram.png")

plt.figure(figsize=(4, 4))
plt.boxplot(df["Marks"])
plt.title("Marks Boxplot")
plt.tight_layout()
plt.savefig("marks_boxplot.png")

# (d) scatter + correlation matrix
plt.figure(figsize=(6, 4))
plt.scatter(df["StudyHours"], df["Marks"], color="darkorange")
plt.xlabel("Study Hours"); plt.ylabel("Marks"); plt.title("StudyHours vs Marks")
plt.tight_layout()
plt.savefig("studyhours_vs_marks.png")

print("Correlation matrix:")
print(df[["StudyHours", "Attendance(%)", "Marks"]].corr())

# (e) groupby Gender
print("Average Marks and Attendance by Gender:")
print(df.groupby("Gender")[["Marks", "Attendance(%)"]].mean())

print("Saved marks_histogram.png, marks_boxplot.png, studyhours_vs_marks.png")