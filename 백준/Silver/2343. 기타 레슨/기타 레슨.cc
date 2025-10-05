#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N, M;
    cin >> N >> M;
    vector<int> A(N);
    int start = 0, end = 0;
    for (int i = 0; i < N; ++i) {
        cin >> A[i];
        if (A[i] > start)
            start = A[i];   // 배열의 최고값을 이진탐색 시작값으로
        end += A[i];        // 배열의 마지막값을 최종 합으로
    }
    while (start <= end) {   // count가 M 이상이 되면 -> 값이 작음, count가 M보다 작거나 같으면 -> 값이 큼
        int middle = (start + end) / 2;
        int sum = 0, count = 0;

        for (int i = 0; i < N; ++i) {
            if (sum + A[i] > middle) {  // sum+A[i]값이 미들값을 넘어가는 순간 블루레이 저장불가 -> 다음 수업으로
                count++;
                sum = 0;
            }
            sum += A[i];
        }
        if (sum != 0)   // 잔여 값이 있으면 그 수업을 위한 블루레이가 추가로 필요
            count++;
        if (count > M) // 값이 작음, start = middle + 1
            start = middle + 1;
        else           // 값이 큼, end = middle - 1
            end = middle - 1;
    }
    cout << start << '\n';

    return 0;
}