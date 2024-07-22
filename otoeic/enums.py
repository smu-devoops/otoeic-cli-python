from enum import Enum


class WordType(Enum):
    NOUN = 1  # 명사
    VERB = 2  # 동사
    ADJECTIVE = 3  # 형용사
    ADVERB = 4  # 부사
    PRONOUN = 5  # 대명사
    PREPOSITION = 6  # 전치사
    CONJUNCTION = 7  # 접속사
    INTERJECTION = 8  # 감탄사
    DETERMINER = 9  # 한정사
    NUMERAL = 10  # 수사
    PARTICLE = 11  # 조사
    ARTICLE = 12  # 관사
    MODAL = 13  # 조동사
    PHRASAL_VERB = 14  # 구동사
    IDIOM = 15  # 관용구


class WordLevel(Enum):
    """
    TODO: 코파일럿이 추천해준 아래의 5단계는 어떤지 토론해볼 것

    BASIC = 1  # 초급
    INTERMEDIATE = 2  # 중급
    ADVANCED = 3  # 고급
    PROFESSIONAL = 4  # 전문가
    NATIVE = 5  # 원어민
    """
    EASY = 1  # 쉬움
    NORMAL = 2  # 보통
    HARD = 3  # 어려움
    VERY_HARD = 4  # 매우 어려움
