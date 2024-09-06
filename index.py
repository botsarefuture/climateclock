import requests
from datetime import datetime, timedelta
import time


def get_time_and_format():
    response = requests.get("https://api.climateclock.world/v2/clock.json")
    time1 = response.json()["data"]["modules"]["carbon_deadline_1"]["timestamp"]
    cat = datetime.fromisoformat(time1)
    climate_time = datetime(
        cat.year, cat.month, cat.day, cat.hour, cat.minute, cat.second
    )
    return climate_time


def get_current():
    now_time = datetime.now()
    now_time = datetime(
        now_time.year,
        now_time.month,
        now_time.day,
        now_time.hour,
        now_time.minute,
        now_time.second,
    )
    return now_time


def calc_years(timeleft):
    years = timeleft / timedelta(days=365)
    years = int(str(years)[0:1])
    return years


while True:
    try:
        climate_time = get_time_and_format()
    except:
        climate_time = "2029-07-22T16:00:00+00:00"
    times = 0
    while times < 300:
        now_time = get_current()
        timeleft = climate_time - now_time
        years = calc_years(timeleft)
        timeleft = timeleft - timedelta(days=(years * 365))
        print(f"Time left to end of world: {years} years {timeleft}", end="\r")
        time.sleep(0.5)
        times += 0.5
