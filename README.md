# ⏱️ Time Calculator  

The **Time Calculator** allows you to add durations to start times in 12‑hour format, intelligently handling AM/PM transitions, weekday rollovers, large durations, and clean human‑readable output.  
Designed to be **lightweight**, **reliable**, and **easy to use**—perfect for automation, scheduling tasks, and coding challenges.

---

## 🚀 Features

- ⏰ **12‑hour AM/PM format support**
- ➕ **Add durations of any size** (e.g., `"205:12"`)
- 📅 **Optional weekday tracking**
- 🔁 **Handles multi‑day rollovers**
- 🕛 Correctly handles **midnight** and **noon**
- 🧪 **Tested & documented**
- 🧩 **Zero dependencies**

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/TheComputationalCore/Time-Calculator.git
cd Time-Calculator
```

---

## 🧠 Usage

Import the function:

```python
from time_calculator.time_calculator import add_time
```

### 💡 Examples

```python
print(add_time("3:30 PM", "2:12"))
# → 5:42 PM

print(add_time("11:30 AM", "2:32", "Monday"))
# → 2:02 PM, Monday

print(add_time("10:10 PM", "3:30"))
# → 1:40 AM (next day)

print(add_time("11:43 PM", "24:20", "tuesday"))
# → 12:03 AM, Thursday (2 days later)

print(add_time("6:30 PM", "205:12"))
# → 7:42 AM (9 days later)
```

---

## 🛠️ Command‑Line Interface (CLI)

The package includes a CLI tool:

```bash
python -m time_calculator "3:30 PM" "2:12"
```

Or directly:

```bash
python time_calculator/cli.py "3:30 PM" "2:12"
```

---

## 📚 Project Structure

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
│   ├── api.md
│   └── usage.md
├── .github/workflows/
│   ├── deploy-docs.yml
│   └── tests.yml
├── mkdocs.yml
├── pyproject.toml
└── README.md
```

---

## 📘 Documentation

Full documentation (built with MkDocs) is available at:

👉 **https://thecomputationalcore.github.io/Time-Calculator/**

Includes:
- API reference  
- Usage guide  
- Examples  
- Developer notes  

---

## 🧪 Testing

Run tests:

```bash
pytest -q
```

---

## 🤝 Contributing

1. Fork the repository  
2. Create a feature branch  
   ```bash
   git checkout -b feature-name
   ```
3. Commit changes  
4. Push your branch  
5. Open a pull request  

---

## 📜 License

Released under the **MIT License**  
© TheComputationalCore

---

## ⭐ Support the Project

If this project helped you, consider **starring the repository** ⭐ on GitHub!
