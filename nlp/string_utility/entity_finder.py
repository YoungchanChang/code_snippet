"""
엔티티와 속성값 찾는 로직
1. 엔티티를 찾는다.
2. 속성값을 찾는다.
3. 부정 표현 찾는다.
4. 부가 속성값 찾는다.
"""


from mecab_parser import *


entity = {
    "치킨": ["food", 'location']
}

intent = {
    ('싶', 'VX'): [("food","싶다"), ('location', "싶다")],
    ('괜찮', 'VA'): [("food","괜찮다"), ('location', "괜찮다")],
}

intent_sub = {
    ('먹', 'VV'): [("food", "먹기가")],
    ('가', 'VV'): [("location", "가기가")]
}

intent_not = {
    ('안', 'MAG'): ('F', '안'),
    ('못', 'MAG'): ('F', '못'),
    ('않', 'VX'): ('B', '않다'),
    ('말', 'VX'): ('B', '말다'),
    ('말기', 'NNG'): ('B', '말다'),
    ('없', 'VA'): ('B', '모르다'),
    ('모르', 'VV'): ('B', '모르다'),
    ('아니', 'VCN'): ('B', '아니다')
}


sample_item = "나는 치킨이 안 괜찮다"
mecab_parse_results = list(MecabParser(sentence=sample_item).gen_mecab_compound_token_feature())
mecab_word = [(x[0], x[1].pos) for x in mecab_parse_results]


entity_attr_save = []
for mecab_parse_item in mecab_parse_results:

    mecab_compound_idx = mecab_parse_item[1].mecab_compound
    mecab_word = mecab_parse_item[0]
    word_pos = (mecab_word, mecab_parse_item[1].pos)
    entity_val = entity.get(mecab_word, None)

    if entity_val: # 엔티티 값 저장
        for entity_cat_val in entity_val:
            entity_attr_save.append({
                "category" : entity_cat_val,
                "entity": mecab_word,
                "idx" : [mecab_compound_idx, None],
            })

    intent_val = intent.get(word_pos, None)
    if intent_val: # 인텐트 값 저장
        for intent_cat_val in intent_val: # 2차원 배열 2중 탐색
            for entity_attr_dict in entity_attr_save:
                entity_cat = entity_attr_dict.get('category', None) # 인텐트와 엔티티 값 검증 로직
                if (entity_cat == intent_cat_val[0]) and (entity_attr_dict.get('idx')[0] < mecab_compound_idx):
                    entity_attr_dict["intent"] = intent_cat_val[1]
                    entity_attr_dict['idx'][1] = mecab_compound_idx


for mecab_parse_item in mecab_parse_results:
    mecab_compound_idx = mecab_parse_item[1].mecab_compound
    mecab_word = mecab_parse_item[0]
    word_pos = (mecab_word, mecab_parse_item[1].pos)
    intent_sub_val = intent_sub.get(word_pos, None)
    if intent_sub_val: # 인텐트 값 저장

        for intent_sub_cat_val in intent_sub_val: # 2차원 배열 2중 탐색
            for entity_attr_dict in entity_attr_save:
                entity_cat = entity_attr_dict.get('category', None) # 인텐트와 엔티티 값 검증 로직
                if (entity_cat == intent_sub_cat_val[0]) and (entity_attr_dict.get('idx')[0] < mecab_compound_idx < entity_attr_dict.get('idx')[1]):
                    entity_attr_dict["intent_sub"] = intent_sub_cat_val[1]
                    entity_attr_dict['idx'][1] = mecab_compound_idx

    intent_not_val = intent_not.get(word_pos, None)
    if intent_not_val:
        for entity_attr_dict in entity_attr_save:
            entity_cat = entity_attr_dict.get('category', None) # 인텐트와 엔티티 값 검증 로직
            if entity_attr_dict.get('idx')[0] < mecab_compound_idx and intent_not_val[0] == 'B':
                entity_attr_dict["intent"] = entity_attr_dict["intent"][:-1] + "지"
                intent_replace = entity_attr_dict.get("intent_sub", "") + " " + entity_attr_dict["intent"] + " " + intent_not_val[1]
                entity_attr_dict["intent"] = intent_replace.lstrip()
                entity_attr_dict["not"] = True
            elif entity_attr_dict.get('idx')[0] < mecab_compound_idx and intent_not_val[0] == 'F':
                intent_replace = entity_attr_dict.get("intent_sub", "") + " " + intent_not_val[1] + " " + entity_attr_dict["intent"]
                entity_attr_dict["intent"] = intent_replace.lstrip()
                entity_attr_dict["not"] = True

print(entity_attr_save)




