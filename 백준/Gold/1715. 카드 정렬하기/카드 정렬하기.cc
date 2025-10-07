#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N, ans = 0;
    cin >> N;
    priority_queue<int, vector<int>, greater<int>> pq;
    for (int i = 0; i < N; ++i) {
        int temp;
        cin >> temp;
        pq.push(temp);
    }
    while (pq.size() != 1) {
        int num1 = pq.top();
        pq.pop();
        int num2 = pq.top();
        pq.pop();
        ans += num1 + num2;
        pq.push(num1+num2);
    }
    cout << ans << '\n';

    return 0;
}