'''
트리인가?
- 간선정보를 받고 해당 케이스가 트리인지를 판별
- 루트에서 다른 노드로 가는 경로는 유일해야 함. 
'''
testCase = 0
# graph = [[] for _ in range(10)]
isBreak = 0
indegree = {}  # 들어오는 간선 개수 (0인 것이 존재하면 루트가 존재, 루트 외에 모든 노드는 다 1 이상이어야 함)
while True:
    if isBreak == -1:
        break
    buf = input().rstrip().split("  ")
    if buf[0] == "":
        continue
    for tmp in buf:
        u, v = map(int, tmp.split(" "))  # u에서 v로 가는 간선
        if u == -1 and v == -1:
            isBreak = -1
            break
        elif u == 0 and v == 0:
            # print(indegree)
            testCase += 1
            result = False  # 트리인지 아닌지를 저장
            # 트리인지 계산 & 결과 출력 & 그래프 초기화
            # indegree가 0인 값은 하나만 존재해야 함.
            cnt = 0  # indegree가 0인 개수
            cntPath = 0
            if 0 not in indegree.values():
                result = False
            else:
                for k, v in indegree.items():
                    if v == 0:
                        cnt += 1
                    if v >= 2:
                        cntPath = 1
                if cnt == 1 and cntPath == 0:  # 루트에서 다른 노드까지의 경로도 유일해야 함.
                    result = True
                if cntPath != 0:
                    result = False

            if not indegree: # 비어있어도 트리
                result = True
            
            if len(indegree) == 1:
                result = True

            if result == True:
                print("Case {} is a tree.".format(testCase))
            else:
                print("Case {} is not a tree.".format(testCase))

            # graph = [[] for _ in range(10)]  # 그래프, indgree 초기화
            indegree = {}
            continue
        else:  # 간선정보 넣어주기
            # graph[u].append(v)
            if v in indegree:
                indegree[v] += 1
            else:
                indegree[u] = 0
                indegree[v] = 1
