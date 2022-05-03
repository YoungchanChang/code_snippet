import os, sys
import time
import re
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import requests
from bs4 import BeautifulSoup
import time

import os, sys
UTILITY_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/utility"
print(UTILITY_DIR)
sys.path.append(UTILITY_DIR)


class BSUtil:

    def __init__(self):
        self.header = { "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36",
                        "cookie": "<MyCookie>",
                        }


    def ask_question(self, question):

        headers = {"Ocp-Apim-Subscription-Key": "<KEY>"}
        params = {"q": question, "textDecorations": True, "textFormat": "HTML"}
        response = requests.get("https://api.bing.microsoft.com/v7.0/search", headers=headers, params=params)
        response.raise_for_status()
        search_results = response.json()
        print(search_results['webPages']['webSearchUrl'])

        my_url = search_results['webPages']['webSearchUrl']
        print(my_url)

        st = time.time()
        a = requests.get(my_url, headers=self.header)
        print(time.time() - st)
        soup = BeautifulSoup(a.content, 'html.parser')

        section = soup.find('div', class_='dc_mn')
        if section:
            print("dc_mn")
            return section.text, "dc_mn"

        b_focusTextMedium= soup.find('div', class_='b_focusTextMedium')
        if b_focusTextMedium:
            print("b_focusTextMedium")
            return b_focusTextMedium.text, "b_focusTextMedium"

        b_focusTextLarge = soup.find('div', class_='b_focusTextLarge')
        if b_focusTextLarge:
            print("b_focusTextLarge")
            return b_focusTextLarge.text, "b_focusTextLarge"

        b_paractl = soup.find('p', class_='b_paractl')
        if b_paractl:
            # tag_list = b_paractl.find_all("strong")
            answer_list = [x.get_text() for x in b_paractl.find_all("strong")]
            my_list = ' and '.join(answer_list)
            if len(my_list) == 0:
                return 'None', 'None'
            return my_list, "b_paractl"

        elc_cname = soup.find_all('div', class_='elc_cname')
        if elc_cname:
            # tag_list = b_paractl.find_all("strong")
            answer_list = [x.get_text() for x in elc_cname]
            my_list = ' and '.join(answer_list)
            print("elc_cname")
            return my_list, "elc_cname"

        rwrl = soup.find('div', class_='rwrl')
        if rwrl:

            # li태그로 나열되어있는 경우 아래 출력
            rwrl_li = [x.get_text() for x in rwrl.findAll('li')]
            if rwrl_li:
                answer_str = ' and '.join(rwrl_li)
                print("rwrl")
                return answer_str, "rwrl-li"
            return rwrl.text, "rwrl" # 지운 이유 : tell me good food of strawberry

        qna_mf = soup.find('div', class_='qna-mf')
        if qna_mf:
            print("qna-mf")
            return qna_mf.text, "qna-mf"

        mf_item = soup.find('div', class_='mf-item')
        if mf_item:
            print("mf-item")
            return mf_item.text, "mf-item"

        return 'None', 'None'

    def regex_of_bs4(self, context, where):
        """ 셀레니움에서 가져온 답변 정제하기 """

        context = re.sub(r'www\.([a-z|A-Z|0-9])+\.([a-z|A-Z|0-9])+', r' ', str(context))  # www제거하기
        context = re.sub(r"[a-z|A-Z|0-9]+\.(com|edu|tk|net|de|uk|org|cn|ru|info)", r' ', str(context))  # 최상위 도메인부터 제거하기
        context = re.sub("\\u200B", r'',str(context)) # u200b 조판없는 문자 제거하기
        if where != "qna-mf":
            pattern2 = r'([a-z|A-Z|0-9])+\.([a-z|A-Z|0-9])+\.'  # . 기준으로 단어만 있는 경우 지우기 qna-mf는 단어.단어.단어 기준이 많기 때문에
            context = re.sub(pattern2, r' ', str(context))

        context = re.sub(r'\((.*?)\)', r' ', str(context))  # 괄호 안에 있는 내용 지우기.
        context = re.sub(r'[,|:]', r' ', str(context))  # 괄호 안에 있는 내용 지우기.
        context = re.sub(r"[\.|\n](\w)", r'. \1', str(context))  # . 바로 뒤에 단어가 오는 경우 스페이스 주기
        context = re.sub(r"\.{2}", r'.', str(context))  # .. 이면 .으로 바꾸기
        context = re.sub(r"\.{2,}", r' ', str(context))  # .. 등의 표현 지우기
        context = re.sub(r"\s{2,}", r' ', str(context))  # 공백 2번 이상은 1번으로 변경하기.
        context = re.sub(r"\u2019", r' ', str(context))  # 공백 2번 이상은 1번으로 변경하기.
        context = re.sub(r"\u2018", r' ', str(context))  # 공백 2번 이상은 1번으로 변경하기.
        context = re.sub(r"\n", r' ', str(context))  # 공백 2번 이상은 1번으로 변경하기.
        context = context.replace("\n", "")
        regex_only_eng = "[^\w\s\.]"
        context = re.sub(regex_only_eng, ' ', context)
        return context, where


if __name__ == "__main__":

    user_sentence = "michael jordan"
    print("NO")
