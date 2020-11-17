import numpy as np
import pandas as pd
"""
(1) Create a structured array with desired data:


"""
#(1) Create a structured arrary with desired data:
data = np.array([['','Col1','Col2'],
                 ['Row 1',1,2],
                 ['Row 2',2,3]])
dataframe = pd.DataFrame(data=data[1:,1:],
                         index=data[1:,0],
                         columns = data[0,1:])
print(dataframe)
#we need to generate sample space
"""
def is_independent(x_vals,x_probs,y_vals,y_probs: list):
    for x in range(0,len(x_vals)):
        for y in range(0,y_vals):
            if x_probs[x]*y_probs[y] !=
"""