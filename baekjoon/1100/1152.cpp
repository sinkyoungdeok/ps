#include <iostream>
using namespace std;
int main()
{
	char *a = new char[1000000];
	cin.getline(a, 1000000);
	int check;
	if (a[0] == ' ') check = 0;
	else check = 1;
	for (int i = 0; a[i] != NULL; i++)
	{
		if (a[i] == ' ' && a[i+1] != NULL)
			check++;
	}
	cout << check << endl;
	
	return 0;
}