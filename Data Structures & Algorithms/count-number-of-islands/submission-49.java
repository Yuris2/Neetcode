class Solution {
    public int numIslands(char[][] grid) {
        int mRow = grid.length;
        int mCol = grid[0].length;
        int res = 0;

        for (int r = 0; r < mRow; r++) {
            for (int c = 0; c < mCol; c ++) {
                if (grid[r][c] == '1') {
                    res ++;
                    dfs(r,c,grid);
                }
            }
        }

        return res;
        
        
    }

    private void dfs(int r, int c, char[][] grid) {
        if (r < 0 || c < 0 || r >= grid.length || c >= grid[0].length) {
            return;
        }

        if (grid[r][c] != '1') {
            return;
        }

        grid[r][c] = '#';
        dfs(r + 1, c, grid);
        dfs(r, c + 1, grid);
        dfs(r - 1, c, grid);
        dfs(r, c - 1, grid);

        return;

    }
}
