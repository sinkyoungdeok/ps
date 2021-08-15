#include <iostream>
#include <string.h>
using namespace std;
int main()
{
	while (1) {
		char *num = new char[256];
		cin.getline(num, 256);
		if (num[0] == '#')
			return 0;
		int numlen = strlen(num);
		int check = 0;
		for (int i = 0; i < numlen; i++)
			if (num[i] == 'a' || num[i] == 'A' || num[i] == 'e' || num[i] == 'E' || num[i] == 'i' || num[i] == 'I' || num[i] == 'o' || num[i] == 'O' || num[i] == 'u' || num[i] == 'U')
				check++;
		cout << check << endl;
	}

	return 0;
}