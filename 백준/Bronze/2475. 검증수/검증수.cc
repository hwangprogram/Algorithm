#include <iostream>
#include <math.h>
using namespace std;

int main() {
	int a, b, c, d, e;
	cin >> a >> b >> c >> d >> e;
	a = pow(a, 2);
	b = pow(b, 2);
	c = pow(c, 2);
	d = pow(d, 2);
	e = pow(e, 2);
	cout << (a+b+c+d+e) % 10;

	return 0;
}