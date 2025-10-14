#include <iostream>
#include <vector>
#include <tuple>    
#include <cmath>

using namespace std;
vector<tuple<int, int, int>> A[10];
long lcm;
bool visited[10];
long D[10];
long gcd(long a, long b);
void DFS(int node);

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N;
    cin >> N;
    lcm = 1;

    for (int i = 0; i < N-1; ++i) {
        int a, b, p, q;
        cin >> a >> b >> p >> q;
        A[a].emplace_back(b, p, q);
        A[b].emplace_back(a, q, p);
        // 두 수의 최소 공배수는 두 수의 곱을 최대 공약수로 나눈 것
        lcm *= (p * q / gcd(p, q));
    }

    D[0] = lcm;
    DFS(0);
    long mgcd = D[0];
    for (int i = 1; i < N; ++i) {
        mgcd = gcd(mgcd, D[i]);
    }
    for (int i = 0; i < N; ++i) {
        cout << D[i] / mgcd << ' ';
    }

    return 0;
}

long gcd(long a, long b) {
    if (b == 0) {
        return a;
    }
    else {
        return gcd(b, a % b);
    }
}

void DFS(int node) {
    visited[node] = true;

    for (tuple<int, int, int> i : A[node]) {
        int next = get<0>(i);
        if (!visited[next]) {
            // 주어진 비율로 다음 노드값 업데이트
            D[next] = D[node] * get<2>(i) / get<1>(i);
            DFS(next);
        }
    }
}
