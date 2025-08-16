import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

grades_above_50 = []
age_above_25 = []
max_grade_names = []
min_grade_names = []
data = []
students = []

try:
    with open("student_data/data/data.json", "r", encoding="utf-8") as f:
        students = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    students = []

entry_made = False
decision = input("Do you want to enter student data? (Y/N) ")
while decision == 'Y':
    entry_made = True
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    try:
        age = int(input("Enter age: "))
    except ValueError:
        print("Invalid age. Please try again.")
        continue
    city = input("Enter city: ")
    try:
        grade = int(input("Enter grade: "))
    except ValueError:
        print("Invalid grade. Please try again.")
        continue
    record = {"ad": first_name, "soyad": last_name, "yas": age, "sehir": city, "not": grade}
    students.append(record)
    decision = input("Do you want to enter student data? (Y/N) ")

if entry_made:
    with open("student_data/data/data.json", "w", encoding="utf-8") as f: 
        json.dump(students, f, ensure_ascii=False, indent=4)

df = pd.read_json("student_data/data/data.json")
summary = df.describe()
all_grades = []
all_ages = []

for student in students:
    all_grades.append(student["not"])
    all_ages.append(student["yas"])
    if student["not"] > 50:
        grades_above_50.append(student["ad"])
    if student["yas"] > 25:
        age_above_25.append(student["ad"])
    if student["not"] == summary.loc["max", "not"]:
        max_grade_names.append(student["ad"])
    if student["not"] == summary.loc["min", "not"]:
        min_grade_names.append(student["ad"])

results = {
    "Category": [
        "Students with grade above 50",
        "Students older than 25",
        "Average grade",
        "Highest grade",
        "Lowest grade"
    ],
    "Value": [
        ', '.join(grades_above_50),
        ', '.join(age_above_25),
        summary.loc['mean','not'],
        f"{summary.loc['max','not']} -> {max_grade_names}",
        f"{summary.loc['min','not']} -> {min_grade_names}"
    ]
}

df_results = pd.DataFrame(results)
df_results.to_csv("student_data/results.csv", index=False, encoding="utf-8")

decision = input("Do you want to see summary graphs? (Y/N) ").upper()
while decision == 'Y':
    try:
        graph_no = int(input("""Choose the graph to display:
                              1- Grade distribution
                              2- Age vs Grade
                              3- Grade distribution with mean\n"""))
        if graph_no == 1:
            plt.hist(all_grades, bins=5)
            plt.title("Grade Distribution")
            plt.xlabel("Grade ranges")
            plt.ylabel("Number of students")
            plt.show()
        elif graph_no == 2:
            df_plot = pd.DataFrame({"Age": all_ages, "Grade": all_grades})
            sns.scatterplot(x="Age", y="Grade", data=df_plot, alpha=0.7)
            plt.title("Age vs Grade")
            plt.show()
        elif graph_no == 3:
            mean_grade = df["not"].mean()
            plt.figure()
            plt.hist(all_grades, bins=5, alpha=0.7, edgecolor="black")
            plt.axvline(mean_grade, linestyle="--", color="red", linewidth=2, label=f"Mean: {mean_grade:.2f}")
            plt.title("Grade Distribution with Mean")
            plt.xlabel("Grade")
            plt.ylabel("Number of students")
            plt.legend()
            plt.tight_layout()
            plt.show()
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
    except ValueError:
        print("Invalid input. Please enter a number (1, 2, or 3).")
    
    decision = input("Do you want to see another summary graph? (Y/N) ").upper()
