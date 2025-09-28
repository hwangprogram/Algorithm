#include <iostream>
#include <map>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N;
    cin >> N;
    int DP[1000001];
    DP[0] = 0, DP[1] = 0;

    for (int i = 2; i <= N; i++) {
        // 그 전 숫자의 count + 1 or 2나 3의로 나눈 숫자의 count + 1
        DP[i] = DP[i-1] + 1;

        if (i % 3 == 0) {
            DP[i] = min(DP[i],DP[i/3] + 1);
        }

        if (i % 2 == 0) {
            DP[i] = min(DP[i],DP[i/2] + 1);
        }
    }

    cout << DP[N] << '\n';

    return 0;
}