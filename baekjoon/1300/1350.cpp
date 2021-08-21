#include <iostream>
#include <string>
#include <queue>
#include <functional>
#include <cstdlib>
#include <map>
using namespace std;
int main()
{
	int n;
	cin >> n;
	long long int cnt = 0;
	long long int *num = new long long int[n];
	for (int i = 0; i < n; i++)
	{
		cin >> num[i];
	}
	long long int cluster;
	cin >> cluster;

	for (int i = 0; i < n; i++)
	{
		if (num[i] == 0)
			continue;
		else {
			cnt += num[i] / cluster;
			num[i] %= cluster;
			if (num[i] != 0)
				cnt++;

		}
	}
	cout << cluster * cnt << endl;
	return 0;
}