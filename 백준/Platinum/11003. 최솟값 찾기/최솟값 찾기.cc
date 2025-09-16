#include <iostream>
#include <deque>

using namespace std;
typedef pair<int, int> Node;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    // N개의 수, 슬라이딩 윈도우 크기 L
    int N, L;
    cin >> N >> L;
    // 덱 mydeque
    deque<Node> mydeque;

    // 배열 순회하면서 최소값 확인, 출력
    for (int i = 0; i < N; i++) {
        // 들어오는 값 now
        int now;
        cin >> now;
        // 값이 들어올떄마다 정렬하지 않고
        // 현재 수보다 큰 값을 덱에서 제거
        // mydeque가 비어있지 않고, 더 작은 값이 들어왔다면 큰 값을 제거
        while (mydeque.size() && mydeque.back().first > now) {
            mydeque.pop_back();
        }
        // (값, 인덱스)
        mydeque.push_back(Node(now, i));
        // 범위에서 벗어난 값 제거
        if (mydeque.front().second < i - L + 1)
            mydeque.pop_front();

        cout << mydeque.front().first << " ";
    }

    return 0;
}