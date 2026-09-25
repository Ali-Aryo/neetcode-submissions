class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # row check
        for row in range(9):
            seen = set()
            for col in range(9):
                value = board[row][col] 

                if  value == ".": #ignore empty
                    continue

                if value in seen: #check for dups
                    return False
                
                else:
                    seen.add(value)
        
        #col check
        for col in range(9):
            seen = set()
            for row in range(9):
                value = board[row][col]

                if  value == ".": #ignore empty
                    continue

                if value in seen: 
                    return False
                
                else: 
                    seen.add(value)


        # Check all 3x3 boxes
        for box_row in range(0, 9, 3): #for i in range of 0 - 9, steps of 9
            for box_col in range(0, 9, 3):
                seen = set()

                for row in range(box_row, box_row + 3):
                    for col in range(box_col, box_col + 3):
                        value = board[row][col]

                        if value == ".":
                            continue

                        if value in seen:
                            return False

                        seen.add(value)

        return True