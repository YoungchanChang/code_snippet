# !pip install transformers==4.4.2
# !pip install sentencepiece
# !pip install tensorflow_addons

import os
import csv
from transformers import *
import tensorflow as tf
import tensorflow_addons as tfa
import numpy as np
from tokenization_kobert import KoBertTokenizer


max_seq_len = 64
LR = 3e-5
initializer_range = 0.2
tokenizer = KoBertTokenizer.from_pretrained('monologg/kobert')


def create_model():
    model = TFBertModel.from_pretrained("monologg/kobert", from_pt=True)

    input_ids_layer = tf.keras.layers.Input(shape=(max_seq_len,), dtype=tf.int32)
    attention_masks_layer = tf.keras.layers.Input(shape=(max_seq_len,), dtype=tf.int32)
    token_type_ids_layer = tf.keras.layers.Input(shape=(max_seq_len,), dtype=tf.int32)

    outputs = model([input_ids_layer, attention_masks_layer, token_type_ids_layer])
    pooled_output = outputs[1]

    optimizer = tfa.optimizers.RectifiedAdam(lr=LR)

    pooled_output = tf.keras.layers.Dropout(0.5)(pooled_output)
    prediction = tf.keras.layers.Dense(1, activation='sigmoid',
                                       kernel_initializer=tf.keras.initializers.TruncatedNormal(
                                           stddev=initializer_range))(pooled_output)
    cls_model = tf.keras.Model([input_ids_layer, attention_masks_layer, token_type_ids_layer], prediction)
    cls_model.compile(optimizer=optimizer, loss=tf.keras.losses.BinaryCrossentropy(), metrics=['accuracy'])
    cls_model.summary()

    return cls_model


def sentence_prediction(example):
    global tokenizer

    input_ids, attention_masks, token_type_ids = [], [], []

    input_id = tokenizer.encode(example, max_length=max_seq_len, pad_to_max_length=True)

    # attention_mask는 실제 단어가 위치하면 1, 패딩의 위치에는 0인 시퀀스.
    padding_count = input_id.count(tokenizer.pad_token_id)
    attention_mask = [1] * (max_seq_len - padding_count) + [0] * padding_count

    # token_type_id는 세그먼트 임베딩을 위한 것으로 이번 예제는 문장이 1개이므로 전부 0으로 통일.
    token_type_id = [0] * max_seq_len

    input_ids.append(input_id)
    attention_masks.append(attention_mask)
    token_type_ids.append(token_type_id)

    input_ids = np.array(input_ids)
    attention_masks = np.array(attention_masks)
    token_type_ids = np.array(token_type_ids)
    return [input_ids, attention_masks, token_type_ids]


def evaluation_predict(sentence):
    data_x = sentence_prediction(sentence)
    predict = kobert_model.predict(data_x)

    print('예측 결과 수치', predict)
    predict_value = np.ravel(predict)
    predict_answer = np.round(predict_value, 0).item()
    print('0.5 기준으로 레이블 변환', predict_answer)

    if predict_answer == 0:
        print("(부정 확률 : %.2f) 부정 데이터입니다." % (1 - predict_value))
    elif predict_answer == 1:
        print("(긍정 확률 : %.2f) 긍정 데이터입니다." % predict_value)

    return predict_answer, predict_value


if __name__ == "__main__":
    kobert_model = create_model()
    path = 'checkpoint'
    checkpoint_path = f"{path}/bert-base"
    checkpoint_dir = os.path.dirname(checkpoint_path)
    print(checkpoint_dir)
    latest = tf.train.latest_checkpoint(checkpoint_dir)
    kobert_model.load_weights(latest)


    tmp_data = []
    with open("test_data.txt", "r", encoding='utf-8-sig') as file:
        # "\n표시 없이 데이터를 한줄씩 리스트로 읽음"
        sample = file.read().splitlines()

        for sample_item in sample:
            predict_answer, predict_value = evaluation_predict(sample_item)
            tmp_data.append([sample_item, predict_answer, round(float(predict_value[0]), 3)])

    with open('test_result.csv', 'w', encoding='utf-8-sig', newline='') as writer_csv:

        writer = csv.writer(writer_csv, delimiter=',')

        for tmp_item in tmp_data:
            writer.writerow(tmp_item)
