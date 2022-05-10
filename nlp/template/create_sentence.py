"""
문장 템플릿으로 만드는 모듈
"""
from nlp.string_check import josa_change


answer = []
with open("test_txt.txt", "r", encoding='utf-8-sig') as file:
    # "\n표시 없이 데이터를 한줄씩 리스트로 읽음"
    sample = file.read().splitlines()

    for sample_item in sample:
        hint_item = "{entity} " + sample_item
        # hint_item = josa_change(sample_item, hint_item)
        answer.append(hint_item)


with open("test_write.txt", "w", encoding='UTF8') as file:
    for test in answer:
        data = test + "\n"
        file.write(data)