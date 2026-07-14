class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # let us say board = 
        '''
        board= [ ["5","3",".",".","7",".",".",".","."]
                ,["6",".",".","1","9","5",".",".","."]
                ,[".","9","8",".",".",".",".","6","."]
                ,["8",".",".",".","6",".",".",".","3"]
                ,["4",".",".","8",".","3",".",".","1"]
                ,["7",".",".",".","2",".",".",".","6"]
                ,[".","6",".",".",".",".","2","8","."]
                ,[".",".",".","4","1","9",".",".","5"]
                ,[".",".",".",".","8",".",".","7","9"]  ]
        '''
        #1st checking if the rows are correct or not 
        #note len(board)=9
        for i in range (len(board)):
            '''
            #now validating the row
            for j in board[i]:
                
                if j==".":
                    continue
                
                #No need to check this one I overthought 0

                elif int(j)>=0 and int(j)<=9:
                    continue 
                
                else:
                    return false # invalid sudoku 
            '''
            #now validating the row  ( if any duplicate is there ) 
            for j in range(len(board[i])):
                for k in range(j+1, len(board[i])):

                    if board[i][j]=="." or board[i][k]==".":
                        continue
                    elif board[i][j]==board[i][k]:
                        return False # as duplicate element present so invalid 

            #now validating for each column 
            # no need to check for 0-9 ( i overthought that part )

            #1st extracting a column 
            #note len(board)=9
            column=[]
            for j in range(len(board)):
                column.append(board[j][i])
            #we have the column now 

            #we will check the duplicate elements in column 
            for j in range(len(column)):
                for k in range(j+1, len(column)):
                    if column[k]=="." or column[j]==".":
                        continue
                    elif column[j]==column[k]:
                        return False # as duplicate value found 
                        
        # now validating each 3x3 box

        # box starting positions
        for start_row in range(0, 9, 3):
            for start_col in range(0, 9, 3):

                # extracting one 3x3 box
                box = []

                for i in range(start_row, start_row + 3):
                    for j in range(start_col, start_col + 3):
                        box.append(board[i][j])

                # now we have the box

                # checking duplicate elements in box
                for i in range(len(box)):
                    for j in range(i + 1, len(box)):

                        if box[i] == "." or box[j] == ".":
                            continue

                        elif box[i] == box[j]:
                            return False   # duplicate found  

        return True



                