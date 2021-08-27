#include <iostream>
#include <iomanip>


using namespace std;
int main()
{
	int num = 0;
	float sum = 0;
	cin >> num;
	int *score = new int[num];
	for (int i = 0; i < num; i++)
		cin >> score[i];
	for (int i = 0; i < num; i++)
	{
		for (int j = 0; j < i; j++)
		{
			if (score[j] > score[i])
			{
				int swap = score[j];
				score[j] = score[i];
				score[i] = swap;
			}
		}
	}
	for (int i = 0; i < num; i++)
	{
		sum += ((double)score[i] / score[num-1]) * 100;
	}
	cout << fixed;
	cout.precision(2);
	cout << sum / num;
	//system("pause");
	return 0;
}