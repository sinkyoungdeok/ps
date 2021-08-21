#include <iostream>
#include<cstdio>
#include<cmath>
using namespace std;
int main()
{
	int A, B, N;
	cin >> A >> B >> N;

	if (A == B)
	{
		cout << "0" << endl;
		return 0;
	}
	A %= B;

	
	while (--N)
	{
		A *= 10;
		A %= B;
	}
	cout << (A*10)/B << endl;

	return 0;
}