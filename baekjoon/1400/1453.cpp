#include <iostream>
using namespace std;
int main() {
	int n = 0;
	cin >> n;
	int *num = new int[n];
	int num2[110] = { 0, };
	int check = 0;
	for (int i = 0; i < n; i++)
	{
		cin >> num[i];
		if (num2[num[i]] == 0)
			num2[num[i]] = 1;
		else
			check++;
			
	}
	cout << check << endl;




	return 0;
}