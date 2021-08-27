#include <iostream>
#include <cstdio>
#include <cmath>
#include <string>
using namespace std;
int main()
{
	int n = 0;
	cin >> n;
	string *num = new string[n];
	int num_i = 0;
	for (int i = 0; i < n; i++)
	{
		string a;
		cin >> a;
		int check = 0;
		for (int j = 0; j < num_i; j++)
		{
			for (int k = 0; k < a.length(); k++)
			{
				a.push_back(a[0]);
				a.erase(0, 1);
				if (a == num[j])
				{
					check = 1;
				}
			}
		}
		if (check == 0)
			num[num_i++] = a;
	}
	cout << num_i << endl;
	return 0;
}