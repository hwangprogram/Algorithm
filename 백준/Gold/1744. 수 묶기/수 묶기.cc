#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N;
    cin >> N;
    vector<int> positive_A, negative_A;
    for (int i = 0; i < N; ++i) {
        int temp;
        cin >> temp;
        if (temp > 0)
            positive_A.push_back(temp);
        else
            negative_A.push_back(temp);
    }
    // 정렬
    sort(positive_A.begin(), positive_A.end(), greater<int>());
    sort(negative_A.begin(), negative_A.end());
    // 조건 분기
    // 양수 배열 -> 다음 수가 양수 중 1보다 클때만 묶는다
    // 음수 배열 -> 다음 수가 양수가 아니라면(음수나 0) 묶는다
    if (!positive_A.empty()) {
        for (int i = 0; i < positive_A.size() - 1; ++i) {
            if (positive_A[i+1] > 1) {
                positive_A[i] *= positive_A[i+1];
                positive_A[i+1] = 0;
                i++;
            }
        }
    }
    if (!negative_A.empty()) {
        for (int i = 0; i < negative_A.size() - 1; ++i) {
            if (negative_A[i+1] <= 0) {
                negative_A[i] *= negative_A[i+1];
                negative_A[i+1] = 0;
                i++;
            }
        }
    }
    int sum = 0;
    // 배열의 값 전부 더한것이 값
    for (int i : positive_A) {
        sum += i;
    }
    for (int i : negative_A) {
        sum += i;
    }
    cout << sum << '\n';

    return 0;
}