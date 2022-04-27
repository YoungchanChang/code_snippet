import json
import requests
import csv
headers = {'content-type': 'application/json'}
TEST_URL = ""

answer_key_value = ""
def test_request(json_question: dict):

    utility_answer = requests.post(
        TEST_URL, headers=headers, data=json.dumps(json_question), timeout=3
    )
    answer = json.loads(utility_answer.text).get(answer_key_value)
    return answer


test_answer = []
with open("test.txt", "r", encoding='utf-8-sig') as file:
    sample = file.read().splitlines()
    for sample_item in sample:
        json_question = {
            "query": sample_item
        }
        response = test_request(json_question)
        test_answer.append([sample_item, response])


with open('tmp_csv.csv', 'w', encoding='utf-8-sig', newline='') as writer_csv:
    writer = csv.writer(writer_csv, delimiter=',')
    for test_item in test_answer:
        writer.writerow(test_item)