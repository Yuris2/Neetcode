class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        m = len(image)
        n = len(image[0])
        og_color = image[sr][sc]

        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n:
                return
            if image[r][c] != og_color:
                return
            if color == image[r][c]:
                return
            else:
                image[r][c] = color
                dfs(r + 1, c)
                dfs(r - 1, c)
                dfs(r, c + 1)
                dfs(r, c - 1)

        dfs(sr, sc)
        return image

