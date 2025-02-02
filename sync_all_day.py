from sync_one_day import request_post
from datetime import datetime, timezone, timedelta

if __name__ == '__main__':
    completed = 0
    start_date = datetime.strptime('2024-06-23', '%Y-%m-%d').replace(tzinfo=timezone.utc)
    print(start_date)
    today = datetime.now(timezone.utc)
    while start_date <= today:
        res = request_post(start_date)
        if not res:
            continue
        completed += 1
        if completed == 10:
            break
        start_date = start_date + timedelta(days=1)
