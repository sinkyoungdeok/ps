#include <iostream>
#include <string>
using namespace std;
int main()
{
	string a, b, c;
	cin >> a >> b >> c;
	long long int sum = 0;
	if (a == "black")
		sum += 0;
	else if (a == "brown")
		sum += 10;
	else if (a == "red")
		sum += 20;
	else if (a == "orange")
		sum += 30;
	else if (a == "yellow")
		sum += 40;
	else if (a == "green")
		sum += 50;
	else if (a == "blue")
		sum += 60;
	else if (a == "violet")
		sum += 70;
	else if (a == "grey")
		sum += 80;
	else if (a == "white")
		sum += 90;

	if (b == "black")
		sum += 0;
	else if (b == "brown")
		sum += 1;
	else if (b == "red")
		sum += 2;
	else if (b == "orange")
		sum += 3;
	else if (b == "yellow")
		sum += 4;
	else if (b == "green")
		sum += 5;
	else if (b == "blue")
		sum += 6;
	else if (b == "violet")
		sum += 7;
	else if (b == "grey")
		sum += 8;
	else if (b == "white")
		sum += 9;

	if (c == "black")
		sum *= 1;
	else if (c == "brown")
		sum *= 10;
	else if (c == "red")
		sum *= 100;
	else if (c == "orange")
		sum *= 1000;
	else if (c == "yellow")
		sum *= 10000;
	else if (c == "green")
		sum *= 100000;
	else if (c == "blue")
		sum *= 1000000;
	else if (c == "violet")
		sum *= 10000000;
	else if (c == "grey")
		sum *= 100000000;
	else if (c == "white")
		sum *= 1000000000;
		
	cout << sum << endl;
	return 0;
}