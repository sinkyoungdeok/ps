#include<cstdio>
#include <iostream>
using namespace std;
int main() 
{
	int a, b;
	cin >> a >> b;
	int rea = 0;
	int reb = 0;

	while (a)
	{
		rea *= 10;
		rea += a % 10;
		a /= 10;
	}
	while (b)
	{
		reb *= 10;
		reb += b % 10;
		b /= 10;
	}
	
	int result = rea + reb;
	int re_result = 0;
	while (result)
	{
		re_result *= 10;
		re_result += result % 10;
		result /= 10;
	}
	cout << re_result << endl;


	return 0;
}