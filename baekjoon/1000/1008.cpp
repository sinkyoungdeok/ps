#include <iostream>
#include <string>
using namespace std;
int main()
{
	double a, b = 0;
	cin >> a >> b;
	cout << fixed;
	cout.precision(9);
	cout << a / b;
	return 0;
}