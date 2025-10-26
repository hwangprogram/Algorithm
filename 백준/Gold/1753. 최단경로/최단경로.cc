#include <iostream>
#include <queue>
#include <climits>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    vector<vector<pair<int, int>>> A;  // 연결 리스트
    vector<int> result;     // 결과 배열
    int V, E;   // 정점 V, 간선 E
    cin >> V >> E;
    int start;  // 시작 노드
    cin >> start;
    A.resize(V+1);
    result.resize(V+1, INT_MAX);
    result[start] = 0;

    // 간선 정보 입력
    for (int i = 0; i < E; ++i) {
        int u, v, w;
        cin >> u >> v >> w;
        A[u].emplace_back(v, w);
    }

    // 최단 거리 배열 완성하기
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    pq.emplace(0, start);

    while (!pq.empty()) {
        // 1. 가장 거리가 짧은 노드를 꺼냄
        int now_dist = pq.top().first;
        int now = pq.top().second;
        pq.pop();

        // 2. 이미 처리된(최종 확정된) 노드는 스킵
        if (now_dist > result[now]) {
            continue;
        }

        // 3. 현재 노드와 연결된 모든 이웃 노드 탐색
        for (pair<int, int> next : A[now]) {
            int next_node = next.first;
            int weight = next.second;

            // 현재 경로가 이웃 노드의 기존 최단 경로보다 짧으면 갱신
            if (result[now] + weight < result[next_node]) {
                result[next_node] = result[now] + weight;
                // 갱신된 노드를 새로운 거리와 함께 큐에 삽입
                pq.emplace(result[next_node], next_node);
            }
        }
    }
    for (int i = 1; i <= V; ++i) {
        if (result[i] != INT_MAX) cout << result[i] << '\n';
        else cout << "INF" << '\n';
    }

    return 0;
}