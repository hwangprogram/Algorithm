#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	// 재료의 개수 N, 갑옷을 만드는데 필요한 수 M
	int N, M;
	cin >> N;
	cin >> M;

	// 재료의 고유번호 배열
	vector<int> ing_vec(N, 0);
	for (int i = 0; i < N; i++) {
		cin >> ing_vec[i];
	}
	// 벡터 정렬
	sort(ing_vec.begin(), ing_vec.end());

	// 포인터 두개 (양 끝점)
	// 양 끝점에서 시작하고, 둘 더한 값이 M이면 count++, end 이동
	// 둘 더한 값이 M보다 작으면 start 이동
	// 둘 더한 값이 M보다 크면 end 이동
	// 둘이 만나면 종료
	int start_point = 0, end_point = N - 1;
	// 카운트
	int count = 0;
	while (start_point < end_point) {
		int sum = ing_vec[start_point] + ing_vec[end_point];
		// 둘 합이 M이라면, count 늘리고 end 이동
		if (sum == M) {
			count++;
			end_point--;
		}
		// 둘 합이 M보다 작으면 start 이동
		else if (sum < M)
			start_point++;
		// 둘 합이 M보다 크면 end 이동
		else if (sum > M)
			end_point--;	
	}

	cout << count << "\n";

	return 0;
}