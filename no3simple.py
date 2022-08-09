import numpy as np
arr = np.array([
    [4,0,0,1],
    [3,5,2,1],
    [0,4,1,1],
    [2,2,5,1]  
])
determinan = np.linalg.det(arr)
print("determinannya", determinan)
if(determinan <0):
    volume = determinan / -6
else:
    volume = determinan/6
print ("volumenya", volume)