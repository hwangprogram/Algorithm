#include <iostream>
#include <queue>
#include <vector>

using namespace std;

void union_func(int a, int b);
int find(int a);
static vector<int> parent;

typedef struct Edge {   // 에지 정보 구조체 생성, 가중치 값 기준 오름차순 정렬로 설정
    int s, e, v;
    bool operator > (const Edge& temp) const {
        return v > temp.v;
    }
} Edge;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N, M;
    cin >> N >> M;
    priority_queue<Edge, vector<Edge>, greater<Edge>> pq;   // 오름차순 정렬
    parent.resize(N+1);

    for (int i = 0; i <= N; ++i) {
        parent[i] = i;
    }
    for (int i = 0; i < M; ++i) {
        int s, e, v;
        cin >> s >> e >> v;
        pq.push(Edge{s, e, v});
    }

    int useEdge = 0;
    int result = 0;

    while (useEdge < N - 1) {
        Edge now = pq.top();
        pq.pop();
        // 같은 부모가 아니라면 > 연결해도 사이클이 생기지 않는다면
        if (find(now.s) != find(now.e)) {
            union_func(now.s, now.e);
            result += now.v;
            useEdge++;
        }
    }
    cout << result;

    return 0;
}

int find(int a) {
    if (parent[a] == a) {
        return a;
    }
    return parent[a] = find(parent[a]);
}

void union_func(int a, int b) {
    a = find(a);
    b = find(b);
    if (a != b) {
        parent[b] = a;
    }
}