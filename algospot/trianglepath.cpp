#include <iostream>
#include <vector>
#include <cstring>

using namespace std;
int tc,n;

int dp[101][101];
int tr[101][101];

int main()
{

    ios_base::sync_with_stdio(false);

    cin>>tc;
    while(tc--) {
        cin>>n;
        int res = 0;
        memset(dp,0,sizeof(dp));
        memset(tr,0,sizeof(tr));

        for(int i = 0; i<n; ++i){
            for(int j = 0; j<i+1; ++j){
                cin>>tr[i][j];
            }
        }

        dp[0][0] = tr[0][0];

        for(int i = 1; i<n; ++i){
            for(int j = 0; j<i+1; ++j){
                if(j == 0){ dp[i][0] = dp[i-1][0] + tr[i][0];}
                else{
                    dp[i][j] = tr[i][j] + max(dp[i-1][j], dp[i-1][j-1]);
                }
                res = max(res,dp[i][j]);
            }
        }
        cout<<res<<'\n';
        }

    return 0;
}