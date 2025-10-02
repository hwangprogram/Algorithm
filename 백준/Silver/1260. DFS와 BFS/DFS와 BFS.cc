#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

static int N, M, V;
static vector<vector<int>> linked_A;
static vector<bool> dfs_visited;
static vector<bool> bfs_visited;
static vector<int> dfs_result;
static vector<int> bfs_result;
void DFS(int v);
void BFS(int v);

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> N >> M >> V;
    linked_A.resize(N+1);
    dfs_visited.resize(N+1);
    bfs_visited.resize(N+1);

    int s, e;
    for (int i = 0; i < M; i++) {   // 연결 리스트 저장
        cin >> s >> e;
        linked_A[s].push_back(e);
        linked_A[e].push_back(s);
    }
    for (int i = 1; i <= N; i++) {
        sort(linked_A[i].begin(), linked_A[i].end());
    }
    DFS(V);
    BFS(V);

    for (int i = 0; i < dfs_result.size(); i++) {
        if (i) cout << ' ';
        cout << dfs_result[i];
    }
    cout << '\n';
    for (int i = 0; i < bfs_result.size(); i++) {
        if (i) cout << ' ';
        cout << bfs_result[i];
    }

    return 0;
}

void DFS(int v) {
    dfs_visited[v] = true;
    dfs_result.push_back(v);
    for (int i : linked_A[v]) {
        if (!dfs_visited[i]) {
            DFS(i);
        }
    }
}

void BFS(int v) {
    queue<int> q;
    q.push(v);
    bfs_visited[v] = true;

    while (!q.empty()) {
        int current = q.front();
        q.pop();
        bfs_result.push_back(current);

        for (int i : linked_A[current]) {
            if (!bfs_visited[i]) {
                q.push(i);
                bfs_visited[i] = true;
            }
        }
    }
}