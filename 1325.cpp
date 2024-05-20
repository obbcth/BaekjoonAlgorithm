#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int n, m;
vector<vector<int>> edges;  // Adjacency list representation of the graph

int bfs(int v) {
    queue<int> queue;
    queue.push(v);

    vector<bool> visited(n + 1, false);  // Visited flag for each node
    visited[v] = true;
    int componentSize = 0;

    while (!queue.empty()) {
        int q = queue.front();
        queue.pop();
        componentSize++;

        for (int neighbor : edges[q]) {
            if (!visited[neighbor]) {
                queue.push(neighbor);
                visited[neighbor] = true;
            }
        }
    }

    return componentSize;
}

int main() {
    cin >> n >> m;

    edges.resize(n + 1);  // Resize adjacency list for n nodes (1-based indexing)

    for (int i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;
        // edges[a].push_back(b);  // Add edge (a, b) to adjacency list
        edges[b].push_back(a);  // Add edge for undirected graph
    }

    int maxComponentSize = 0;
    vector<int> largestComponents;

    for (int start = 1; start <= n; start++) {
        if (!edges[start].empty()) { // Skip already visited nodes (empty adjacency list)
            int componentSize = bfs(start);
            // cout << "result: " << componentSize << endl;
            if (componentSize > maxComponentSize) {
                maxComponentSize = componentSize;
                largestComponents.clear();
                largestComponents.push_back(start);
            } else if (componentSize == maxComponentSize) {
                largestComponents.push_back(start);
            }
        }
    }

    // cout << maxComponentSize;
    if (!largestComponents.empty()) {
        for (int node : largestComponents) {
            cout << node << " ";
        }
    }
    cout << endl;

    return 0;
}
