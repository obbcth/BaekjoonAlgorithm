#include <iostream>
using namespace std;

int board[65][65];
int visited[65][65];

int n;
int dfs(int x, int y);

int main() {
    cin >> n;

    for (int i=0; i<n; i++) {
        for (int j=0; j<n; j++) {
            cin >> board[j][i];
        }
    }

    int answer = dfs(0, 0);

    if (answer == 1) {
        cout << "HaruHaru" << endl;
    } else {
        cout << "Hing" << endl;
    }
}

int dfs(int x, int y) {

    if (x == n-1 && y == n-1) {
        return 1;
    }

    int answer = 0;

    visited[x][y] = 1;

    if (x + board[x][y] < n && !visited[x + board[x][y]][y]) 
        answer |= dfs(x + board[x][y], y);

    if (y + board[x][y] < n && !visited[x][y + board[x][y]])
        answer |= dfs(x, y + board[x][y]);

    return answer;
}