#include <stdio.h>

char str[505];
int trie[5050505][26], fin[5050505], sz = 1;

void ins() {
    int cur = 0;
    for (int i = 0; str[i]; ++i) {
        int nxt = str[i] - 'a';
        if (!trie[cur][nxt]) trie[cur][nxt] = sz++;
        cur = trie[cur][nxt];
    }
    fin[cur] = 1;
}

int query() {
    int cur = 0;
    for (int i = 0; str[i]; ++i) {
        int nxt = str[i] - 'a';
        if (!trie[cur][nxt]) return 0;
        cur = trie[cur][nxt];
    }
    return fin[cur];
}

int main() {
    int n, m, res = 0;
    scanf("%d %d", & n, & m);
    for (int i = 0; i < n; ++i) {
        scanf("%s", str);
        ins();
    }
    for (int i = 0; i < m; ++i) {
        scanf("%s", str);
        res += query();
    }
    printf("%d\n", res);
    return 0;
}