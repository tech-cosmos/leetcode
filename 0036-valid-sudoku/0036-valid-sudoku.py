class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        from collections import defaultdict
        valid=True
        def row_check():
            for row in board:
                if not check_valid(row):
                    return False
            return True
        
        def col_check():
            for i in range(9):
                nums=[row[i] for row in board]
                if not check_valid(nums):
                    return False
            return True

        def grid_check():
            bb=[]
            for row in board:
                for j in range(len(row)):
                    bb.append(row[j])
            for i in range(9):
                gc=i//3
                rem=i%3
                base=rem*3
                if gc!=0:
                    base+=(27*gc)
                grid=bb[base:base+3]+bb[base+9:base+12]+bb[base+18:base+21]
                if not check_valid(grid):
                    return False
            return True
        
        def check_valid(arr):
            num_map=defaultdict(int)
            for num in arr:
                num_map[num]+=1
            num_map['.']=0
            for x in list(num_map.values()):
                if x>1:
                    return False
            return True

        if row_check() and col_check() and grid_check():
            return True
        else:
            return False
