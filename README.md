# Password_Generator
A simple Python password generator that creates secure custom passwords using random letters, numbers, and symbols. The project allows users to generate either ordered or fully shuffled passwords using Python’s randomization functions and basic list manipulation techniques.

# PyPassword Generator 🔐

PyPassword Generator is a simple yet interactive password generator built using Python. The project allows users to create custom passwords by specifying the number of letters, numbers, and symbols they want in the password. It also provides two password generation modes: ordered passwords and fully shuffled mixed passwords.

The project demonstrates the use of Python fundamentals such as:

* Lists
* Loops
* Conditional statements
* Randomization
* String manipulation
* User input handling

---

# Features

* Generate custom passwords based on user preferences
* Choose the number of:

  * Letters
  * Numbers
  * Symbols
* Two password generation modes:

  * Ordered Password
  * Mixed/Shuffled Password
* Uses Python randomization functions:

  * `random.choice()`
  * `random.sample()`
  * `random.shuffle()`
* Beginner-friendly terminal-based application

---

# How the Program Works

## 1. Character Lists

The program first creates three separate lists:

```python id="x1a2b3"
letters
numbers
symbols
```

These lists contain:

* Uppercase and lowercase alphabets
* Digits from 0–9
* Special symbols

These serve as the source pool for generating passwords.

---

## 2. User Input

The user is asked to enter:

* Number of letters
* Number of numbers
* Number of symbols

Example:

```python id="c4d5e6"
How many letters would you like in your password?
```

This makes the password fully customizable.

---

## 3. Password Mode Selection

The user chooses between:

* `1` → Ordered Password
* `2` → Mixed/Shuffled Password

---

# Ordered Password Mode

In ordered mode:

* Letters appear first
* Numbers appear next
* Symbols appear last

Example:

```python id="f7g8h9"
abc123!@
```

Two different approaches are demonstrated:

### Method 1

Using:

* `random.sample()`
* `.join()`

### Method 2

Using:

* `for` loops
* `random.choice()`
* String concatenation

This section helps beginners understand multiple ways to solve the same problem in Python.

---

# Mixed Password Mode

In mixed mode:

* All characters are shuffled randomly

Example:

```python id="i1j2k3"
a@1B#9x
```

### Process:

1. Characters are added to a list
2. `random.shuffle()` randomizes the order
3. `.join()` converts the list into a final password string

This produces a stronger and less predictable password pattern.

---

# Concepts Used

This project demonstrates:

* Python lists
* Loops (`for`)
* Conditional statements (`if`)
* Functions from the `random` module
* String concatenation
* List manipulation
* User input handling
* Password generation logic

---

# Python Functions Used

| Function           | Purpose                              |
| ------------------ | ------------------------------------ |
| `random.choice()`  | Selects a random item                |
| `random.sample()`  | Selects multiple unique random items |
| `random.shuffle()` | Randomly rearranges list elements    |
| `.join()`          | Combines list elements into a string |

---

# Learning Objectives

This project helps beginners understand:

* How randomness works in Python
* How passwords are generated programmatically
* Different approaches to building strings
* Basic cybersecurity-related programming concepts

---

# 👩‍💻 Author

Developed as a beginner-friendly Python project to practice programming logic, randomization, and string manipulation.
