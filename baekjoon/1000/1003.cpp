#include <iostream>
#include <string>
#include <queue>
#include <functional>
#include <cstdlib>
#include <map>
#include <algorithm>
using namespace std;
int main()
{
	int T;
	cin >> T;
	for (int j = 0; j < T; j++)
	{
		int n;
		cin >> n;
		if (n == 0)
			cout << "1 0" << endl;
		else if (n == 1)
			cout << "0 1" << endl;
		else {
			int *num = new int[n + 1];
			num[0] = 0;
			num[1] = 1;
			for (int i = 2; i <= n; i++)
				num[i] = num[i - 1] + num[i - 2];
			cout << num[n-1] <<" " << num[n] <<  endl;
		}

	}
	return 0;
}

