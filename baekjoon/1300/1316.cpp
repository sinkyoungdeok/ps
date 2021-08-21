#include <iostream>
using namespace std;
int main()
{
	int size = 0;
	cin >> size;
	char *num = new char[100];
	int groupcheck = 0;
	if (size <= 100) {
		for (int a = 0; a < size; a++)
		{
			cin >> num;
			int check = 0;
			if (num[0] != NULL) {
				for (int i = 0; num[i] != NULL; i++)
				{
					if (num[i] == num[i + 1]) // hhhaappy -> h와a와p와y를 하나씩검사하기위함
						continue;
					for (int j = i + 1; num[j] != NULL; j++)
					{
						if (num[i] == num[j])
							check++;
					}
				}
			}
			if (check < 1)
				groupcheck++;
		}
	}
	cout << groupcheck;

	return 0;
}