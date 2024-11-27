#include <iostream>
#include <vector>

using namespace std;

int tc,n,arrived;

void jump(vector<vector<int>>&, vector<vector<int>>&, int, int);

int main()
{
    ios_base::sync_with_stdio(false);
    cin>>tc;
    while(tc--) {

        cin>>n;
        arrived = false;
        vector<vector<int>>a(n,vector<int>(n,0));
        vector<vector<int>>dp(n,vector<int>(n,0));
        for(int i = 0; i<n; ++i){
            for(int j = 0; j<n; ++j) {
                cin>>a[i][j];
            }
        }

        jump(a,dp,0,0);
        if(arrived) cout<<"YES"<<'\n';
        else cout<<"NO"<<'\n';
    }

    return 0;
}

void jump(vector<vector<int>>& a, vector<vector<int>>&dp, int x, int y) {


    if(x >= n || y >= n || arrived) return;

    int& visit = dp[x][y];

    if(visit) return;
    visit = true;

    if(x == n-1 && y == n-1) {
        arrived = true;
        return;
    }

    int nx = x + a[x][y];
    int ny = y;

    jump(a,dp, nx,ny);

    nx = x;
    ny = y + a[x][y];
    jump(a,dp, nx,ny);
}