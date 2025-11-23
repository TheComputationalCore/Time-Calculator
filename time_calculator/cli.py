import argparse
from .time_calculator import add_time


def main():
    parser = argparse.ArgumentParser(
        description="Add a duration to a 12-hour start time with optional weekday handling."
    )

    parser.add_argument(
        "start_time",
        type=str,
        help='Start time in 12-hour format, e.g. "3:30 PM"',
    )

    parser.add_argument(
        "duration",
        type=str,
        help='Duration to add, e.g. "2:12"',
    )

    parser.add_argument(
        "start_day",
        nargs="?",
        default=None,
        help='(Optional) Day of the week, e.g. "Monday"',
    )

    args = parser.parse_args()

    result = add_time(args.start_time, args.duration, args.start_day)
    print(result)


if __name__ == "__main__":
    main()
