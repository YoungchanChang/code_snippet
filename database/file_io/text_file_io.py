
with open("text_read.txt", "r", encoding='utf-8-sig') as file:
    # "\n표시 없이 데이터를 한줄씩 리스트로 읽음"
    sample = file.read().splitlines()


with open("text_write.txt", "w", encoding='UTF8') as file:
    for test in sample:
        data = test + "\n"
        file.write(data)