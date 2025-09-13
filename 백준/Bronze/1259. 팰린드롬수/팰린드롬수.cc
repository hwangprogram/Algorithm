#include <iostream>
#include <cmath>

using namespace std;

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	string number;
	while (true)
	{
		bool palindrom = 1;
		cin >> number;
		if (number == "0")
			break;

		for (int i = 0; i < number.length() / 2; i++) {
			if (number[i] != number[number.length() - 1 - i]) {
				palindrom = 0;
				break;
			}
		}
		if (palindrom)
			cout << "yes\n";
		else
			cout << "no\n";
	}

	return 0;
}