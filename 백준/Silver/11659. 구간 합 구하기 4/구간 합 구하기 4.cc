#include <iostream>

using namespace std;

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int n, m;	// 수 N개, M번의 연산
	int s[100001] = {0,};	// 구간 합 배열

	cin >> n >> m;

	// 배열 입력 받음과 동시에 합 배열 생성
	for (int i = 1; i <= n; i++) {
		int a;
		cin >> a;
		s[i] = s[i - 1] + a;
	}
	
	// 횟수 만큼 구간 합 구하기 실행
	for (int rep = 0; rep < m; rep++) {
		int i, j;
		cin >> i >> j;
		cout << s[j] - s[i-1] << "\n";
	}

	return 0;
}