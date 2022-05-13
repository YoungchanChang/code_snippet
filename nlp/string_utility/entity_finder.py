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
    ('싶', 'VX'): ["food", 'location'],
    ('괜찮', 'VA'): ["food", 'location'],
}

intent_sub = {
    ('먹', 'VV'): ["food"],
    ('가', 'VV'): ["location"]
}

intent_not = {
    ('안', 'MAG'): 1,
    ('못', 'MAG'): 1,
    ('않', 'VX'): 1,
    ('말', 'VX'): 1,
    ('말기', 'NNG'): 1,
    ('없', 'VA'): 1,
    ('모르', 'VV'): 1,
    ('아니', 'VCN'): 1
}


sample_item = "나는 치킨이 괜찮지 않아"
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
                "is_matching" : False
            })

    intent_val = intent.get(word_pos, None)
    if intent_val: # 인텐트 값 저장
        for intent_cat_val in intent_val: # 2차원 배열 2중 탐색
            for entity_attr_dict in entity_attr_save:
                entity_cat = entity_attr_dict.get('category', None) # 인텐트와 엔티티 값 검증 로직
                if (entity_cat == intent_cat_val) and (entity_attr_dict.get('idx')[0] < mecab_compound_idx):
                    entity_attr_dict["is_matching"] = True
                    entity_attr_dict["intent"] = mecab_word
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
                if (entity_cat == intent_sub_cat_val) and (entity_attr_dict.get('idx')[0] < mecab_compound_idx < entity_attr_dict.get('idx')[1]):
                    entity_attr_dict["intent_sub"] = mecab_word
                    entity_attr_dict['idx'][1] = mecab_compound_idx

    intent_not_val = intent_not.get(word_pos, None)
    if intent_not_val:
        for entity_attr_dict in entity_attr_save:
            entity_cat = entity_attr_dict.get('category', None) # 인텐트와 엔티티 값 검증 로직
            if entity_attr_dict.get('idx')[0] < mecab_compound_idx:
                entity_attr_dict["not"] = True


print(entity_attr_save)




