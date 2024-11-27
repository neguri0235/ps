#include <iostream>
#include <string>

using namespace std;

const int dx[8] = {-1, -1, -1, 1, 1, 1, 0, 0};
const int dy[8] = {-1,  0,  1,-1, 0, 1,-1, 1};

char board[5][5];

bool dbg = false;


bool inRange(int y, int x) {
    if (y < 0 || x < 0) return false;
    if (y >= 5 || x >= 5) return false;
    return true;
}

bool hasWord(int y, int x, const string& word) {

    if(!inRange(y, x)) return false;

    if(board[y][x] != word[0]) return false;

    if (word.size() == 1) return true;

    for(int direction = 0; direction < 8; ++direction) {
        int nextY = y + dy[direction], nextX = x + dx[direction];
        if(hasWord(nextY, nextX, word.substr(1)))
            return true;
    }
    return false;
}

int main() 
{
    int tc = 0;
    string s;
    cin>>tc;
    while (tc--)
    {
        for (int y = 0; y < 5; ++y) {
            cin >> s;
            for (int x = 0; x < 5; ++x) {
                board[y][x] = s[x];
            }
        }

        int num = 0;
        cin>>num;

        while(num--) {
            cin>>s;
            bool res = false;
            for(int y = 0; y <5; ++y){
                for (int x = 0; x<5; ++x){
                    if(board[y][x] != s[0]) continue;
                    res = hasWord(y,x,s);
                    if(res) break;
                }
                if(res) break;
            }
            if(res == true) {
                cout<<s<<' '<<"YES"<<'\n';
            }else{
                cout<<s<<' '<<"NO"<<'\n';
            }
        }
    }
    if (dbg) {
        for(int i = 0; i<5; i++) {
            for (int j = 0; j<5; j++) {
                cout<<board[i][j];
            }
            cout<<endl;
        }

    }
    return 0;
}