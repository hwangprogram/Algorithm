#include <iostream>
#include <vector>

using namespace std;

static int N, M;
static bool arrived;
static vector<vector<int>> linked_A;
static vector<bool> visited;
void DFS(int v, int depth);

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> N >> M;
    linked_A.resize(N);
    visited.resize(N);

    int s, e;
    for (int i = 0; i < M; i++) {   // 연결 리스트 저장
        cin >> s >> e;
        linked_A[s].push_back(e);
        linked_A[e].push_back(s);
    }
    for (int i = 0; i < N; i++) {   // DFS 순회 시작
        DFS(i, 1);
        if (arrived)
            break;
    }

    cout << (arrived? 1 : 0) << '\n';

    return 0;
}

void DFS(int v, int depth) {
    if (depth == 5 || arrived) {   // 가지치기 : 깊이가 5가 되거나, 이미 도달한 상태이면 return
        arrived = true;
        return;
    }

    visited[v] = true;
    for (int i : linked_A[v]) {
        if (!visited[i]) {
            DFS(i, depth + 1);
        }
    }
    visited[v] = false;
}