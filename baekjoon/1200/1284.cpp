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
	while (1) 
	{
		string N;
		cin >> N;
		if (N == "0")
			break;

		int cnt = 0;
		for (int i = 0; i < N.length(); i++)
		{
			cnt++;
			if (N[i] == '1')
				cnt += 2;
			else if (N[i] == '0')
				cnt += 4;
			else
				cnt += 3;
		}
		cout << ++cnt << endl;
	}
	return 0;
}