# importing libraries
import pandas as pd
import numpy as np


num = {'strings': [1, 2, 3, 4, 5, None,
                    6, None, 7, 8, None]}

# Create the dataframe
df = pd.DataFrame(num, columns=['strings'])

# applying the method
count_nan = df['strings'].isna().sum()

# printing the number of values present
# in the column
print('Number of NaN values present: ' + str(count_nan))