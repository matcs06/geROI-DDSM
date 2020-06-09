# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import numpy as np 
import cv2
import os

# %%
def prepArr(ovelayfilepath):

  arr = open(ovelayfilepath, "r")
  
  nums = ["0","1","2","3","4","5","6","7","8","9"]

  overlaycord = []

  count = 0

  for line in arr:
    count = count + 1
    if(count >= 9):
      if(line[0] in nums):
        print("Cordinates found in line: " + str(count))
      else:
        continue

      overlaycord = line
      
  overArr = overlaycord.split(" ")
  arr=[]
  for item in overArr:
    if(item != " "):
      arr.append(item)

  return arr    

def getXY(ovelayfilepath):
    # %%
    arr = []
    arr = prepArr(ovelayfilepath)
    x = 0
    y = 0
    xi = int(arr[0])
    yi = int(arr[1])
    xstatic = xi
    ystatic = yi
    i = 0

    #imagem = cv2.imread("./newImmage2.png", 0)


    # %%
    menorX = xstatic
    menorY = ystatic
    maiorX = xstatic
    maiorY = ystatic


    # %%
    while (arr[i]!="#\n"):
        
        if (arr[i] == "0"):
            x = 0
            y = -1
        
        if (arr[i] == "1"):
            x = 1
            y = -1

        if (arr[i] == "2"):
            x = 1
            y = 0

        if (arr[i] == "3"):
            x = 1
            y = 1

        if (arr[i] == "4"):
            x = 0
            y = 1

        if (arr[i] == "5"):
            x = -1
            y = 1 

        if (arr[i] == "6"):
            x = -1
            y = 0

        if (arr[i] == "7"):
            x = -1
            y = -1

        #passando o maior e manor valor das cordenadas de x e y
        if(xi > maiorX):
            maiorX = xi
        
        if(xi < menorX):
            menorX = xi
        
        if(yi > maiorY):
            maiorY = yi
        
        if(yi < menorY):
            menorY = yi

        #Incrementing xi and yi
        xi = xi + x
        yi = yi + y
        
        #cv2.line(imagem, (xstatic, ystatic), (xi, yi),(255,0,0), 10)
        i = i+1

    return [menorX, menorY, maiorX, maiorY]


if __name__ == '__main__':
    getXY()
