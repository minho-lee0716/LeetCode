import java.util.ArrayList;
import java.util.List;

class Solution {
    public boolean validPath(int n, int[][] edges, int source, int destination) {
        List<List<Integer>> graph = new ArrayList<>();
        boolean[] visited = new boolean[n];

        for (int i = 0; i < n; i++) {
            graph.add(new ArrayList<>());
        }

        for (int[] edge : edges) {
            graph.get(edge[0]).add(edge[1]);
            graph.get(edge[1]).add(edge[0]);
        }

        dfs(graph, source, destination, visited);
        return visited[destination];
    }

    private void dfs(List<List<Integer>> graph, int v, int target, boolean[] visited) {
        visited[v] = true;

        for (int neighbor : graph.get(v)) {
            if (neighbor == target) {
                visited[neighbor] = true;
                break;
            }

            if (!visited[neighbor]) {
                dfs(graph, neighbor, target, visited);
            }
        }
    }
}
