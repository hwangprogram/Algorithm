#include <iostream>
#include <climits>

using namespace std;

static int N, M;
static long mdistance[101][101];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> N >> M;

    for (int i = 1; i <= N; ++i) {  // 인접 행렬 초기화
        for (int j = 1; j <= N; ++j) {
            if (i == j) mdistance[i][j] = 0;
            else mdistance[i][j] = INT_MAX;  // 충분히 큰 수로 저장
        }
    }
    for (int i = 0; i < M; ++i) {
        int s, e, v;
        cin >> s >> e >> v;
        if (mdistance[s][e] > v) {
            mdistance[s][e] = v;
        }
    }
    for (int k = 1; k <= N; ++k) {  // 플로이드 워셜 알고리즘 수행
        for (int i = 1; i <= N; ++i) {
            for (int j = 1; j <= N; ++j) {
                if (mdistance[i][j] > mdistance[i][k] + mdistance[k][j]) {
                    mdistance[i][j] = mdistance[i][k] + mdistance[k][j];
                }
            }
        }
    }
    for (int i = 1; i <= N; ++i) {
        for (int j = 1; j <= N; ++j) {
            string end;
            if (j == N) end = "";
            else end = " ";

            if (mdistance[i][j] == INT_MAX) cout << 0 << end;
            else cout << mdistance[i][j] << end;
        }
        cout << '\n';
    }

    return 0;
}