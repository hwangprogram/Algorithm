#include <iostream>
#include <map>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int dp0[41];
    int dp1[41];

    dp0[0] = 1, dp1[0] = 0;
    dp0[1] = 0, dp1[1] = 1;
    for (int i = 2; i < 41; i++) {
        dp0[i] = dp0[i-2] + dp0[i-1];
        dp1[i] = dp1[i-2] + dp1[i-1];
    }

    int T;
    cin >> T;
    while (T--) {
        int N;
        cin >> N;

        cout << dp0[N] << ' ' << dp1[N] << '\n';
    }

    return 0;
}