def add_time(start_time, duration, start_day=None):
    """
    Add a duration to a starting 12-hour time, optionally adjusting weekday.

    Parameters:
    ------------
    start_time : str
        Time in 12-hour format, e.g. "3:30 PM".
    duration : str
        Duration to add, e.g. "2:12".
    start_day : str, optional
        Starting day of the week, e.g. "Monday".

    Returns:
    ---------
    str
        The resulting time, properly formatted, including:
        - updated AM/PM
        - updated weekday (if provided)
        - day offset: (next day) or (n days later)
    """

    # --- Parse start time ---
    time_part, meridiem = start_time.split()
    start_hours, start_minutes = map(int, time_part.split(':'))

    # Convert starting time to 24-hour format
    if meridiem.upper() == "PM" and start_hours != 12:
        start_hours += 12
    elif meridiem.upper() == "AM" and start_hours == 12:
        start_hours = 0

    # --- Parse duration ---
    dur_hours, dur_minutes = map(int, duration.split(':'))

    # --- Add minutes ---
    total_minutes = start_minutes + dur_minutes
    extra_hours = total_minutes // 60
    final_minutes = total_minutes % 60

    # --- Add hours ---
    total_ho_
