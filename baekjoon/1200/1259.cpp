#include <iostream>
#include <string.h>
using namespace std;
int main()
{
	char *num = new char[101];
	cin >> num;
	while (num[0] != '0') {
		int len = strlen(num);
		int check = 1;
		for (int i = 0; i < (len / 2); i++)
		{
			if (num[i] != num[len - 1 - i])
				check = 0;
		}
		if (check == 1)
			cout << "yes" << endl;
		else
			cout << "no" << endl;
		cin >> num;
	}
	return 0;
}