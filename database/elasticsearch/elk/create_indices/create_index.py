# -*- coding: utf-8 -*-
from elasticsearch import Elasticsearch

local_ip = "127.0.0.1"
es_port = "9200"

es = Elasticsearch(
    hosts=[ {'host': local_ip, 'port': es_port, "timeout": 120, "max_retries": 10, "retry_on_timeout": True},]
)


class ElasticsearchIndexException(Exception):
    pass


def recreate_elastic_index(elastic_index, body, recreate= False):
    for index in es.indices.get('*'):
        if index == elastic_index and recreate is False:
            raise ElasticsearchIndexException("이미 인덱스가 존재합니다.")

    es.indices.delete(index=elastic_index, ignore=[400, 404])

    create_result = es.indices.create(index=elastic_index, body=body, ignore=400, )

    if create_result['acknowledged'] is False:
        raise ElasticsearchIndexException("이미 인덱스가 존재합니다.")


from pathlib import Path
import os
BASE_DIR_PATH = Path(__file__).resolve().parent
BASE_DIR_OS = os.path.dirname(os.path.abspath(__file__))
sub_dir_file = BASE_DIR_PATH / 'index_info' / 'user_interest_push.json'

import json
if __name__ == "__main__":
    with open(sub_dir_file, "r") as st_json:
        st_python = json.load(st_json)
    elastic_index = "user_interest_push"
    recreate_elastic_index(elastic_index, st_python, recreate=True)
    # print(es.indices.get_alias("*"))
    # # 기존에 index list 뽑아와
    # se와_elastic_index(st_python)