#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N, K;   // 배열 크기 N, 구하려는 순서의 수 K
    cin >> N >> K;
    int start = 1, end = K, ans = 0;

    while (start <= end) {
        int middle = (start + end) / 2;
        int cnt = 0;

        for (int i = 1; i <= N; ++i) {
            cnt += min(middle / i, N);
        }
        if (cnt < K)    // cnt값 (중앙값보다 작거나 같은 값이 K보다 작다면 -> 정답값이 중앙값보다 큰것)
            start = middle + 1;
        else {          // 중앙값보다 작거나 같은 같이 K보다 크거나 같다면 -> 정답값이 중앙값이거나 그보다 작은값
            ans = middle;
            end = middle - 1;
        }
    }
    cout << ans << '\n';

    return 0;
}