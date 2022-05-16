import copy
from pathlib import Path

from nlp.string_utility.mecab_parser import mecab_word_finder, MecabParser

FORBIDDEN_POS = ["JKS", "JKB", 'VCP']
EOF = "EOF"

DATA_PATH = Path(__file__).resolve().parent.parent.joinpath("data", "mecab")


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

        try:
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
        except TypeError as te:
            ...


def read_attribute(suffix="main"):
    """데이터 딕셔너리에서 속성값 읽는 함수"""
    ATTRIBUTE_SEPARATOR = "#"
    for i in Path.iterdir(DATA_PATH):
        if (i.suffix == ".txt") and (i.stem.split("_")[1] == suffix):
            with open(str(i.parent) + "/" + str(i.name), "r", encoding='utf-8-sig') as file:
                # "\n표시 없이 데이터를 한줄씩 리스트로 읽음"
                sample = file.read().splitlines()

                title = None
                return_data = []
                for sample_item in sample:
                    if ATTRIBUTE_SEPARATOR in sample_item:
                        title = sample_item.replace(ATTRIBUTE_SEPARATOR, "")
                    elif sample_item.strip() != '':
                        return_data.append((title, sample_item, i.stem)) # 소제목 로드시 문자열 비교 위해 필요

            return_data = sorted(return_data, key=lambda x : len(x[1]), reverse=True)
            yield from return_data # Return Iterator


if __name__ == "__main__":

    mecab_word_found = MecabParser(sentence="어 그니까 팔이 아파").get_mecab_words()
    insert_mecab_word = [(x[0], x[1].pos) for x in mecab_word_found]

    entity_list = list(extract_entity(insert_mecab_word))

    intent_main = {}
    for i in read_attribute(suffix="main"):
        intent_main[eval(i[1])] = [(i[0], i[2].split("_")[0])]

    intent_sub = {}
    for i in read_attribute(suffix="sub"):
        intent_sub[eval(i[1])] = [(i[0], i[2].split("_")[0])]
    print(intent_main)
    print(intent_sub)