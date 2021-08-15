#include <iostream>
#include <algorithm>
using namespace std;
int main()
{
	int n = 0;
	cin >> n;
	int *num = new int[n];
	for (int i = 0; i < n; i++)
		cin >> num[i];
	sort(num, num + n);
	cout << num[0] * num[n - 1] << endl;
	return 0;
}