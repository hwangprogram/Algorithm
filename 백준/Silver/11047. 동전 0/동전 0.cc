#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    // 동전 종류 N, 맞춰야 할 합 K
    int N, K;
    cin >> N >> K;

    // 동전들 수열 coins
    vector<int> coins(N, 0);
    for (int i = 0; i < N; i++) {
        cin >> coins[i];
    }
    // 정담 ans
    int ans = 0;

    // coins를 뒤에서부터 순회하며 남은 값이 동전값보다 크다면 빼가는 식으로 반복
    for (int i = N - 1; i >= 0; i--) {
        // K 값이 coin보다 큰지 확인
        if (coins[i] <= K) {
            // 크다면, 큰 동전에서 가능한 만큼 빼기
            while (coins[i] <= K) {
                K -= coins[i];
                ans++;
            }
        }
    }

    cout << ans;

    return 0;
}