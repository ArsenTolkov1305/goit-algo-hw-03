from datetime import datetime

mock = '2020-10-09'


def get_days_from_today(date: str) -> int:
    try:
        time_object = datetime.strptime(date, "%Y-%m-%d").date()
        now = datetime.today().date()
        delay = now - time_object
        return delay.days
    except ValueError:
        return "Invalid date format."


# Test
print(get_days_from_today(mock))