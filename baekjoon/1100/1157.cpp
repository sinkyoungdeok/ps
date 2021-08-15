#include <iostream>
using namespace std;
int main()
{ // 알파벳a =아스키 97 /  z=아스키122
	char *num = new char[1000000];
	int *ascii = new int[130];
	cin >> num;
	int maxascii = 0;
	int maxasciivalue = 0;
	int maxcheck = 0;
	for (int i = 0; num[i] != 0; i++) // 입력된 대문자를 모두 소문자로 변경
		if (!(num[i] >= 'a' && num[i] <= 'z'))
			num[i] += 32;

	for (int i = 97; i < 123; i++) // 아스키코드에 사용할 배열들 0으로초기화
		ascii[i] = 0;

	for (int i = 0; num[i] != 0; i++) // num[i]번째알파벳이 a이면 a에해당하는아스키코드번째 배열을 ++시킴
		ascii[(int)num[i]] ++;

	for (int i = 97; i < 123; i++) // 가장 많이 사용한것을 확인
		if (maxascii < ascii[i]) {
			maxascii = ascii[i];
			maxasciivalue = i;
		}

	for (int i = 97; i < 123; i++) // aaaabbbb 일경우 빈도수많은것이 a,b개이다. 이때 maxcheck를 활용해서 ?가 출력될수있도록..
		if (maxascii == ascii[i])
			maxcheck++;

	if (maxcheck == 1)
		cout << (char)(maxasciivalue - 32) << endl;
	else
		cout << "?" << endl;
	return 0;
}