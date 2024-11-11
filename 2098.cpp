#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

#define INF 10000000

int N;
vector<vector<int>> city;
vector<vector<int>> visited;

int dfs(int row, int visit, int start, int cnt) {
    if (cnt == N) { // 모든 도시를 방문한 경우
        return 0;
    }

    if (visited[row][visit] != -1) { // 이미 방문한 경로가 있다면
        return visited[row][visit];
    }

    int ret = INF;
    for (int i = 0; i < N; i++) {
        // 현재 도시가 이미 방문된 도시거나 연결이 안되어 있다면 건너뜀
        if ((visit & (1 << i)) != 0 || city[row][i] == 0) {
            continue;
        }

        // 마지막 도시일 때 시작 도시로 돌아가지 않으면 건너뜀
        if ((cnt == N - 1 && i != start) || (cnt != N - 1 && i == start)) {
            continue;
        }

        // i번째 도시를 방문하고 최소 비용 갱신
        ret = min(ret, dfs(i, visit | (1 << i), start, cnt + 1) + city[row][i]);
    }

    visited[row][visit] = ret;
    return visited[row][visit];
}

int main() {
    // 도시 개수 입력
    cin >> N;

    // 도시 간 비용 입력
    city.resize(N, vector<int>(N));
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cin >> city[i][j];
        }
    }

    // 방문 상태 초기화
    visited.assign(N, vector<int>(1 << N, -1));

    // DFS 시작: 첫 도시에서, 방문 상태 0, 시작 도시 0, 방문한 도시 개수 0
    cout << dfs(0, 0, 0, 0) << endl;

    return 0;
}
