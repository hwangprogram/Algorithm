#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

static int N, M, min_route = 10000;
int A[101][101];  // 2차원 배열
int dx[4] = {1, -1, 0, 0};
int dy[4] = {0, 0, 1, -1};
void BFS(int x, int y, int count);

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> N >> M;
    for (int i = 1; i <= N; i++) {
        string line;
        cin >> line;
        for (int j = 1; j <= M; j++) {
            A[i][j] = line[j-1] - '0';    // 문자 -> 숫자 변환
        }
    }
    BFS(1, 1, 1);
    cout << min_route << '\n';

    return 0;
}

void BFS(int x, int y, int count) {
    queue<vector<int>> q;
    vector<int> temp(3);
    q.push({x, y, count});
    A[x][y] = 0;    // 방문처리

    while (!q.empty()) {
        temp = q.front();
        if (temp[0] == N && temp[1] == M) {     // N, M에 도달했을 때
            if (temp[2] < min_route) {
                min_route = temp[2];
            }
        }
        q.pop();
        for (int dir = 0; dir < 4; dir++) {
            int nx = temp[0] + dx[dir], ny = temp[1] + dy[dir];
            if (nx <= N && ny <= M && A[nx][ny] == 1) {
                q.push({nx, ny, temp[2]+1});
                A[nx][ny] = 0;  // 방문처리
            }
        }
    }
}