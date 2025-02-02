import argparse
from sync_one_day import request_post
from datetime import datetime, timezone, timedelta


def init_argparse():
    parser = argparse.ArgumentParser()
    parser.add_argument('--start_date', required=True)
    return parser.parse_args()


if __name__ == '__main__':
    args = init_argparse()

    completed = 0
    start_date = datetime.strptime(args.start_date, '%Y-%m-%d').replace(tzinfo=timezone.utc)
    today = datetime.now(timezone.utc)
    while start_date <= today:
        res = request_post(start_date)
        if res:
            completed += 1
        if completed == 10:
            break
        start_date = start_date + timedelta(days=1)
