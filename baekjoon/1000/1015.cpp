#include<iostream>
#include<algorithm>
using namespace std;
 
int main() {
    pair<int, int> A[50];
    int Size, B[50];
    
    cin >> Size;
    for (int i = 0; i < Size; ++i) {
        cin >> A[i].first;
        A[i].second = i;
    }
    sort(A, A + Size);
    for (int i = 0; i < Size; ++i) 
        B[A[i].second] = i;
 
    for (int i = 0; i < Size; ++i) cout << B[i] << " ";
 
}