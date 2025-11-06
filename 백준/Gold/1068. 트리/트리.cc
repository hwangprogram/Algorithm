#include <iostream>
#include <vector>

using namespace std;

static int N, result = 0, deleteNode;
static vector<int> answer;
static vector<bool> visited;
static vector<vector<int>> tree;
void DFS(int number);

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> N;
    visited.resize(N+1);
    answer.resize(N+1);
    tree.resize(N+1);

    int root = 0;

    for (int i = 0; i < N; ++i) {
        int par;
        cin >> par;
        if (par != -1) {
            tree[i].push_back(par);
            tree[par].push_back(i);
        }
        else {
            root = i;
        }
    }
    cin >> deleteNode;

    if (deleteNode == root) {
        cout << 0 << '\n';
    }
    else {
        DFS(root);
        cout << result <<'\n';
    }

    return 0;
}

void DFS(int number) {
    visited[number] = true;
    int cNode = 0;

    for (int node : tree[number]) {
        if (!visited[node] && node != deleteNode) {   // 삭제 노드면 탐색중지
            cNode++;
            DFS(node);
        }
    }
    if (cNode == 0) {   // 자식 노드 수가 0이면 리프 노드로 간주
        result++;
    }
}