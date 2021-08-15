#include <iostream>
#include <vector>
#include <queue>
#include <string>
using namespace std;
int main()
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	int T;
	cin >> T;
	
	unsigned long long int pascal_t[31][31] = { 0 };
	pascal_t[1][1] = 1;
	for (int i = 2; i <= 30; i++)
		for (int j = 1; j <= 30; j++)
		{
			pascal_t[i][j] = pascal_t[i - 1][j - 1] + pascal_t[i - 1][j];
		}
	for (int t = 0; t < T; t++)
	{
		int n, k;
		cin >> n >> k;
		if(n>k)
			cout << pascal_t[n + 1][k + 1] << endl;
		else
			cout << pascal_t[k + 1][n + 1] << endl;
	}
	return 0;
}