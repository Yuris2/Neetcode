class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        source = image[sr][sc]

        if source == color:
            return image
        
        seen = set()
        def dfs(r,c):
            if r < 0 or c < 0 or r >= len(image) or c >= len(image[0]):
                return
            if (r,c) in seen or image[r][c] != source:
                return 
            
            seen.add((r,c))
            image[r][c] = color

            dfs(r+1,c)
            dfs(r,c+1)
            dfs(r-1,c)
            dfs(r,c-1)

            return
        
        dfs(sr, sc)
        return image



        