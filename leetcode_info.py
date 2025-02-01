import requests
from datetime import datetime, timedelta
import time

# GraphQL query
query = """
query dailyCodingChallengeRecord($year: Int!, $month: Int!) {
  dailyCodingChallengeV2(year: $year, month: $month) {
    challenges {
      date
      userStatus
      link
      question {
        questionFrontendId
        title
        titleSlug
        content
      }
    }
  }
}
"""

def format_date(date=None):
    """
    Format the current or provided date into year, month, and formatted date strings.
    """
    if date is None:
        date = datetime.now()
    year = date.year
    month = date.month
    day = date.day
    formatted_date = f"{year}-{str(month).zfill(2)}-{str(day).zfill(2)}"
    return {
        "year": year,
        "month": month,
        "day": day,
        "formatted_date": formatted_date,
    }

def fetch_daily_challenges(year, month):
    """
    Fetch daily coding challenges from LeetCode's GraphQL API.
    """
    headers = {
        'content-type': 'application/json',
    }
    body = {
        "query": query,
        "variables": {"year": year, "month": month},
    }
    try:
        response = requests.post('https://leetcode.com/graphql/', json=body, headers=headers)
        response.raise_for_status()
        result = response.json()
        return result.get('data', {}).get('dailyCodingChallengeV2', {}).get('challenges', [])
    except requests.RequestException as error:
        print(f"Error fetching daily challenges: {error}")
        return None


def get_daily_problem(date):
    """
    Retrieve today's daily coding problem and print its title.
    """
    date_info = format_date(date)
    print(date_info)
    year = date_info["year"]
    month = date_info["month"]
    formatted_date = date_info["formatted_date"]

    challenges = fetch_daily_challenges(year, month)
    if not challenges:
        print('Failed to retrieve daily challenges.')
        return

    daily_challenge = next((challenge for challenge in challenges if challenge["date"] == formatted_date), None)
    if daily_challenge:
        print(f"Today's Daily Problem Details: {daily_challenge['question']}")
    else:
        print('No daily problem found for today.')
    return daily_challenge['question']

# Run the function to get today's problem
if __name__ == "__main__":
    start_date = datetime.strptime("2024-06-01","%Y-%m-%d")
    end_date = datetime.now()
    while start_date <= end_date:
        get_daily_problem(start_date)
        start_date += timedelta(days=1)
        time.sleep(1)

