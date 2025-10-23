#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N, M;
    cin >> N >> M;
    vector<vector<int>> A;
    vector<int> indegree;
    A.resize(N+1);
    indegree.resize(N+1);

    for (int i = 0; i < M; ++i) {
        int S, E;
        cin >> S >> E;
        A[S].push_back(E);  // 연결 리스트 초기화
        indegree[E]++;      // 진입 차수 배열 데이터 저장하기
    }
    queue<int> q;   // 위상 정렬 수행

    // 진입 차수 0인 노드들을 큐에 삽입
    for (int i = 1; i <= N; ++i) {
        if (indegree[i] == 0) {
            q.push(i);
        }
    }
    while (!q.empty()) {
        int now = q.front();
        q.pop();
        cout << now << ' ';
        for (int next : A[now]) {
            indegree[next]--;
            if (indegree[next] == 0) {
                q.push(next);
            }
        }
    }

    return 0;
}