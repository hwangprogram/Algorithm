#include <iostream>
#include <queue>
#include <climits>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    typedef pair<int, int> node;
    vector<vector<node>> A;
    vector<int> distance;

    int N, M;   // 도시 수 N, 버스 개수 M
    cin >> N >> M;
    // 배열들 크기 초기화
    A.resize(N+1);
    distance.resize(N+1, INT_MAX);

    // 연결 리스트 입력
    for (int i = 0; i < M; ++i) {
        int s, e, c;
        cin >> s >> e >> c;
        A[s].emplace_back(c, e);
    }

    // 출발 도시, 도착 도시 입력
    int start, end;
    cin >> start >> end;

    // 출발 도시로부터 탐색 시작
    priority_queue<node, vector<node>, greater<>> pq;
    pq.emplace(0, start);
    distance[start] = 0;

    while (!pq.empty()) {
        int now = pq.top().second, now_dist = pq.top().first;
        pq.pop();

        // 이미 처리된 노드 스킵
        if (now_dist > distance[now]) continue;

        for (node next : A[now]) {
            int next_node = next.second, weight = next.first;

            // 다음 노드의 distance 값보다 현재 노드 + 가중치 값이 더 작으면 업데이트
            if (distance[next_node] > distance[now] + weight) {
                distance[next_node] = distance[now] + weight;
                // 갱신된 노드를 새로운 거리와 함께 큐에 삽입
                pq.emplace(distance[next_node], next_node);
            }
        }
    }
    cout << distance[end] << '\n';

    return 0;
}