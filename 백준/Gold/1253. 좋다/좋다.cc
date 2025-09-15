#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    // 수의 개수 N
    int N;
    cin >> N;
    // 배열 A
    vector<long> A(N, 0) ;

    // 배열 입력
    for (int i = 0; i < N; i++) {
        cin >> A[i];
    }
    sort(A.begin(), A.end());   // 배열 정렬
    int count = 0;  // 카운트
    // 배열 순회하며 투포인터 연산 실행
    for (int k = 0; k < N; k++) {
        // 찾을 값 find
        long find = A[k];
        int i = 0, j = N - 1;
        while (i < j) {
            long sum = A[i] + A[j];
            // sum이 찾는 값이라면, i, j가 k값과 같지 않으면 카운트
            // i가 k와 같다면 i++, j가 k와 같다면 j--
            if (sum == find) {
                if (i != k && j != k) {
                    count++;
                    break;
                }
                else if (i == k)
                    i++;
                else if (j == k)
                    j--;
            }
            // sum이 찾는 값 보다 크다면, j--
            else if (sum > find)
                j--;
            // sum이 찾는 값 보다 작다면, i++
            else if (sum < find)
                i++;
        }
    }
    cout << count << "\n";

    return 0;
}