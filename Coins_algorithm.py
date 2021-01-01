#######################################################################################################################
## Converts value (an int representing a value in coins) into coins of size 1, 3, or 4, with the mission ...         ##
## to use the least amount of coins possible.                                                                        ##
## My solution uses a brute-force strategy, but uses dynamic programming to make the calculations very fast and cheap##
#######################################################################################################################

def changeCalculator(value:int)-> arr:
    """
    Returns an array - each index represents a value and the integer at that index represents the minimum number of coins at that point. 
    For example: 
    DP[34] = 9 (9 coins is the minimum number of coins that can get you to a value of 34) 
    DP[0] = 0 (it takes 0 coins to get to a value of 0) 
    """
    #coins are value 1, 3, and 4
    
    DP = []
    DP.append(0)
    for i in range(1, value + 1):
        winner = -1
        coins1val = i - 1
        coins3val = i - 3
        coins4val = i - 4
        if coins1val >= 0:
            coins1val = DP[i - 1] + 1
            winner = coins1val

        if coins3val >= 0:
            coins3val = DP[i - 3] + 1
            if coins3val < winner:
                winner = coins3val

        if coins4val >= 0:
            coins4val = DP[i - 4] + 1
            if coins4val < winner:
                winner = coins4val
        DP.append(winner)
    return DP


print(changeCalculator(34)) 
