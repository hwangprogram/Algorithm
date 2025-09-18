#include <iostream>
#include <vector>
#include <stack>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N;  // N개의 수열
    cin >> N;
    vector<int> A(N, 0), ansA(N, 0);    // 수열 A, 정답수열 ansA;
    stack<int> myStack;

    // 수열 입력
    for (int i = 0; i < N; i++) {
        cin >> A[i];
    }

    // 배열 순회하며 스택 연산
    for (int i = 0; i < N; i++) {
        // 스택이 비지 않았고, 지금 들어오려는 값이 스택 맨 위값보다 크다면
        while (!myStack.empty() && A[myStack.top()] < A[i]) {
            // 정답배열에 오큰수 저장
            ansA[myStack.top()] = A[i];
            myStack.pop();
        }
        // 스택이 비었거나 지금값이 스택 맨 위값보다 작다면
        myStack.push(i);
    }

    // 스택에 남은 값이 있으면 다 빼주고 해당 인덱스의 정답 배열 값을 -1로
    while (!myStack.empty()) {
        ansA[myStack.top()] = -1;
        myStack.pop();
    }

    // 정답 출력
    for (int i = 0; i < N; i++)
        cout << ansA[i] << " ";

    return 0;
}