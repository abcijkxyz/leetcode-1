class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        p = [i for i in range(n)]

        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]

        for a, b in edges:
            p[find(b)] = find(a)
        return sum(i == find(i) for i in range(n))
