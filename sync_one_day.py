import json
from datetime import datetime, timezone

from github_info import get_repo_contents
from leetcode_info import get_daily_problem
from database import is_daily_date_exists, insert_problem_name
from llama_3_2_3B import explain_solution
from util.convert_html import *
from post_tistory import post_to_tistory


def request_post(date):
    with open("config.json", "r") as f:
        config = json.load(f)

    if is_daily_date_exists(date):
        print("already synced")
        return None

    problem = get_daily_problem(date)
    if not problem:
        print("problem not found")
        return None
    print('titleSlug', problem['titleSlug'])
    print('content', problem['content'])


    code = get_repo_contents(problem['titleSlug'])
    if not code:
        print("code not found")
        return None
    print(code)

    blog_content_dict = explain_solution(problem['content'], code)
    print('solution', blog_content_dict)

    blog_content_html = get_leetcode_link(problem['title'], problem['titleSlug'])
    blog_content_html += dict_to_html(blog_content_dict)
    blog_content_html += tistory_code_block(code)

    tags = "algorithm, Leetcode, 알고리즘, 릿코드"
    post_to_tistory(config["tistory"]["username"], config["tistory"]["password"],
                    config["tistory"]["tistory_url"], problem['title'], blog_content_html, tags)

    insert_problem_name(problem['titleSlug'], date)
    return True


if __name__ == "__main__":
    # today = datetime.strptime("2025-02-01", "%Y-%m-%d")
    today = datetime.now(timezone.utc)
    request_post(today)
