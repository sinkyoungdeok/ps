#include <iostream>
#include <cmath>
using namespace std;

int main() {
	long long A,B,C;
	cin >> A>>B>>C;
	
	if(B == 0)
	{	
		cout << 1 << '\n';
		return 0;
	}
	long long result= 1;
	A%=C;
	while(B >0)
	{
		if(B%2 == 1)
		{
			result = result * A;
			result %= C;
		}
		A *= (A %C);
		A %= C;
		B /= 2;
	}
	result %= C;
	cout << result << '\n';
	
	
	
	return 0;
}