#include <iostream>
#include <vector>
#include <cmath>
#include <climits>
using namespace std;

#define MOD 1000000007

static vector<long> tree;
static vector<long> copyTree;
long long multipleTree(int s, int e);
void changeTree(int index, int value);
void setTree(int n);

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N, M, K;    // 수 N개, 수의 변경 M회, 구간 곱 K회
    cin >> N >> M >> K;

    // 트리 깊이 구하기
    int treeHeight = 0;
    int temp = N;

    while (temp != 0) {
        treeHeight++;
        temp /= 2;
    }

    // 트리 사이즈, 시작 인덱스 구하기, 값 넣기, 트리 초기화하기
    int treeSize = int(pow(2, treeHeight + 1));
    int startIndex = treeSize / 2 - 1;
    tree.resize(treeSize + 1);
    std::fill(tree.begin(), tree.end(), 1);
    for (int i = startIndex + 1; i <= startIndex + N; ++i) {
        cin >> tree[i];
    }
    setTree(treeSize - 1);

    // 값 변경 or 구간 곱 출력하기
    for (int i = 0; i < M + K; ++i) {
        int o, s, e;
        cin >> o >> s >> e;

        // o가 1일 경우 값 변경
        if (o == 1) {
            changeTree(s + startIndex, e);
        }
        // o가 2일 경우 구간 곱 출력
        else if (o == 2) {
            cout << multipleTree(s + startIndex, e + startIndex) << '\n';
        }
    }

    return 0;
}

void setTree(int n) {
    while (n != 1) {
        tree[n / 2] = (tree[n / 2] * tree[n]) % MOD;
        n--;
    }
}

void changeTree(int index, const int value) {
    tree[index] = value;
    index /= 2;

    while (index > 0) {
        tree[index] = (tree[index * 2] * tree[index * 2 + 1]) % MOD;
        index /= 2;
    }
}

long long multipleTree(int s, int e) {
    long long result = 1;

    while (s <= e) {
        if (s % 2 == 1) result = (result *= tree[s]) % MOD;
        if (e % 2 == 0) result = (result *= tree[e]) % MOD;
        // 부모 트리로
        s = (s + 1) / 2;
        e = (e - 1) / 2;
    }
    return result;
}