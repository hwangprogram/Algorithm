#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;
void BFS(int node);
vector<vector<int>> A;
vector<int> visited;
bool isdiv;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int K; // 테스트케이스
    cin >> K;
    for (int k = 0; k < K; ++k) {
        int V, E;   // 노드 V, 간선 E
        cin >> V >> E;
        A.clear();
        A.resize(V+1);
        visited.resize(V+1);
        visited.assign(V+1, 0);
        for (int i = 0; i < E; ++i) {
            int u, v;
            cin >> u >> v;
            A[u].push_back(v);
            A[v].push_back(u);
        }
        isdiv = true;
        for (int i = 1; i <= V; ++i) {
            if (visited[i] == 0)
                BFS(i);
        }
        if (isdiv) cout << "YES\n";
        else cout << "NO\n";
    }

    return 0;
}

void BFS(int node) {
    queue<int> q;
    q.push(node);
    visited[node] = -1;     // -1부터 시작

    while (!q.empty()) {
        int now = q.front();
        q.pop();

        for (int next : A[now]) {
            if (visited[next] == 0) {   // 방문한적 없다면
                visited[next] = (visited[now] == -1 ? 1 : -1);
                q.push(next);
            }
            else if (visited[next] == visited[now]) {   // 방문했는데, 인접노드끼리 색이 같으면
                isdiv = false;
                return;
            }
        }
    }
}