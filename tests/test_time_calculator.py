from time_calculator import add_time

def test_basic_addition():
    assert add_time("3:30 PM", "2:12") == "5:42 PM"

def test_with_day():
    assert add_time("11:30 AM", "2:32", "Monday") == "2:02 PM, Monday"

def test_next_day():
    assert add_time("10:10 PM", "3:30") == "1:40 AM (next day)"

def test_multiple_days():
    assert add_time("11:43 PM", "24:20", "tueSday") == "12:03 AM, Thursday (2 days later)"
