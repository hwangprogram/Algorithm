#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;
static vector<vector<int>> list;
static vector<bool> visited;
static vector<int> cnt_list;
int BFS(int node);

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int N, M; // N개의 노드 M개의 간선
	int max_cnt = 0;	// 최대 해킹컴퓨터 개수
	cin >> N >> M;
	list.resize(N + 1);
	visited.resize(N + 1);
	cnt_list.resize(N + 1);

	for (int i = 0; i < M; ++i) {
		int A, B;	// B -> A
		cin >> A >> B;
		list[B].push_back(A);
	}

	for (int start = 1; start <= N; ++start) {
		visited.assign(N + 1, false);
		cnt_list[start] = BFS(start);
		max_cnt = max(max_cnt, cnt_list[start]);
	}

	for (int i = 1; i <= N; ++i) {
		if (max_cnt == cnt_list[i]) {
			cout << i << ' ';
		}
	}
	cout << '\n';

	return 0;
}

int BFS(int node) {
	queue<int> q;
	int cnt = 1;	// 자신을 포함한 해킹된 컴퓨터 수
	q.push(node);
	visited[node] = true;

	while (!q.empty())
	{
		int now = q.front();
		q.pop();

		for (int next : list[now]) {
			if (!visited[next]) {
				visited[next] = true;
				q.push(next);
				cnt++;
			}
		}
	}

	return cnt;
}