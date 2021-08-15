#include <bits/stdc++.h>
using namespace std;

#define FAIL 9
const int tr[10][2] = {
    {5,1},
    {2,FAIL},
    {3,FAIL},
    {3,4},
    {5,7},
    {FAIL,6},
    {5,1},
    {8,7},
    {3,6},
    {FAIL,FAIL}
};

bool chk(string &seq)
{
    int state = 0;
    for(int i=0; i<seq.size();i++)
    {
        char ch = seq[i] - '0';
        state = tr[state][ch];
    }
    return state ==4 or state ==6 or state==7;
}
int main()
{
    int t;
    cin >> t;
    while(t--) {
        string seq;
        cin >> seq;
        bool ans = chk(seq);
        cout << (ans ? "YES" : "NO") << '\n';
    }
    
    
}