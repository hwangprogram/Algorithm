#include <iostream>
#include <vector>
#include <climits>
#include <tuple>

using namespace std;

static int N, S, E, M;
typedef tuple<int, int, int> edge;
static vector<edge> edges;
static vector<long> mdistance, benefits;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> N >> S >> E >> M;
    mdistance.resize(N);
    benefits.resize(N);
    std::fill(mdistance.begin(), mdistance.end(), LONG_MIN);    // 최단 거리 배열 초기화

    for (int i = 0 ; i < M; ++i) {
        int start, end, time;
        cin >> start >> end >> time;
        edges.emplace_back(start, end, time);
    }
    for (int i = 0; i < N; ++i) {
        cin >> benefits[i];
    }

    // 변형된 벨만-포드 알고리즘 수행
    mdistance[S] = benefits[S];

    // 양수 사이클이 전파되도록 충분히 큰 수로 반복하기
    for (int i = 0; i <= N + 50; ++i) {
        for (int j = 0; j < M; ++j) {
            edge medge = edges[j];
            int start = get<0>(medge);
            int end = get<1>(medge);
            int time = get<2>(medge);
            // 시작 노드가 미방문 노드이면 continue
            if (mdistance[start] == LONG_MIN) continue;
            // 시작 노드가 양수 사이클에 연결된 노드라면 종료 노드도 연결 노드로 갱신
            else if (mdistance[start] == LONG_MAX) mdistance[end] = LONG_MAX;
            // 더 많은 돈을 벌 수 있는 새로운 경로를 발견하면 새로운 경로값으로 갱신
            else if (mdistance[end] < mdistance[start] + benefits[end] - time) {
                mdistance[end] = mdistance[start] + benefits[end] - time;
                // N - 1 반복 이후 갱신되는 종료 노드는 양수 사이클 연결 노드로 변경
                if (i >= N - 1) {
                    mdistance[end] = LONG_MAX;
                }
            }
        }
    }
    if (mdistance[E] == LONG_MIN) {
        cout << "gg" << '\n';           // 도착 불가능
    }
    else if (mdistance[E] == LONG_MAX) {
        cout << "Gee" << '\n';          // 양수 사이클 연결
    }
    else {
        cout << mdistance[E] << '\n';   // 그 외 경우
    }

    return 0;
}