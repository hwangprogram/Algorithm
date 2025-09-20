#include <iostream>
#include <queue>

using namespace std;

struct compare {
    // 우선순위 큐에 사용될 순위 조건
    bool operator()(int o1, int o2) {
        int first_obj = abs(o1);
        int second_obj = abs(o2);

        if (first_obj == second_obj)
            return o1 > o2;
        else
            return first_obj > second_obj;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N;  // 요청 개수
    cin >> N;
    priority_queue<int, vector<int>, compare> myQueue;  // 우선순위 큐 (자료형, 구조체, 비교 함수명

    for (int i = 0; i < N; i++) {
        int number;
        cin >> number;

        // number가 0이면 탑 값 출력, 큐가 비었으면 0 출력
        if (number == 0) {
            if (myQueue.empty())
                cout << "0\n";
            else {
                cout << myQueue.top() << "\n";
                myQueue.pop();
            }
        }
        // number가 다른 값이면 우선순위 큐에 집어넣기
        else
            myQueue.push(number);
    }

    return 0;
}