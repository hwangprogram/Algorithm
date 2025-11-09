#include <iostream>
using namespace std;

static int T, N, M;
static int D[31][31];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    for (int i = 0; i <= 30; ++i) {
        D[i][1] = i; // i개중 1개 선택 : i
        D[i][0] = 1; // i개중 0개 선택 : 1
        D[i][i] = 1; // i개중 i개 선택 : 1
    }
    for (int i = 2; i <= 30; ++i) {
        for (int j = 1; j <= i; ++j) {
            // i에서 j개 고르는 경우의 수 :
            // i-1개 중 j개 고르는 수 (i번째 수를 고르지 않는 경우)
            // i-1개 중 j-1개 고르는 수 (i번째 수를 고르는 경우)
            D[i][j] = D[i-1][j] + D[i-1][j-1];
        }
    }

    cin >> T;
    for (int i = 0; i < T; ++i) {
        cin >> N >> M;
        cout << D[M][N] << '\n';
    }

    return 0;
}