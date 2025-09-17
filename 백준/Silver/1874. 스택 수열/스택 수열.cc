#include <iostream>
#include <vector>
#include <stack>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    // N개의 수
    int N;
    cin >> N;
    // 수열 A, 정답 문자 배열 result
    vector<int> A(N, 0);
    vector<char> resultV = {};

    // 수열 입력 받기
    for (int i = 0; i < N; i++) {
        cin >> A[i];
    }

    // 스택 myStack, 자연수 num
    stack<int> myStack;
    int num = 1;
    bool result = true;
    // 수열을 순회하며 스택 연산하기
    for (int i = 0; i < N; i++) {
        // 수열의 값이 자연수값보다 크다면
        if (A[i] >= num) {
            // 자연수가 수열값이 될때까지 push, 정답에 +추가
            while (A[i] >= num) {
                myStack.push(num++);
                resultV.push_back('+');
            }
            // 자연수 == 수열값이되면 pop, 정답에 -추가
            myStack.pop();
            resultV.push_back('-');
        }
        // 수열의 값이 자연수값보다 작다면
        else {
            // 스택의 맨 위수를 pop하고 수열 값과 비교
            int top_v = myStack.top();
            myStack.pop();

            // 만약 수열값이 스택 맨 위값보다 크다면 NO
            if (top_v < A[i]) {
                cout << "NO";
                result = false;
                break;
            }
            // 아니라면 pop하기
            else {
                resultV.push_back('-');
            }
        }
    }

    if (result) {
        for (int i = 0; i < resultV.size(); i++) {
            cout << resultV[i] << "\n";
        }
    }

    return 0;
}