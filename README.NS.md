# finalphaseone
This is phase one of the final project for fall 18 python

## This will allow us to print Summary Statistics for All Fields##
print(df.describe(include='all'))

## Count the number of Nulls prior to assigning the mean. This code provides more detail if applied after the column header renaming## 
null_counts = df.isnull().sum()
null_counts[null_counts > 0].sort_values(ascending= False)

print(null_counts[null_counts > 0].sort_values(ascending=False))
