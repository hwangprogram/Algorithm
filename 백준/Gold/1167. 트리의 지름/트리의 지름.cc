#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

static vector<vector<pair<int, int>>> linked_A;    // 연결 리스트
static vector<bool> visited;
static vector<int> route;
static int far_node, max_v = 0;
void BFS(int v);

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int V;  // 정점 갯수
    cin >> V;
    linked_A.resize(V+1);
    visited.resize(V+1);
    route.resize(V+1);

    for (int i = 1; i <= V; i++) {  // 연결리스트 채우기
        int s, e, cost;
        cin >> s;
        while (true) {
            cin >> e;
            if (e == -1) break;
            cin >> cost;
            linked_A[s].push_back({e, cost});
        }
    }

    // 1) 임의의 점점(1)에서 가장 먼 정점 찾기
    fill(visited.begin(), visited.end(), false);
    fill(route.begin(), route.end(), 0);
    BFS(1);

    max_v = 0;
    for (int i = 1; i <= V; i++) {
        if (route[i] > max_v) {
            max_v = route[i];
            far_node = i;
        }
    }

    // 2) far_node에서 다시 BFS해서 지름 길이 구하기
    fill(visited.begin(), visited.end(), false);
    fill(route.begin(), route.end(), 0);
    BFS(far_node);

    max_v = 0;
    for (int i = 1; i <= V; i++) {
        if (route[i] > max_v) max_v = route[i];
    }

    cout << max_v << '\n';
    return 0;
}

void BFS(int v) {
    queue<pair<int, int>> q;
    q.push({v, 0});
    visited[v] = true;
    route[v] = 0;

    while (!q.empty()) {
        pair<int, int> current = q.front();
        q.pop();
        int node = current.first;
        int dist = current.second;

        for (auto &edge : linked_A[node]) {
            int next = edge.first;
            int w = edge.second;
            if (visited[next]) continue;
            visited[next] = true;
            route[next] = dist + w;
            q.push({next, route[next]});
        }
    }
}