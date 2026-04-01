class Solution: 

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def getAdjacentPixels(r, c, og_color):
            adj_pixels = []
            if r != len(image) - 1 and image[r + 1][c] == og_color:
                adj_pixels.append((r + 1, c))
            if r != 0 and image[r - 1][c] == og_color:
                adj_pixels.append((r - 1, c))
            if c != len(image[0]) - 1 and image[r][c + 1] == og_color:
                adj_pixels.append((r, c + 1))
            if c != 0 and image[r][c - 1] == og_color:
                adj_pixels.append((r, c - 1))
            return adj_pixels
            
        agenda = set()
        agenda.add((sr, sc))
        while agenda:
            row, col = agenda.pop()
            og_color = image[row][col]
            if color == og_color:
                break
            image[row][col] = color
            for coord in getAdjacentPixels(row, col, og_color):
                agenda.add(coord)
        return image
