#include <iostream>
#include <string>
using namespace std;
int main()
{
	int n = 0;
	cin >> n;
	string *num = new string[n];
	for (int i = 0; i < n; i++)
	{
		cin >> num[i];
	}
	int len = num[0].length();
	for (int j = 0; j < len; j++)
	{
		int check = 0;
		for (int i = 0; i < n-1; i++)
		{
			if (num[i][j] != num[i + 1][j])
				check = 1;
		}
		if (check == 0)
			cout << num[0][j];
		else
			cout << "?";
	}
	return 0;
}