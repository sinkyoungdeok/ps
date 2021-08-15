#include <iostream>
#include <algorithm>
using namespace std;
int main()
{
	int n1; int m1;
	int n2; int m2;
	cin >> n1 >> m1 >> n2 >> m2;

	int min1 = min(n1, m1);
	int min2 = min(n2 - n1, m2 - m1);
	cout << min(min1, min2) << endl;
	return 0;
}