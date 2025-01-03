function validPath(n: number, edges: number[][], source: number, destination: number): boolean {
    const graph: number[][] = Array.from({ length: n }, () => []);
    const visited: boolean[] = Array(n).fill(false);

    for (const edge of edges) {
        graph[edge[0]].push(edge[1]);
        graph[edge[1]].push(edge[0]);
    }


    dfs(graph, source, destination, visited);
    return visited[destination];
};

function dfs(graph: number[][], v: number, target: number, visited: boolean[]): void {
    visited[v] = true;

    for (const i of graph[v]) {
        if (i === target) {
            visited[i] = true;
            break;
        }

        if (!visited[i]) {
            dfs(graph, i, target, visited);
        }
    }
}