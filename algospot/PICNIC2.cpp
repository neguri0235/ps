#include <iostream>
#include <vector>

using namespace std;

int tc, n, m, fr, to;
int pairs(vector<vector<int>>&, vector<int>&);
int main()
{
    cin>>tc;

    while(tc--) {
        cin>>n>>m;

        vector<vector<int>>p(10, vector<int>(10,0));
        for(int i = 0; i<m; i++) {
            cin>>fr>>to;
            p[fr][to] = p[to][fr] = 1;
        }
        vector<int>c(10,0);

        cout<<pairs(p,c)<<endl;
    }

    return 0;
}

int pairs(vector<vector<int>>& p, vector<int>& c){
    int first = -1;
    int ret = 0;

    for(int i = 0; i<n; ++i) {
        if(!c[i]) {
            first = i;
            break;
        }
    }

    if(first == -1) return 1;

    for(int i = first + 1; i<n; ++i) {
        if(!c[i] && p[first][i]) {
            c[i] = c[first] = 1;
            ret += pairs(p,c);
            c[i] = c[first] = 0;
        }
    }
    return ret;
}