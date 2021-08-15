#include <iostream>
using namespace std;
int k[51];
int k_check[51];
int p[51];
int party[51][51];
int main()
{
    int N,M;
    cin >> N>> M;
    int K;
    cin >> K;
    

    for(int i=0; i< K;i++)
    { 
        cin >> k[i];
        k_check[k[i]] = 1;
    }

    for(int i=0; i< M;i++)
    {
        cin >> p[i];
        for(int j=0; j< p[i];j++)
            cin >> party[i][j];
    }


    while(1)
    {
        int check = 0;
        
        for(int i=0; i< M;i++)
        {
            int mid_check = 0;
            for(int j=0; j< p[i];j++)
            {
                if(k_check[party[i][j]])
                    mid_check =1;


            }
            if(mid_check)
            {
                for(int j=0; j< p[i];j++)
                {
                    if(k_check[party[i][j]] == 0)
                    {
                        k_check[party[i][j]] =1;
                        check =1;
                    }
                }
            }
        }


        if(check == 0 )
            break;

        
    }


    int result =0;
    for(int i=0; i<M;i++)
    {
        int check =0;
        for(int j=0; j<p[i]; j++)
        {
            if(k_check[party[i][j]])
                check =1;
        }
        if(check == 0)
            result ++;
    }
    cout << result << endl;


    return 0;
}