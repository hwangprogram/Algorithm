#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N, M;   // N 사람수, M 도로 수
    vector<vector<pair<int, int>>> A ,reverseA;  // 연결 리스트, 역 연결 리스트
    vector<int> indegree, result;   // 진입 차수, 결과 배열

    cin >> N >> M;
    // 배열 크기 초기화
    A.resize(N+1);
    reverseA.resize(N+1);
    indegree.resize(N+1);
    result.resize(N+1);

    // 연결 리스트, 역 연결 리스트 입력 (도착 노드와 비용을 같이 넣음)
    for (int i = 0; i < M; ++i) {
        int s, e, c;
        cin >> s >> e >> c;
        A[s].emplace_back(e, c);
        reverseA[e].emplace_back(s, c);
        indegree[e]++;
    }

    // 출발 노드, 도착 노드
    int start, end;
    cin >> start >> end;

    // 위상 정렬 시작
    queue<int> q;
    q.push(start);

    while (!q.empty()) {
        int now = q.front();
        q.pop();

        for (pair<int, int> next : A[now]) {
            indegree[next.first]--;
            result[next.first] = max(result[next.first], result[now] + next.second);
            if (indegree[next.first] == 0) q.push(next.first);
        }
    }

    // 역방향 탐색
    // 핵심 아이디어 : 역방향 임계치 값이 전 노드 임계치 값 + 도로 비용이라면
    // 1분도 쉬지 않아야 하는 경로
    int road_count = 0;
    queue<int> rq;
    vector<bool> visited(N+1, false);
    rq.push(end);

    while (!rq.empty()) {
        int now = rq.front();
        rq.pop();

        for (pair<int, int> prev : reverseA[now]) {
            if (result[now] == result[prev.first] + prev.second) {
                road_count++;
                if (!visited[prev.first]) {
                    visited[prev.first] = true;
                    rq.push(prev.first);
                }
            }
        }
    }
    cout << result[end] << '\n';
    cout << road_count << '\n';

    return 0;
}