#include <iostream>
#include <climits>
#include <vector>

using namespace std;

static int N;
static long mdistance[101][101];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> N;

    for (int i = 1; i <= N; ++i) {      // 배열 정보 입력
        for (int j = 1; j <= N; ++j) {
            cin >> mdistance[i][j];
        }
    }

    for (int k = 1; k <= N; ++k) {
        for (int i = 1; i <= N; ++i) {
            for (int j = 1; j <= N; ++j) {
                if (mdistance[i][k] == 1 && mdistance[k][j] == 1) {
                    mdistance[i][j] = 1;
                }
            }
        }
    }

    for (int i = 1; i <= N; ++i) {
        for (int j = 1; j <= N; ++j) {
            string end;
            if (j == N) end = "";
            else end = " ";

            cout << mdistance[i][j] << end;
        }
        cout << '\n';
    }

    return 0;
}