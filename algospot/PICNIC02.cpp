#include <iostream>
#include <cstring>
#include <cstdlib>
#include <vector>

using namespace std;

int tc;
int n,m;
int fr, to;

int student[11][11];

int pairs(vector<int>&);

int main()
{
    ios_base::sync_with_stdio(false);
    cin>>tc;

    while(tc--) {
        cin>>n>>m;

        memset(student, 0, sizeof(student));
        for(int i = 0; i<m; i++) {
            cin>>fr;
            cin>>to;
            student[fr][to] = student[to][fr] = 1;
        }

        vector<int>c(n,-1);
        cout<<pairs(c)<<'\n';
    }

    return 0;
}

int pairs(vector<int>& c){

    int person = -1;
    int cnt = 0;
    for(int i = 0; i<c.size(); ++i) {
        if(c[i] == -1)
        {
            person = i;
            break;
        }
    }

    if(person == -1) return 1;

    for(int k = person + 1; k<c.size(); k++) {
        if(student[person][k] == 1 && c[k] == -1){
            c[person] = 1;
            c[k] = 1;
            cnt += pairs(c);
            c[person] = -1;
            c[k] = -1;
        }
    }
    return cnt;
}