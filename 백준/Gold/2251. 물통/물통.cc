#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;
void BFS();
static int from[] = {0, 0, 1, 1, 2, 2};
static int to[] = {1, 2, 0, 2, 0, 1};
bool visited[201][201];
int limit[3];
vector<int> ans;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> limit[0] >> limit[1] >> limit[2];
    BFS();
    sort(ans.begin(), ans.end());
    for (int a : ans) {
        cout << a << ' ';
    }
    cout << '\n';

    return 0;
}

void BFS() {
    queue<vector<int>> q;
    q.push({0, 0, limit[2]});    // A, B 가 0, 0 (비어있는상태)에서 시작
    visited[0][0] = true;
    ans.push_back(limit[2]);    // 이미 A가 빈 상황이므로 이때의 C값을 넣음

    while (!q.empty()) {
        vector<int> now = q.front();
        q.pop();

        // 다음 노드 탐색 로직
        // A->B, A->C, B->A, B->C, C->A, C->B 중 하나
        for (int i = 0; i < 6; ++i) {
            vector<int> next = now;
            int f = from[i], t = to[i];
            // from(물을 옮기려는 병)에 물이 없을때는 continue
            if (next[f] == 0) continue;
            // 물상황 업데이트
            next[t] += next[f];
            next[f] = 0;

            // 물통이 넘친 상황이라면
            if (next[t] > limit[t]) {
                // 넘친만큼 이전통에 넣기
                next[f] += next[t] - limit[t];
                next[t] = limit[t];
            }

            // 이 물상황에 방문하지 않았다면
            if (!visited[next[0]][next[1]]) {
                visited[next[0]][next[1]] = true;
                q.push(next);

                // 처리 진행 후 만약 첫번째 통이 빈 상황이라면
                if (next[0] == 0) {
                    ans.push_back(next[2]);  // 세번째 통의 상황을 정답 배열에
                }
            }

        }
    }
}