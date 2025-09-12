#include <iostream>
#include <cmath>

using namespace std;

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	long N, T, P;
	long T_shirts[6] = {};
	long t_shirts_value = 0, pen_value_bundle = 0, pen_value_single = 0;

	cin >> N;
	for (int i = 0; i < 6; i++) {
		cin >> T_shirts[i];
	}
	cin >> T >> P;

	for (int i = 0; i < 6; i++) {
		if (T_shirts[i] == 0)
			continue;
		else if (T_shirts[i] % T == 0)
			t_shirts_value += T_shirts[i] / T;
		else if ((T_shirts[i] % T) < T && T_shirts[i] % T != 0)
			t_shirts_value += T_shirts[i] / T + 1;

	}

	pen_value_bundle = N / P;
	pen_value_single = N % P;

	cout << t_shirts_value << "\n";
	cout << pen_value_bundle << " " << pen_value_single << "\n";

	return 0;
}