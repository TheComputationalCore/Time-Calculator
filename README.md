# ⏱️ Time Calculator

A **professional, lightweight, and human-friendly Python utility** for performing advanced time arithmetic using 12‑hour format, durations of any size, and optional weekday calculations.

<p align="left">
  <img src="https://img.shields.io/badge/Language-Python_3.10+-blue.svg" />
  <img src="https://img.shields.io/badge/License-MIT-green.svg" />
  <img src="https://img.shields.io/badge/Docs-Automated-success.svg" />
  <img src="https://img.shields.io/badge/Build-Passing-brightgreen.svg" />
</p>

---

## 🌟 Overview

Time Calculator helps you compute resulting times with:
- Automatic **AM/PM rollover**
- **Multi‑day handling** (`(next day)` or `(n days later)`)
- Optional **weekday tracking**
- Support for **very large durations**
- Clean, reliable, deterministic output
- Full test suite + documentation site

---

## 🚀 Features

- ⏰ Precise 12‑hour time support  
- 📅 Optional weekday awareness  
- ➕ Duration arithmetic with unlimited hours  
- 🔁 Handles midnight, noon, edge cases, and multi-day transitions  
- 🧩 Zero external dependencies  
- 🧪 Fully tested  
- 📝 Beautiful documentation  

---

## 📦 Installation

Clone the project:

```bash
git clone https://github.com/TheComputationalCore/Time-Calculator.git
cd Time-Calculator
```

Install locally:

```bash
pip install .
```

---

## 🧠 Usage

```python
from time_calculator.time_calculator import add_time

print(add_time("3:30 PM", "2:12"))
print(add_time("11:30 AM", "2:32", "Monday"))
print(add_time("10:10 PM", "3:30"))
print(add_time("11:43 PM", "24:20", "Tuesday"))
print(add_time("6:30 PM", "205:12"))
```

### 📤 Output:

```
5:42 PM
2:02 PM, Monday
1:40 AM (next day)
12:03 AM, Thursday (2 days later)
7:42 AM (9 days later)
```

---

## 🖥️ Command-Line Interface

Run directly:

```bash
python -m time_calculator "3:30 PM" "2:12"
```

Or:

```bash
python time_calculator/cli.py "10:10 PM" "3:30"
```

---

## 📚 Documentation

Your full documentation is live at:

👉 https://thecomputationalcore.github.io/Time-Calculator/

Includes:
- API reference  
- Examples  
- Usage guide  
- Developer notes  

---

## 🧪 Testing

Run all tests:

```bash
pytest -q
```

---

## 🗂️ Project Structure

```
Time-Calculator/
├── time_calculator/
│   ├── __init__.py
│   ├── cli.py
│   └── time_calculator.py
├── tests/
│   └── test_time_calculator.py
├── docs/
│   ├── index.md
│   ├── usage.md
│   └── api.md
├── .github/workflows/
│   ├── deploy-docs.yml
│   └── tests.yml
├── mkdocs.yml
├── pyproject.toml
└── README.md
```

---

## 🤝 Contributing

1. Fork the repo  
2. Create a feature branch  
3. Commit your improvements  
4. Push & open a PR  

---

## 📜 License  
MIT License © TheComputationalCore

---

⭐ If this project helps you, consider **starring the repository**!
