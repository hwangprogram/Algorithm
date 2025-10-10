#include <iostream>
#include <vector>
#include <stack>
#include <cmath>

using namespace std;
bool palindrom(int v);

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    // 에라토스테네스의 체
    vector<int> A(1003002);
    A[0] = 0, A[1] = 0;
    for (int i = 2; i < 1003002; ++i) {
        A[i] = i;
    }
    for (int i = 2; i <= sqrt(1003002); ++i) {
        if (A[i] == 0)
            continue;
        for (int j = i + i; j < 1003002; j += i) {
            A[j] = 0;
        }
    }

    // N보다 큰 소수이자 팰린드롬인 수 구하기
    int N;
    cin >> N;
    for (int i = N; i < 1003002; ++i) {
        if (A[i] != 0 && palindrom(A[i])) {
            cout << A[i] << '\n';
            break;
        }
    }

    return 0;
}

bool palindrom(int v) {
    const string str_v = to_string(v);
    int left = 0, right = str_v.size() - 1;
    while (left < right) {
        if (str_v[left] != str_v[right]) return false;
        left++;
        right--;
    }
    return true;
}