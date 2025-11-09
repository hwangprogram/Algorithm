#include <iomanip>
#include <iostream>
using namespace std;

static int M, K, T;
static int D[51];
static double probability[51];
static double ans = 0.0;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> M;
    for (int i = 0; i < M; ++i) {
        cin >> D[i];
        T += D[i];
    }
    cin >> K;

    // 같은 색깔만 K개 뽑는 방법 :
    // T개(총 개수) 중 같은 색상 D[i]를 K번만큼 뽑으면 된다
    for (int i = 0; i < M; ++i) {
        if (D[i] >= K) {
            probability[i] = 1.0;
            for (int j = 0; j < K; ++j) {
                probability[i] *= static_cast<double>(D[i] - j) / (T - j);
            }
        }
        ans += probability[i];
    }
    cout << fixed << setprecision(9);   // 오차 범위 내 출력을 위한 소수점 자릿수 설정
    cout << ans;

    return 0;
}