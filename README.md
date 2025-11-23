# Time Calculator

A polished Python utility that computes the resulting time after adding a duration to a starting time, with optional weekday tracking.

## Features
- Works with **12-hour format** and AM/PM transitions  
- Accepts a duration of any length (e.g., `"205:12"`)  
- Optional **day-of-week awareness**  
- Outputs human-readable results  
- Handles edge cases: midnight, noon, multi‑day rollovers  
- Lightweight — **no external dependencies**

## Installation
Clone the repository:
```bash
git clone https://github.com/TheComputationalCore/Time-Calculator.git
cd Time-Calculator
```

## Usage
Import and use the `add_time` function:

```python
from time_calculator.time_calculator import add_time

print(add_time("3:30 PM", "2:12"))  
print(add_time("11:30 AM", "2:32", "Monday"))
print(add_time("10:10 PM", "3:30"))
print(add_time("11:43 PM", "24:20", "Tuesday"))
print(add_time("6:30 PM", "205:12"))
```

### Example Outputs
```
5:42 PM
2:02 PM, Monday
1:40 AM (next day)
12:03 AM, Thursday (2 days later)
7:42 AM (9 days later)
```

## Project Structure
```
├── time_calculator
│   ├── __init__.py
│   └── time_calculator.py
├── tests
│   └── test_time_calculator.py
├── docs
│   ├── index.md
│   └── usage.md
├── README.md
├── pyproject.toml
└── mkdocs.yml
```

## Contributing
1. Fork the repo  
2. Create a feature branch: `git checkout -b feature-name`  
3. Commit your changes  
4. Push and open a PR  

## License
MIT License © TheComputationalCore
