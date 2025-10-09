#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    // 에라토스테네스의 체 구현
    vector<int> A(1000001);
    for (int i = 2; i < 1000001; ++i) {
        A[i] = i;
    }
    for (int i = 2; i < sqrt(1000001); ++i) {
        if (A[i] == 0)
            continue;
        for (int j = i + i; j < 1000001; j = j + i) {
            A[j] = 0;
        }
    }

    int M, N;
    cin >> M >> N;
    for (int i = M; i <= N; i++) {
        if (A[i] == 0)
            continue;
        cout << A[i] << '\n';
    }

    return 0;
}