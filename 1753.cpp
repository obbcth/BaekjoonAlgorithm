#include <iostream>
#include <tuple>
#include <queue>
using namespace std;

const int INF = 2000000000;
const int V_MAX = 200000;

typedef pair<int, int> Edge;

vector<Edge> edges[V_MAX];
int dist[V_MAX];

int V, E, K;

void Dijkstra(int start)
{
    fill(dist, dist+V_MAX, INF);
    priority_queue<Edge> pq;
    pq.push({0, start});

    while (!pq.empty())
    {
        int u, v, d, w;
        tie(d, u) = pq.top();
        pq.pop();

        if (dist[u] < INF) continue;
        dist[u] = -d;

        for (Edge e : edges[u])
        {
            tie(v, w) = e;
            if (dist[v] < INF) continue;
            pq.push({d-w, v});
        }

    }

}


int main(void)
{
    int u, v, w;

    scanf("%d %d %d", &V, &E, &K);

    for(int i=1; i<=E; i++)
    {
        scanf("%d %d %d", &u, &v, &w);
        edges[u].push_back({v, w});
    }

    Dijkstra(K);

    for (int i=1; i<=V; i++)
    {
        if (dist[i] == INF) printf("INF\n");
        else printf("%d\n", dist[i]);
    }

}