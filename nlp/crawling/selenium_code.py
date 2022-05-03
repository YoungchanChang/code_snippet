import time
from selenium import webdriver

# chromedriver = 'C:/dev_python/Webdriver/chromedriver.exe' # 윈도우
chromedriver = '/Users/youngchan/Desktop/bokji-qa/user_interest/user_character_entity/tests/chromedriver' # 맥
driver = webdriver.Chrome(chromedriver)

# 1. url 설정
url = "https://ko.dict.naver.com/#/search?range=example&page=1&query=%ED%86%B5%EC%A6%9D&autoConvert="
driver.get(url)
time.sleep(3)
test_list = []

# 2. 함수 설정
def get_elem():
    try:
        for i in range(1, 16, 1):
            time.sleep(1)
            elems = driver.find_element_by_css_selector(f'#searchPage_example > div.component_example.has-saving-function > div:nth-child({i}) > div > span')
            test_list.append(elems.text)
    except Exception as e:
        print(e)

# 3. 범위 설정
range_list = [str(x) for x in range(2, 11, 1)]
range_list.append('Next')
range_list.extend([str(x) for x in range(12, 21, 1)])
range_list.append('Next')
range_list.extend([str(x) for x in range(22, 31, 1)])
range_list.append('Next')

# 4. 범위 실행
try:
    for range_item in range_list:
        continue_link = driver.find_element_by_link_text(range_item)
        webdriver.ActionChains(driver).click(continue_link).perform()
        get_elem()
except Exception as e:
    ...

# 저장
with open("text_write.txt", "w", encoding='UTF8') as file:
    for test in test_list:
        data = test + "\n"
        file.write(data)
