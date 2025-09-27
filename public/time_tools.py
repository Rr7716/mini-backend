from datetime import datetime


def is_same_day(now_date: datetime, create_date: datetime):
    return create_date.year == now_date.year and create_date.month == now_date.month and create_date.day == now_date.day
    