#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N;  // 건물 수
    cin >> N;
    vector<vector<int>> A(N+1);  // 연결 리스트
    vector<int> indegree(N+1);   // 진입 차수 배열
    vector<int> time(N+1);       // 소요되는 시간, 시간 합

    for (int i = 1; i <= N; ++i) {
        cin >> time[i];
        while (true) {    // -1이 나올 때 까지 입력받음
            int node;
            cin >> node;

            if (node == -1) break;
            A[node].push_back(i);
            indegree[i]++;
        }
    }

    queue<int> q;   // 위상 정렬 시작
    for (int i = 1; i <= N; ++i) {  // 진입 차수가 0인 노드 큐에 집어넣기
        if (indegree[i] == 0) q.push(i);
    }

    vector<int> result(N+1);

    while (!q.empty()) {
        int now = q.front();
        q.pop();
        for (int next : A[now]) {
            indegree[next]--;   // 타깃 진입 차수 감소
            // 계산 한 후의 결과값과, 새로 계산하는 값 중 큰 값을 결과값으로
            result[next] = max(result[next], result[now] + time[now]);
            if (indegree[next] == 0) q.push(next);
        }
    }
    for (int i = 1; i <= N; ++i) {
        cout << result[i] + time[i] << '\n';
    }

    return 0;
}