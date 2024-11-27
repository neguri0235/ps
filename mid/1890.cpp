
/*
4
2 3 3 1
1 2 1 3
1 2 3 1
3 1 1 0
*/

#include <iostream>
#include <cstring>

using namespace std;

int n,k;

int dp[102][102];
int vec[102][102];

int main()
{
    ios_base::sync_with_stdio(false);
    cin>>n;

    memset(dp, -1, sizeof(dp));
    memset(vec, -1, sizeof(vec));

    for (int i = 1; i<=n; ++i){
        for(int j = 1; j<=n; ++j){
            cin>>k;
            vec[i][j] = k;
        }
    }

    dp[1][1] = 1;
    for(int i = 1; i<=n; ++i) {
        for(int j = 1; j<=n; ++j) {

            if(i == n && j == n) break;
            if(dp[i][j] == -1) continue;

            int nx = j + vec[i][j];

            if (nx <= n) {
                if(dp[i][nx] == -1) {
                    dp[i][nx] = dp[i][j];
                }else{
                    dp[i][nx] += dp[i][j];
                }
            }

            int ny = i + vec[i][j];
            if (ny <= n) {
                if(dp[ny][j] == -1) {
                    dp[ny][j] = dp[i][j];
                }else{
                    dp[ny][j] += dp[i][j];
                }
            }
        }
    }
    cout<<dp[n][n]<<'\n';
    return 0;
}