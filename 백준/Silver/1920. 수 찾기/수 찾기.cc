#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

bool binary_serch(const vector<int> &A, int target);

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N, M;
    vector<int> Arr;
    cin >> N;
    for (int i = 0; i < N; ++i) {
        int tmp;
        cin >> tmp;
        Arr.push_back(tmp);
    }
    sort(Arr.begin(), Arr.end());
    cin >> M;
    for (int i = 0; i < M; ++i) {
        int target_v;
        cin >> target_v;
        cout << binary_serch(Arr, target_v) << '\n';
    }

    return 0;
}

bool binary_serch(const vector<int> &A, int target) {
    int s, e;
    s = 0, e = A.size() - 1;

    while (s <= e) {
        int m = s + (e - s) / 2;    // 중앙값 탐색
        if (A[m] == target)    // 값을 찾았으면 true 리턴
            return true;
        else if (A[m] < target)   // A[m]이 타겟값보다 작다면 (오른쪽 그룸 선택)
            s = m + 1;
        else if (A[m] > target)    // A[m]이 타겟값보다 크다면 (왼쪽 그룹 선택)
            e = m - 1;
    }
    return false;
}