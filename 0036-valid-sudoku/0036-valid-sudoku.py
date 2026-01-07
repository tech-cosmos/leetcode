class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        from collections import defaultdict
        valid=True
        bb=[]
        def check_valid(arr):
            num_map=defaultdict(int)
            for num in arr:
                num_map[num]+=1
            num_map['.']=0
            for x in list(num_map.values()):
                if x>1:
                    return False
            return True

        for row in board:
            if not check_valid(row):
                return False
            for j in range(9):
                bb.append(row[j])
        for i in range(9):
            nums=[bb[j*9+i] for j in range(9)]
            if not check_valid(nums):
                return False
            gc=i//3
            base=(i%3)*3
            if gc!=0:
                base+=(27*gc)
            grid=bb[base:base+3]+bb[base+9:base+12]+bb[base+18:base+21]
            if not check_valid(grid):
                return False
        return True