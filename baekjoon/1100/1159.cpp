#include <iostream>
using namespace std;
int check[26];
int main(void)
{
	int n = 0;
	cin >> n;
	while (n--)
	{
		char num[31];
		cin >> num;
		check[num[0] -'a']++;


	}
	int predaja = 0;
	for (int i = 0; i < 26; i++)
	{
		if (check[i] >= 5)
		{
			predaja = 1;
			cout << (char)(i + 'a');
		}
	}
	if (predaja == 0)
		cout << "PREDAJA";
	return 0;

}