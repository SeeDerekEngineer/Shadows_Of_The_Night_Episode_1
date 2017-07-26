import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]
batX, batY = x0, y0
roundsLeft = n
prevXRight = w - 1
prevXLeft = 0
prevYUp = 0
prevYDown = h - 1


# game loop
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
    
    if bomb_dir == 'U':
        
        newBatY = math.ceil((abs(batY - prevYUp))/2)
        prevYUp = batY
        prevYDown = batY
        if newBatY == 0: newBatY = 1
        if (batY - newBatY) < 0:
            batY = 0
        else:
            batY -= newBatY
        
    elif bomb_dir == 'UR':
        
        newBatY = math.ceil((abs(batY - prevYUp))/2)
        prevYUp = batY
        prevYDown = batY
        if newBatY == 0: newBatY = 1
        if (batY - newBatY) < 0:
            batY = 0
        else:
            batY -= newBatY
        
        newBatX = math.ceil((abs(batX - prevXRight))/2)
        prevXLeft = batX
        prevXRight = batX
        if newBatX == 0: newBatX = 1
        if (batX + newBatX) >= w:
            batX = w - 1
        else:
            batX += newBatX
    
    elif bomb_dir == 'R':
       
        newBatX = math.ceil((abs(batX - prevXRight))/2)
        prevXLeft = batX
        prevXRight = batX
        if newBatX == 0: newBatX = 1
        if (batX + newBatX) >= w:
            batX = w - 1
        else:
            batX += newBatX
    
    elif bomb_dir == 'DR':
       
        newBatY = math.ceil((abs(batY - prevYDown))/2)
        prevYUp = batY
        prevYDown = batY
        if newBatY == 0: newBatY = 1
        if (batY + newBatY) >= h:
            batY = h - 1
        else:
            batY += newBatY
        
        newBatX = math.ceil((abs(batX - prevXRight))/2)
        prevXLeft = batX
        prevXRight = batX
        if newBatX == 0: newBatX = 1
        if (batX + newBatX) >= w:
            batX = w - 1
        else:
            batX += newBatX
    
    elif bomb_dir == 'D':
        
        newBatY = math.ceil((abs(batY - prevYDown))/2)
        prevYUp = batY
        prevYDown = batY
        if newBatY == 0: newBatY = 1
        if (batY + newBatY) >= h:
            batY = h - 1
        else:
            batY += newBatY
    
    elif bomb_dir == 'DL':
        
        newBatY = math.ceil((abs(batY - prevYDown))/2)
        prevYUp = batY
        prevYDown = batY
        if newBatY == 0: newBatY = 1
        if (batY + newBatY) >= h:
            batY = h - 1
        else:
            batY += newBatY
        
        newBatX = math.ceil((abs(batX - prevXLeft))/2)
        prevXRight = batX
        prevXLeft = batX
        if newBatX == 0: newBatX = 1
        if (batX - newBatX) < 0:
            batX = 0
        else:
            batX -= newBatX
    
    elif bomb_dir == 'L':
        
        newBatX = math.ceil((abs(batX - prevXLeft))/2)
        prevXRight = batX
        prevXLeft = batX
        if newBatX == 0: newBatX = 1
        if (batX - newBatX) < 0:
            batX = 0
        else:
            batX -= newBatX
    
    elif bomb_dir == 'UL':
        
        newBatY = math.ceil((abs(batY - prevYUp))/2)
        prevYUp = batY
        prevYDown = batY
        if newBatY == 0: newBatY = 1
        if (batY - newBatY) < 0:
            batY = 0
        else:
            batY -= newBatY
        
        newBatX = math.ceil((abs(batX - prevXLeft))/2)
        prevXRight = batX
        prevXLeft = batX
        if newBatX == 0: newBatX = 1
        if (batX - newBatX) < 0:
            batX = 0
        else:
            batX -= newBatX
    
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    

    # the location of the next window Batman should jump to.
    print(batX, batY)
