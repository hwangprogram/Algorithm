#include <iostream>
#include <vector>
#include <stack>
#include <cmath>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    long N;  // GCD 개수 구하려는 수
    cin >> N;
    long result = N;
    for (long i = 2; i <= sqrt(N); ++i) {
        if (N % i == 0) {   // i가 소인수인지 확인
            result = result - result / i;   // 결과값 업데이트
            // 해당 소인수 지우기
            while (N % i == 0) {
                N /= i;
            }
        }
    }
    if (N > 1) {    // 아직 소인수 구성이 남아있는 경우
        result = result - result / N;
    }
    cout << result << '\n';

    return 0;
}