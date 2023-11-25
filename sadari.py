import random

def ladder_game(participants, results):
    """
    사다리타기 게임 구현.
    :param participants: 참가자 목록 (리스트).
    :param results: 결과 목록 (리스트). 참가자 수와 동일해야 함.
    :return: 각 참가자에 대한 결과를 담은 딕셔너리.
    """
    if len(participants) != len(results):
        return "참가자 수와 결과 수가 일치하지 않습니다."

    random.shuffle(results)
    return dict(zip(participants, results))

# 예시 참가자와 결과 목록
participants_example = ["Alice", "Bob", "Charlie", "Diana"]
results_example = ["상품1", "상품2", "상품3", "꽝"]

# 사다리타기 게임 실행
ladder_game_result = ladder_game(participants_example, results_example)
print(ladder_game_result)
