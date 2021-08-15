#include <iostream>
using namespace std;
int main() {
	char *a = new char[10010];
	char *b = new char[10010];
	cin >> a >> b;

	long long int sum = 0;

	for (int i = 0; a[i] != NULL; i++)
	{
		for (int j = 0; b[j] != NULL; j++)
		{
			sum += (a[i] - '0') * (b[j] - '0');
		}

	}
	cout << sum << endl;




	return 0;
}