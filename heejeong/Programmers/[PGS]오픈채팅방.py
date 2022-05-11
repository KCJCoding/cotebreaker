'''
[0] : Enter/Change/Leave
[1] : User ID
[2] : 닉네임
'''


def solution(record):
    answer = []  # 최종 결과를 담는 리스트
    info = []  # record 공백으로 구분
    visitList = {}

    for i in range(len(record)):  # [i][0]: 변화 [i][1]: 유저아이디 [i][2]: 닉네임
        info.append(list(map(str, record[i].split(' '))))
        if info[i][0] == 'Enter':
            visitList[info[i][1]] = info[i][2]
            answer.append([info[i][1], "님이 들어왔습니다."])
        elif info[i][0] == 'Leave':
            answer.append([info[i][1], "님이 나갔습니다."])
        else:
            visitList[info[i][1]] = info[i][2]

    final_answer = []
    for s in answer:
        final_answer.append(visitList[s[0]]+s[1])  # 딕셔너리이기 때문에 s[0]이 key로 사용됨.

    return final_answer


record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo",
          "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]
# result = ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]

print(solution(record))
