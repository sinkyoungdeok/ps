#include <iostream>
#include <string>
using namespace std;
int main()
{
	char n[9][9];
	for (int i = 0; i < 8; i++)
	{
		cin >> n[i];
	}
	int check = 0;
	for ( int i = 0; i< 8 ; i++)
		for (int j = 0; j < 8; j++)
		{
			if ((i + j) % 2 == 0 && n[i][j] == 'F')
				check++;
		}
	cout << check << endl;
	return 0;
}