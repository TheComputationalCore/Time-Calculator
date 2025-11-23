def add_time(start_time, duration, start_day=None):
    """
    Add a duration to a start time in 12-hour format with optional weekday handling.

    Parameters
    ----------
    start_time : str
        Time in 12-hour format, e.g., "3:30 PM".
    duration : str
        Duration in the format "H:MM".
    start_day : str, optional
        Optional starting day of the week (case-insensitive).

    Returns
    -------
    str
        The resulting time with proper formatting, including:
        - updated AM/PM
        - updated weekday (if provided)
        - next day / n days later (if applicable)
    """

    # Parse start time
    time_part, meridiem = start_time.split()
    start_hours, start_minutes = map(int, time_part.split(':'))

    # Convert to 24-hour time
    meridiem = meridiem.upper()
    if meridiem == "PM" and start_hours != 12:
        start_hours += 12
    elif meridiem == "AM" and start_hours == 12:
        start_hours = 0

    # Parse duration
    dur_hours, dur_minutes = map(int, duration.split(':'))

    # Add minutes
    total_minutes = start_minutes + dur_minutes
    extra_hours = total_minutes // 60
    final_minutes = total_minutes % 60

    # Add hours
    total_hours = start_hours + dur_hours + extra_hours
    days_later = total_hours // 24
    final_hour_24 = total_hours % 24

    # Convert back to 12-hour component
    if final_hour_24 == 0:
        final_hour_12 = 12
        meridiem = "AM"
    elif final_hour_24 == 12:
        final_hour_12 = 12
        meridiem = "PM"
    elif final_hour_24 > 12:
        final_hour_12 = final_hour_24 - 12
        meridiem = "PM"
    else:
        final_hour_12 = final_hour_24
        meridiem = "AM"

    # Build base result
    result = f"{final_hour_12}:{final_minutes:02d} {meridiem}"

    # Weekday handling
    if start_day:
        weekdays = [
            "monday", "tuesday", "wednesday",
            "thursday", "friday", "saturday", "sunday"
        ]
        start_day_index = weekdays.index(start_day.lower())
        final_day_index = (start_day_index + days_later) % 7
        result += f", {weekdays[final_day_index].capitalize()}"

    # Add day rollover info
    if days_later == 1:
        result += " (next day)"
    elif days_later > 1:
        result += f" ({days_later} days later)"

    return result
