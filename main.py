layout = eval(input("Enter layout (in one line): "))

m = len(layout) # total number of rows
n = len(layout[0]) # total number of columns

teams = []

def find_team_else_create(i, j):
    # check vertically above (up)
    if (type(layout[i-1][j]) == type(str()) and (i - 1) >= 0): # part of existing team
        index = int(layout[i-1][j])
        teams[index] += 1
        layout[i][j] = str(index)
    
    # check horizontally below (left)
    elif (type(layout[i][j-1]) == type(str() and (j - 1) >= 0)): # part of existing team
        index = int(layout[i][j-1])
        teams[index] += 1
        layout[i][j] = str(index)
    
    # no team found
    else:
        teams.append(1) # create a new team
        layout[i][j] = str((len(teams)-1)) # replace layout position with index of team

for i in range(0, m):
    for j in range(0, n):
        if layout[i][j] == 1:
            find_team_else_create(i,j)


teams.sort(reverse=True)
output = '{0} teams of {1} totaling {2}'.format(len(teams), teams, sum(teams))

print(output)