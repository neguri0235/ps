#include <iostream>
#include <vector>

using namespace std;

int tc, n, m;
int main()
{
    cin>>tc;
    while(tc--) {
        cin>>n>>m;

        vector<vector<char>>p(21, vector<char>(21,'#'));
        for(int i = 0; i<n; ++i) {
            for(int j = 0; j<m; ++j) {
                cin>>p[i][j];
            }
        }
    }
    return 0;
}