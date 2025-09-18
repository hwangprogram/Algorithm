#include <iostream>
#include <queue>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N;  // 카드 수 N
    queue<int> myQueue; // 큐

    cin >> N;
    // 순서대로 큐에 넣기
    for (int i = 1; i <= N; i++) {
        myQueue.push(i);
    }

    // 큐에 마지막 하나만 남을 때까지
    while (myQueue.size() > 1) {
        // 맨 위장 빼기 -> pop하기 (선입선출)
        myQueue.pop();
        // 다음 장 아래로 옮기기
        int top_v = myQueue.front();
        myQueue.pop();
        myQueue.push(top_v);
    }

    // 마지막 남은 값 출력
    cout << myQueue.front() << "\n";

    return 0;
}