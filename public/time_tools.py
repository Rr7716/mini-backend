from datetime import datetime, timedelta


def is_same_day(date1: datetime, date2: datetime):
    return date2.year == date1.year and date2.month == date1.month and date2.day == date1.day
    
def is_same_week(date1: datetime, date2: datetime):
    # 获取 ISO 周历 (year, week number, weekday)
    y1, w1, _ = date1.isocalendar()
    y2, w2, _ = date2.isocalendar()
    return (y1, w1) == (y2, w2)

def get_week_range():
    now = datetime.now()
    weekday = now.isoweekday()

    # 算周一 (1 表示周一)
    monday = now - timedelta(days=weekday - 1)
    monday = monday.replace(hour=0, minute=0, second=0, microsecond=0)

    # 算周日
    sunday = monday + timedelta(days=6)
    sunday = sunday.replace(hour=23, minute=59, second=59, microsecond=0)

    return monday.strftime('%Y-%m-%d %H:%M:%S'), sunday.strftime('%Y-%m-%d %H:%M:%S')