#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N;  // 수의 수 N
    cin >> N;

    vector<pair<int, int>> A(N);  // 수열 A
    // 수열, 인덱스값 입력 (first: 수열값, second: 인덱스값)
    for (int i = 0; i < N; i++) {
        cin >> A[i].first;
        A[i].second = i;
    }
    // sort 함수 이용하여 정렬
    sort(A.begin(), A.end());

    // 순열 순회하며 이동 최대값 찾기
    int max_v = 0;
    for (int i = 0; i < N; i++) {
        int diff = A[i].second  - i;    // 바뀐값 - 원래값
        if (diff + 1 > max_v)
            max_v = diff + 1;   // 정렬된 후에도 한번 더 실행되기 때문에 +1
    }
    cout << max_v << '\n';

    return 0;
}