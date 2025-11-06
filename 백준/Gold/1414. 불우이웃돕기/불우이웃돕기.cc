#include <iostream>
#include <queue>
#include <vector>

using namespace std;

void munion(int a, int b);
int find(int a);

typedef struct Edge {
    int s, e, v;
    bool operator > (const Edge& temp) const {
        return v > temp.v;
    }
} Edge;

static int N, sum = 0;
static vector<int> parents;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> N;
    cin.ignore();
    priority_queue<Edge, vector<Edge>, greater<Edge>> pq;

    // 랜선 정보 입력받기
    for (int i = 0; i < N; ++i) {
        string line;
        cin >> line;

        for (int j = 0; j < N; ++j) {
            int temp = 0;
            if (line[j] >= 'a' && line[j] <= 'z') {
                temp = line[j] - 'a' + 1;
            }
            else if (line[j] >= 'A' && line[j] <= 'Z') {
                temp = line[j] - 'A' + 27;
            }
            sum += temp;    // 모든 랜선 길이 저장

            if (i != j && temp != 0) {
                pq.push(Edge{i, j, temp});
            }
        }
    }

    parents.resize(N);

    for (int i = 0; i < N; ++i) {
        parents[i] = i;
    }

    int useEdge = 0, result = 0;

    while (!pq.empty()) {
        Edge now = pq.top();
        pq.pop();
        // 같은 부모가 아니라면 -> 연결해도 사이클 생기지 않는다면
        if (find(now.s) != find(now.e)) {
            munion(now.s, now.e);
            result += now.v;
            useEdge++;
        }
    }
    if (useEdge == N - 1) {
        cout << sum - result << '\n';
    }
    else {
        cout << "-1\n";
    }

    return 0;
}

int find(int a) {
    if (parents[a] == a) {
        return a;
    }
    return parents[a] = find(parents[a]);
}

void munion(int a, int b) {
    a = find(a);
    b = find(b);
    if (a != b) {
        parents[b] = a;
    }
}