#include <iostream>
#include <queue>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    typedef pair<int, int> edge;
    vector<vector<edge>> A;
    // 방문을 횟수로 기록 (여러번 방문해야 하기 때문)
    vector<int> visited;
    // 거릿값을 우선순위 큐로 저장
    vector<vector<int>> distance;

    int N, M, K;
    cin >> N >> M >> K;
    // 배열들 크기 지정
    A.resize(N+1);
    visited.resize(N+1, 0);
    distance.resize(N+1);

    // 연결 리스트 입력
    for (int i = 0; i < M; ++i) {
        int s, e, w;
        cin >> s >> e >> w;
        A[s].emplace_back(w, e);
    }

    // 순회하며 루트별 값을 넣기
    priority_queue<edge, vector<edge>, greater<>> pq;
    pq.emplace(0, 1);    // 시작노드 1;
    distance[1].push_back(0);

    while (!pq.empty()) {
        int now = pq.top().second, now_dist = pq.top().first;
        pq.pop();

        if (visited[now] < K) {
            visited[now]++;     // 방문횟수 추가

            for (edge nextNode : A[now]) {
                int next = nextNode.second, next_dist = nextNode.first;
                int new_dist = now_dist + next_dist;
                distance[next].push_back(new_dist);
                pq.emplace(new_dist, next);
            }
        }
    }

    for (int i = 1; i <= N; ++i) {
        sort(distance[i].begin(), distance[i].end());
        try {
            cout << distance[i].at(K-1) << '\n';
        } catch (std::out_of_range) {
            cout << -1 << '\n';
        }
    }

    return 0;
}