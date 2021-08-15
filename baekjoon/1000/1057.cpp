#include <iostream>
#include <cstdio>
using namespace std;
int main()
{
	int n = 0; int jimin = 0; int hansu = 0;
	cin >> n >> jimin >> hansu;
	int count = 0;
	if (n < jimin || n < hansu)
		cout << "-1" << endl;
	else {
		while (jimin != hansu)
		{
			jimin = (jimin + 1) / 2;
			hansu = (hansu + 1) / 2;
			count++;
		}
		cout << count << endl;
	}
	

	return 0;
}