#include <iostream>
using namespace std;

static int T, N, K;
static int D[15][15];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    for (int i = 1; i <= 14; ++i) {
        D[0][i] = i;    // 0층 초기화
        D[i][1] = 1;    // 1호 초기화
    }
    for (int i = 1; i <= 14; ++i) {
        for (int j = 2; j <= 14; ++j) {
            D[i][j] = D[i][j - 1] + D[i - 1][j];    // 같은층 전 호 + 바로 밑의 층만 계산하면됨
        }
    }

    cin >> T;
    for (int i = 0; i < T; ++i) {
        cin >> K >> N;
        cout << D[K][N] << '\n';
    }

    return 0;
}