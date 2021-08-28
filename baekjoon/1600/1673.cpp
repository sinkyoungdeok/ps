#include <iostream>
#include <string>
#include <algorithm>
#include <cstdio>
#include <iomanip>
#include <ctime>
#include <cmath>
using namespace std;
// A=65, Z=90, a=97, z=122
int main()
{
	int n, k;
	while (cin >> n >> k) {
		int result = n;
		int stemp = n;
		while (stemp >= k)
		{
			int temp = stemp / k;
			result += stemp / k;
			stemp %= k;
			stemp += temp;
		}
		cout << result << endl;
	}
	return 0;
}