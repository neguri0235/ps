#include <iostream>
#include <vector>
#include <cstring>

using namespace std;
int tc, n;

int a[101][101];
int c[101][101];
int triangle(int, int);
int main()
{
    ios_base::sync_with_stdio(false);
    cin>>tc;
    while(tc--) {
        cin>>n;
        memset(a,0,sizeof(a));
        memset(c,-1,sizeof(c));

        for(int i = 0; i<n; i++) {
            for(int j = 0; j<i+1; j++){
                cin>>a[i][j];
            }
        }

        int res = triangle(0,0);
        cout<<res<<'\n';

    }
    return 0;
}

int triangle(int x, int y) {

    int& cache = c[x][y];

    if(cache != -1) return cache;

    if(x == n-1) return cache = a[x][y];

    return cache = max(triangle(x+1,y), triangle(x+1,y+1)) + a[x][y];
}