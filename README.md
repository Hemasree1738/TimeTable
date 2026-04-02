# 📚 Smart Study Time Allocator (Python)

## 📖 Description

This is a simple **console-based Study Time Allocator** built using Python.
The program helps students distribute their available study hours across subjects based on their difficulty levels.

Instead of studying randomly, this tool ensures that **harder subjects get more time** and easier ones get less—making your study plan smarter and more efficient.

---

## 🎯 How It Works

1. User enters the number of subjects.
2. Inputs the name of each subject.
3. Assigns a difficulty level (1 to 3):

   * 1 → Easy
   * 2 → Medium
   * 3 → Hard
4. The program:

   * Stores subject-difficulty mapping
   * Sorts subjects by difficulty
   * Calculates total difficulty weight
5. Based on available study hours, time is distributed proportionally.

---

## 🧠 Features

* Dynamic subject input
* Difficulty-based prioritization
* Automatic time allocation
* Sorting subjects by importance
* Beginner-friendly logic

---

## 🛠️ Technologies Used

* Python
* Lists & Dictionaries
* Loops (`while`)
* Lambda functions
* Basic arithmetic calculations

---

## ▶️ How to Run the Project

1. Make sure Python is installed
2. Save the file as `study_allocator.py`
3. Open terminal or command prompt
4. Run the program:

```bash id="x91f2a"
python study_allocator.py
```

---

## 📌 Example Usage

```id="k29d8s"
enter the number of subjects that you want to target : 3

enter the name of subject 1 : Math
enter the name of subject 2 : Physics
enter the name of subject 3 : English

please enter the difficulty-level of each subject
1 to 3 (3->hard and 1->easy)

enter the difficulty level of each subject1 : 3
enter the difficulty level of each subject2 : 2
enter the difficulty level of each subject3 : 1

enter the number of hours you want to study : 6
```

### 🧮 Output:

```id="r4m8pz"
time allocated for Math = 3.00 hours
time allocated for Physics = 2.00 hours
time allocated for English = 1.00 hours
```

---

## 🚀 Future Improvements

* Add input validation (only allow 1–3 difficulty)
* Handle invalid inputs gracefully
* Convert to GUI using Tkinter
* Save study plans to a file (CSV/JSON)
* Add daily/weekly planner mode

---

## 🙌 Contribution

Feel free to:

* Improve the logic
* Add new features
* Optimize the code structure

Pull requests are welcome!

---

## 👩‍💻 Author

**Hemasree**
B.Tech Computer Science Student

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and make your study time smarter!
