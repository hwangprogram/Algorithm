#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N;  // 수의 수 N
    cin >> N;

    vector<int> A(N, 0);  // 수열 A
    // 수열 입력
    for (int i = 0; i < N; i++) {
        cin >> A[i];
    }

    // 정렬하기 (버블 정렬)
    int last_num = A.size();    // 정렬할 위치
    while (last_num > 0) {
        for (int i = 0; i < last_num - 1; i++) {
            // 앞의 값이 더 크면 앞의값을 뒤로 이동
            if (A[i] > A[i+1]) {
                int temp = A[i];
                A[i] = A[i+1];
                A[i+1] = temp;
            }
        }
        last_num--;
    }
    for (int i = 0; i < N; i++) {
        cout << A[i] << "\n";
    }

    return 0;
}