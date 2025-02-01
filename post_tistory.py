from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import random

options = webdriver.ChromeOptions()
options.add_argument("--headless") # not display web browser
options.add_argument("--disable-gpu")  # for headless
options.add_argument("--no-sandbox")  # for linux

# init web driver
driver = webdriver.Chrome(options=options)
driver.maximize_window()

def random_wait():
    time.sleep(random.uniform(3, 6))


def post_to_tistory(username, password, tistory_url, title, content, tags):

    try:
        move_login_page(tistory_url)

        select_kakao_login()

        login(password, username)

        move_write_page()

        check_alert(False)

        change_html_mode()

        input_title(title)

        select_category()

        input_contents(content)

        input_tags(tags)

        click_pre_publish()

        select_public()

        publish()

        print("포스팅 완료!")

    except TimeoutException as e:
        print("페이지 로드 시간 초과:", e)

    finally:
        time.sleep(5)
        driver.quit()


def publish():
    print("publish")
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, "publish-btn")))
    publish_button = driver.find_element(By.ID, "publish-btn")
    publish_button.click()
    random_wait()


def select_public():
    print("select_public")
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, "open20")))
    publish_button = driver.find_element(By.ID, "open20")
    publish_button.click()
    random_wait()


def click_pre_publish():
    print("click_pre_publish")
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, "publish-layer-btn")))
    publish_button = driver.find_element(By.ID, "publish-layer-btn")
    publish_button.click()
    random_wait()


def input_tags(tags):
    print(f"input_tags: {tags}")
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.NAME, "tagText")))
    for tag in tags.split(","):
        tag_input = driver.find_element(By.NAME, "tagText")
        tag_input.send_keys(tag.strip())
        tag_input.send_keys(Keys.RETURN)
        random_wait()


def input_contents(content):
    print("input_contents")
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CLASS_NAME, "ReactCodemirror")))
    container = driver.find_element(By.CLASS_NAME, "ReactCodemirror")
    container.click()
    random_wait()

    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".CodeMirror div textarea")))
    editor = driver.find_element(By.CSS_SELECTOR, ".CodeMirror div textarea")
    editor.send_keys(content)
    random_wait()


def select_category():
    print("select_category")
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, "category-btn")))
    category_dropdown = driver.find_element(By.ID, "category-btn")
    category_dropdown.click()
    category_algorithm = "category-item-672117"
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, category_algorithm)))
    category_option = driver.find_element(By.ID, category_algorithm)
    category_option.click()
    random_wait()


def input_title(title):
    print("input_title")
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, "post-title-inp")))
    title_input = driver.find_element(By.ID, "post-title-inp")
    title_input.send_keys(title)
    random_wait()

def change_html_mode():
    print("change_html_mode")
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, "editor-mode-layer-btn-open")))
    normal_mode = driver.find_element(by=By.ID, value='editor-mode-layer-btn-open')
    normal_mode.click()
    random_wait()

    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, "editor-mode-html")))
    html_mode = driver.find_element(by=By.ID, value='editor-mode-html')
    html_mode.click()
    random_wait()

    check_alert(True)
    random_wait()


def check_alert(yes):
    try:
        print("check_alert")
        WebDriverWait(driver, 10).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        if yes:
            alert.accept()
        else:
            alert.dismiss()
        random_wait()
    except TimeoutException:
        print("No Alert, Continue~")


def move_write_page():
    print("move_write_page")
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CLASS_NAME, "btn_tistory")))
    driver.find_element(By.CLASS_NAME, "btn_tistory").click()
    random_wait()


def login(password, username):
    print("login")
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.NAME, "loginId")))
    driver.find_element(By.NAME, "loginId").send_keys(username)
    random_wait()
    driver.find_element(By.NAME, "password").send_keys(password)
    random_wait()
    driver.find_element(By.NAME, "password").send_keys(Keys.RETURN)
    random_wait()


def select_kakao_login():
    print("select_kakao_login")
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CLASS_NAME, "link_kakao_id")))
    driver.find_element(By.CLASS_NAME, "link_kakao_id").click()
    random_wait()


def move_login_page(tistory_url):
    print("move_login_page")
    login_url = f"https://{tistory_url}/manage"
    driver.get(login_url)
    random_wait()


# 사용 예시
if __name__ == "__main__":
    import json
    with open("config.json", "r") as f:
        config = json.load(f)

    _title = "Tistory 포스팅하기"
    _content = """
    <h3>테스트1</h3>
    <ul>
        <li> 테스트1-1 </li>
        <li> 테스트1-2 </li>
    </ul>        
    <h3>테스트2</h3>
    <ul>
        <li> 테스트2-1 </li>
        <li> 테스트2-2 </li>
    </ul>
    """

    code = """
class Solution {
    public:
    int uf[1001];
    int disjoint(int x){
        if(x == uf[x]) return x;
        return uf[x] = disjoint(uf[x]);
    }
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        for(int i = 0 ; i <= 1000; i++){
            uf[i] = i;
        }
        vector<int> ans;
        for(int i = 0 ; i < edges.size(); i++){
            int a = edges[i][0];
            int b = edges[i][1];
            if(disjoint(a) != disjoint(b)){
                uf[disjoint(a)] = disjoint(b);
            } else{
                ans.push_back(a);
                ans.push_back(b);
            }
        }
        return ans;
    }
};
    """

    
    from util.convert_html import tistory_code_block

    _tags = "algorithm, Leetcode, 알고리즘, 릿코드"
    post_to_tistory(config["tistory"]["username"], config["tistory"]["password"],
                    config["tistory"]["tistory_url"], _title, tistory_code_block(code.replace(" " * 4, "\t")), _tags)

