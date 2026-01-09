class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if target>row[-1] or target<row[0]:
                continue
            for element in row:
                if element==target:
                    return True
        return False

        