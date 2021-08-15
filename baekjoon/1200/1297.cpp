#include <iostream>
#include <vector>
#include <queue>
#include <string>
#include <stack>
#include <cmath>
using namespace std;
int main()
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	int dia, hei, wid;
	cin >> dia >> hei >> wid;
	double dia_2 = dia / sqrt(hei*hei + wid * wid);
	cout << (int)(dia_2*hei) << " " << (int)(dia_2*wid) << endl;
	return 0;
}