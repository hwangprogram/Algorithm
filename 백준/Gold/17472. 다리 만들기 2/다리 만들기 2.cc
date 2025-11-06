#include <iostream>
#include <queue>
#include <vector>

using namespace std;

void munion(int a, int b);
int find(int a);
void BFS(int i, int j);

static int dr[] = {-1, 0, 1, 0};
static int dc[] = {0, 1, 0, -1};
static int map[101][101];
static int visited[101][101] = {false, };
static vector<int> parent;
static int N, M, sNum;
static vector<vector<pair<int, int>>> sumlist;
static vector<pair<int, int>> mlist;

typedef struct Edge {   // 에지 정보 구조체 생성, 가중치 값 기준 오름차순 정렬로 설정
    int s, e, v;
    bool operator > (const Edge& temp) const {
        return v > temp.v;
    }
} Edge;

static priority_queue<Edge, vector<Edge>, greater<Edge>> pq;    // 오름차순 정렬

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> N >> M;

    for (int i = 0;i < N; ++i) {
        for (int j = 0; j < M; ++j) {
            cin >> map[i][j];   // 맵 정보 저장
        }
    }

    sNum = 1;

    // 각 자리에서 BFS탐색을 이용하여 섬 분리
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < M; ++j) {
            if (map[i][j] != 0 && visited[i][j] != true) {
                BFS(i, j);
                sNum++;
                sumlist.push_back(mlist);
            }
        }
    }

    // 섬의 각 지점에서 만들 수 있는 모든 에지를 저장
    for (int i = 0; i < sumlist.size(); ++i) {
        vector<pair<int, int>> now = sumlist[i];

        for (int j = 0; j < now.size(); ++j) {
            int r = now[j].first;
            int c = now[j].second;
            int now_S = map[r][c];

            for (int d = 0; d < 4; ++d) {
                int nr = r;
                int nc = c;
                int blength = 0;

                while (true) {
                    nr += dr[d];
                    nc += dc[d];

                    if (nr < 0 || nr >= N || nc < 0 || nc >= M) break;

                    if (map[nr][nc] == now_S) break; // 같은 섬이면 X
                    else if (map[nr][nc] != 0) {
                        if (blength > 1) {
                            pq.push(Edge{now_S, map[nr][nc], blength});
                        }
                        break;
                    } else {
                        blength++;
                    }
                }
            }

        }
    }

    parent.resize(sNum);

    for (int i = 0; i < parent.size(); ++i) {
        parent[i] = i;
    }

    int useEdge = 0;
    int result = 0;

    while (!pq.empty()) {   // 최소 신장 트리 알고리즘 수행
        Edge now = pq.top();
        pq.pop();
        if (find(now.s) != find(now.e)) {   // 같은 부모가 아니라면 -> 연결 가능
            munion(now.s, now.e);
            result = result + now.v;
            useEdge++;
        }
    }
    // 배열에서 쉽게 index를 처리하고자 sNum을 1부터 시작하였으므로
    // 현재 sNum의 값이 섬의 개수보다 1 많은 상태
    // 그러므로 1 작은 수가 아닌 2 작은 수와 사용 에지 비교
    if (useEdge == sNum - 2) {
        cout << result << '\n';
    }
    else {
        cout << -1 << '\n';
    }

    return 0;
}

void munion(int a, int b) {
    a = find(a);
    b = find(b);
    if (a != b) {
        parent[b] = a;
    }
}

int find(int a) {
    if (a == parent[a]) {
        return a;
    }
    return parent[a] = find(parent[a]);
}

void BFS(int i, int j) {    // BFS를 통해 연결된 섬 찾기
    queue<pair<int, int>> myqueue;
    mlist.clear();
    myqueue.emplace(i, j);
    mlist.emplace_back(i, j);
    visited[i][j] = true;
    map[i][j] = sNum;

    while (!myqueue.empty()) {
        int r = myqueue.front().first;
        int c = myqueue.front().second;
        myqueue.pop();

        for (int d = 0; d < 4; ++d) {
            int nr = r + dr[d];
            int nc = c + dc[d];

            if (nr < 0 || nr >= N || nc < 0 || nc >= M) continue;
            if (!visited[nr][nc] && map[nr][nc] != 0) {
                visited[nr][nc] = true;
                map[nr][nc] = sNum;
                mlist.emplace_back(nr, nc);
                myqueue.emplace(nr, nc);
            }
        }
    }
}