#include <iostream>
#include <vector>
#include <cmath>
#include <climits>
using namespace std;

static vector<long long> tree;
long long treeMin(int s, int e);    // 트리에서 최소값 찾는 함수
void setTree(int n);                // 트리 초기화 함수

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N, M;
    cin >> N >> M;

    // 트리 깊이 구하기
    int treeHeight = 0;
    int temp = N;

    while (temp != 0) {
        temp /= 2;
        treeHeight++;
    }

    // 트리 배열 크기 구하기 + 트리 초기화 하기
    int treeSize = int(pow(2, treeHeight + 1));
    int startIndex = treeSize / 2 - 1;
    tree.resize(treeSize + 1);
    std::fill(tree.begin(), tree.end(), LONG_LONG_MAX);

    for (int i = startIndex + 1; i <= startIndex + N; ++i) {
        cin >> tree[i];
    }
    setTree(treeSize - 1);

    // 질의 값 구하기
    for (int i = 0; i < M; ++i) {
        int s, e;
        cin >> s >> e;
        cout << treeMin(s + startIndex, e + startIndex) << '\n';
    }

    return 0;
}

void setTree(int n) {
    while (n != 1) {
        if (tree[n / 2] > tree[n]) {
            tree[n / 2] = tree[n];
        }
        n--;
    }
}

long long treeMin(int s, int e) {
    long long min_val = LONG_LONG_MAX;

    while (s <= e) {
        if (s % 2 == 1) {
            min_val = min(min_val, tree[s]);
            s++;
        }
        if (e % 2 == 0) {
            min_val = min(min_val, tree[e]);
            e--;
        }
        s /= 2;
        e /= 2;
    }
    return min_val;
}