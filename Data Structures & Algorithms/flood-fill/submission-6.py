class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m = len(image) - 1
        n = len(image[0]) - 1
        og_color = image[sr][sc]

        def dfs(x, y):
            if x < 0 or x > m:
                return
            if y < 0 or y > n:
                return
            if image[x][y] != og_color:
                return
            if og_color == color:
                return 
            image[x][y] = color
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)
        
        dfs(sr, sc)
        return image
