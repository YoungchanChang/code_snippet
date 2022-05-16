import copy
from pathlib import Path

from nlp.string_utility.mecab_parser import mecab_word_finder, MecabParser

FORBIDDEN_POS = ["JKS", "JKB", 'VCP']
EOF = "EOF"

DATA_PATH = Path(__file__).resolve().parent


def read_entity(path):
    """데이터 읽는 함수"""
    for i in Path.iterdir(path):
        if i.suffix == ".txt":
            with open(str(i.parent) + "/" + str(i.name), "r", encoding='utf-8-sig') as file:
                # "\n표시 없이 데이터를 한줄씩 리스트로 읽음"
                sample = file.read().splitlines()
                sample = [x for x in sample if x != ""]
                sample = sorted(sample, key=len, reverse=True) # 문자열 긴 순서대로 정렬
                for sample_item in sample:
                    if "#" not in sample_item:
                        yield sample_item, i.stem
            yield EOF, i.stem


def extract_entity(mecab_word_found):
    copied_mecab_word_found = copy.copy(mecab_word_found)
    tmp_mecab_word_found = " ".join([x[0] for x in mecab_word_found])
    copied_mecab_word_found = " ".join([x[0] for x in copied_mecab_word_found])

    for i in read_entity(DATA_PATH):
        item, stem = i

        if item == EOF: # CHECK if one category is finished
            copied_mecab_word_found = tmp_mecab_word_found # COPY when category over

        elif item.count(",") == 1:
            word, mecab_word = item.split(",")

            mecab_word_found_result = mecab_word_finder(copied_mecab_word_found, mecab_word) # FIND string value
            copied_mecab_word_found, word_idx = mecab_word_found_result
            if mecab_word_found_result and (mecab_word_found[word_idx][1] not in FORBIDDEN_POS): # REPLACE if exists
                yield word, stem, word_idx

        elif item.count(",") == 2:
            word, mecab_word, meta_info = item.split(",")

            mecab_word_found_result = mecab_word_finder(copied_mecab_word_found, mecab_word) # FIND string value
            copied_mecab_word_found, word_idx = mecab_word_found_result

            if mecab_word_found_result: # REPLACE if exists
                yield word, stem, meta_info, word_idx


if __name__ == "__main__":

    mecab_word_found = MecabParser(sentence="어 그니까 팔이 아파").get_mecab_words()
    insert_mecab_word = [(x[0], x[1].pos) for x in mecab_word_found]

    entity_list = list(extract_entity(insert_mecab_word))
    x = 4