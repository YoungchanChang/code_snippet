def has_coda(word):
    """문자열 받침 여부 확인
    :param word: 문자열
    :return: True 받침 없음, False 받침 있음
    """
    return (ord(word[-1]) - 44032) % 28 == 0


def josa_change(entity, hint_item):
    """엔티티에 맞는 조사를 찾아 문장을 변경하는 함수"""
    if entity is None:
        return hint_item
    josa_sbj = "가" if has_coda(entity) else "이"
    josa_obj = "를" if has_coda(entity) else "을"
    josa_together = "와" if has_coda(entity) else "과"
    josa_sbj_action = "는" if has_coda(entity) else "은"
    hint_item = hint_item.replace("{entity}", entity)
    hint_item = hint_item.replace("{josa_sbj}", josa_sbj)
    hint_item = hint_item.replace("{josa_obj}", josa_obj)
    hint_item = hint_item.replace("{josa_together}", josa_together)
    hint_item = hint_item.replace("{josa_sbj_action}", josa_sbj_action)

    return hint_item


def contains(pattern, pattern_contain_list):
    """토큰에서 다른 토큰이 포함되어 있는지 확인"""
    for i in range(len(pattern_contain_list) - len(pattern) + 1):
        for j in range(len(pattern)):
            if pattern_contain_list[i + j] != pattern[j]:
                break
        else:
            # i와 i + len(small)
            return i, i + len(pattern)
    return False


NO_JONGSUNG = 'ᴕ'

CHOSUNGS = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
JOONGSUNGS = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']
JONGSUNGS = [NO_JONGSUNG, 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ',
             'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

N_CHOSUNGS = 19
N_JOONGSUNGS = 21
N_JONGSUNGS = 28

FIRST_HANGUL = 0xAC00  # '가'
LAST_HANGUL = 0xD7A3  # '힣'


def to_jaso(s):
    result = []
    for c in s:
        if ord(c) < FIRST_HANGUL or ord(c) > LAST_HANGUL:  # if a character is a hangul
            result.append(c)
        else:
            code = ord(c) - FIRST_HANGUL
            jongsung_index = code % N_JONGSUNGS
            code //= N_JONGSUNGS
            joongsung_index = code % N_JOONGSUNGS
            code //= N_JOONGSUNGS
            chosung_index = code

            result.append(CHOSUNGS[chosung_index])
            result.append(JOONGSUNGS[joongsung_index])
            result.append(JONGSUNGS[jongsung_index])

    return ''.join(result)


if __name__ == "__main__":
    print(to_jaso("호잉루"))
    jason_token = to_jaso("호잉루")
    print(jason_token)
    print(to_jaso("호잉루"))
    small = "동해물".split()
    big = "동해물 과 백두산이".split()
    print(small, big)
    print(contains(small, big))