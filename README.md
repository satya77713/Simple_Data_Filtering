# 📊 Simple Data Filtering Using Pandas

## 📌 Project Overview

**Simple Data Filtering Using Pandas** is a beginner-friendly Python project that demonstrates how to filter student records using the Pandas library.

The project stores student information in a Pandas DataFrame and filters records based on marks, age, and department.

This project was developed as part of my internship learning journey at **Veda Technology**.

## 🎯 Objectives

- Store student information in a Pandas DataFrame.
- Filter students who score 85 or above.
- Identify students who score 60 or below.
- Filter students aged 20 or above.
- Select students from the ECE department.
- Understand conditional filtering using Pandas.

## 🛠️ Technologies Used

- Python
- Pandas
- Google Colab / Jupyter Notebook
- GitHub

## 📂 Project Structure

```text
Simple-Data-Filtering/
├── Simple_Data_Filtering.ipynb
└── README.md
```

## 📋 Sample Dataset

The notebook contains the following sample student records:

| Name | Age | Department | Marks |
|---|---:|---|---:|
| Rahul | 20 | CSE | 85 |
| Priya | 21 | ECE | 92 |
| Arjun | 19 | CSE | 76 |
| Sneha | 22 | IT | 88 |
| Vikram | 20 | ECE | 55 |
| Ananya | 21 | CSE | 95 |

*Note: These records are created for educational purposes.*

## ✨ Project Features

### 1. Display All Student Records

Creates a Pandas DataFrame from the student dataset and displays all records.

```python
df = pd.DataFrame(data)
print(df)
```

### 2. Filter Students Scoring 85 or Above

Selects students whose marks are greater than or equal to 85.

```python
high_scorers = df[df["Marks"] >= 85]
print(high_scorers)
```

**Expected students:** Rahul, Priya, Sneha, and Ananya.

### 3. Filter Students Scoring 60 or Below

Selects students whose marks are less than or equal to 60.

```python
lowest_score = df[df["Marks"] <= 60]
print(lowest_score)
```

**Expected student:** Vikram.

### 4. Filter Students Aged 20 or Above

Selects students whose age is greater than or equal to 20.

```python
age = df[df["Age"] >= 20]
print(age)
```

**Expected students:** Rahul, Priya, Sneha, Vikram, and Ananya.

### 5. Filter Students from the ECE Department

Selects students whose department is ECE.

```python
course = df[df["Department"] == "ECE"]
print(course)
```

**Expected students:** Priya and Vikram.

## ▶️ How to Run the Project

1. Clone or download this repository.
2. Open `Simple_Data_Filtering.ipynb` in Google Colab or Jupyter Notebook.
3. Ensure Python and Pandas are available.
4. Run the notebook cells in order.
5. Review the filtered student records displayed in the output.

You can use [Google Colab](https://colab.research.google.com/) to run the notebook online.

## 📚 Learning Outcomes

Through this project, I learned how to:

- Create a Pandas DataFrame.
- Store structured student information.
- Access DataFrame columns.
- Filter rows using comparison operators.
- Apply conditions such as `>=`, `<=`, and `==`.
- Display filtered records for basic data analysis.

## 🔮 Future Improvements

- Load student records from a CSV file.
- Add filtering by multiple conditions.
- Sort students by marks or age.
- Calculate average and highest marks.
- Visualize student performance using charts.

## 👨‍💻 Author

**Satya**

GitHub: https://github.com/satya77713

---

*Created as part of my Python internship learning journey at Veda Technology.*
