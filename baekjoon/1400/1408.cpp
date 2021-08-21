#include <cstdio>

int main()
{
	int h, m, s, h2, m2, s2, h3, m3, s3;
	scanf("%d:%d:%d", &h, &m, &s);
	scanf("%d:%d:%d", &h2, &m2, &s2);

	int cT, sT, rT;
	cT = h * 60 * 60 + m * 60 + s;
	sT = h2 * 60 * 60 + m2 * 60 + s2;

	if (cT > sT)
		sT += 24 * 60 * 60;

	rT = sT - cT;
	h3 = rT / 3600, rT %= 3600;
	m3 = rT / 60, rT %= 60;
	s3 = rT;

	printf("%02d:%02d:%02d", h3, m3, s3);
}