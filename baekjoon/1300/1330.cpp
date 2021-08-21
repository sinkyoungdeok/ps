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
	int A, B;
	cin >> A >> B;
	if (A < B)
		cout << "<" << endl;
	else if (A > B)
		cout << ">" << endl;
	else
		cout << "==" << endl;


	return 0;
}