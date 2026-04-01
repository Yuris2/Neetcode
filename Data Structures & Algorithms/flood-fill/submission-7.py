class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        #Change starting pixel to color
        #Change the adjacent pixel to color iff shares the same color
        #as starting pixel

        R,C = len(image), len(image[0])
        start = image[sr][sc]

        if start == color:
            return image
        
        def dfs(r,c):
            if r < 0 or r >= R or c < 0 or c >= C:
                return
            if image[r][c] != start:
                return
            
            image[r][c] = color

            dfs(r + 1, c)
            dfs(r, c + 1)
            dfs(r - 1, c)
            dfs(r, c - 1)
        
        dfs(sr,sc)

        return image
            
        