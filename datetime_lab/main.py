# coding: utf-8

import time
from datetime import datetime, timedelta, timezone


def get_cur_timestamp():
    time_now = time.time()  # 1585673800.394683
    print(time_now)

    datetime_now = datetime.now().timestamp()  # 1585673800.394719
    print(datetime_now)


def stamp2datetime():
    timestamp = 1585650200
    # time模块
    utc_time = time.gmtime(timestamp)  # UTC时间
    local_time = time.localtime(timestamp)  # 本地时间
    print(utc_time, local_time)

    # datetime模块
    utc_datetime = datetime.utcfromtimestamp(timestamp)  # UTC时间
    local_datetime = datetime.fromtimestamp(timestamp)  # 本地时间
    print(utc_datetime, local_datetime)


# 时间戳转字符串
def stamp2time_str():
    timestamp = 1585650200

    # time, 以utc为例
    utc_time = time.gmtime(timestamp)
    time_str = time.strftime("%y-%m-%D %H:%M:%S %I", utc_time)

    # datetime，以utc为例
    utc_datetime = datetime.utcfromtimestamp(timestamp)
    time_str2 = utc_datetime.strftime("%Y-%m-%d %H:%M:%S")
    print(time_str, time_str2)


def time_str2stamp():
    time_str = "2020-03-31 10:23:20"

    time_ = time.strptime(time_str, "%Y-%m-%d %H:%M:%S")
    timestamp = time.mktime(time_)

    datetime_ = datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")
    timestamp2 = datetime_.timestamp()

    print(timestamp, timestamp2)


def time_add_and_sub():
    time_str = "2020-03-31 10:23:20"

    datetime_ = datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")
    time_add_8_hour = datetime_ + timedelta(hours=8)
    print(time_add_8_hour)

    time_sub_1_day = datetime_ - timedelta(days=1)
    print(time_sub_1_day)


def time_zone():
    # 指定零时区
    tz_utc_0 = timezone(timedelta(hours=9))
    print(datetime.now(tz=tz_utc_0))


if __name__ == '__main__':
    time_zone()
