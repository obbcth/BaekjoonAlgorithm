#include <iostream>
#include <tuple>
#include <queue>
#include <algorithm>
using namespace std;

const int INF = 100000001;
const int V_MAX = 1001;

typedef pair<int, int> Edge;

vector<Edge> edges[V_MAX];
int dist[V_MAX];
int route[V_MAX];

int V, E, K;
int END;

void Dijkstra(int start)
{
    priority_queue<Edge, vector<Edge>, greater<Edge>> pq;
    pq.push({0, start});
    dist[start] = 0;

    while (!pq.empty())
    {
        int u, v, d, w;
        tie(d, u) = pq.top();
        pq.pop();

        if (dist[u] < d) continue;

        for (Edge e : edges[u])
        {
            tie(v, w) = e;
            if (d + w < dist[v]) {
                route[v] = u;
                dist[v] = d + w;
                pq.push({dist[v], v});
            }
        }

    }

}


int main(void)
{
    int u, v, w;

    scanf("%d %d", &V, &E);

    for(int i=1; i<=E; i++)
    {
        scanf("%d %d %d", &u, &v, &w);
        edges[u].push_back({v, w});
    }

    scanf("%d %d", &K, &END);

    fill(dist, dist+V+1, INF);
    Dijkstra(K);

    route[K] = 0;
    int idx = END;

    vector<int> answer;

    while(1) {
        if(route[idx] == 0) {
            answer.push_back(K);
            break;
        }
        answer.push_back(idx);
        idx = route[idx];
    }
    
    reverse(answer.begin(), answer.end());

    cout << dist[END] << '\n';
    cout << answer.size() << '\n';

    for(int i = 0 ; i < answer.size() ; i++)
        cout << answer[i] << " ";

}