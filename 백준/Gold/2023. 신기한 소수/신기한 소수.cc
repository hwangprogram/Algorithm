#include <iostream>
#include <vector>

using namespace std;

void DFS(int val, int jarisu);
bool isPrime(int num);
static int N;   // 자릿수 N

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> N;
    DFS(2, 1);
    DFS(3, 1);
    DFS(5, 1);
    DFS(7, 1);

    return 0;
}

void DFS(int val, int jarisu) {
    if (jarisu == N) {  // 기저조건 : 자리수가 N이 되었을 때
        if (isPrime(val)) {
            cout << val << '\n';
        }
        return;
    }

    for (int i = 1; i < 10; i++) {
        if (i % 2 == 0) // i가 짝수일때 넘어감 : 마지막 수가 짝수라면 소수가 아니기 때문
            continue;
        if (isPrime(val * 10 + i)) {    // 소수이면 재귀로 자릿수를 늘림
            DFS(val * 10 + i, jarisu + 1);
        }
    }
}

// 소수 판별 함수
bool isPrime(int num) {
    for (int i = 2; i <= num / 2; i++) {
        if (num % i == 0)
            return false;
    }
    return true;
}