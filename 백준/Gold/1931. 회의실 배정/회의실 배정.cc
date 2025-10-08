#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N, ans = 0;
    cin >> N;
    vector<pair<int, int>> A;
    for (int i = 0; i < N; ++i) {
        int t1, t2;
        cin >> t1 >> t2;
        A.emplace_back(t1, t2);
    }
    // 종료시간별 오름차순으로 정렬
    sort(A.begin(), A.end(), [](const pair<int, int> &a, const pair<int, int> &b) {
        if (a.second == b.second)
            return a.first < b.first;
        return a.second < b.second;
    });

    int end_time = -1;
    for (int i = 0; i < N; ++i) {
        if (A[i].first >= end_time) {
            end_time = A[i].second;
            ans++;
        }
    }
    cout << ans << '\n';

    return 0;
}