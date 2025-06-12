from sklearn.linear_model import LinearRegression
import numpy as np

#First, we must import our data:
#So we import the arrays of x (house sizes) and y (prices) that we know as information
#Pretty sure they have to have at least 2 elements, cuz how do you make a line out of a single point, or even better, no data at all
#Pretty sure the amount of elements has to be the same
x = np.array([25, 100, 107, 200, 271, 299, 300])
y = np.array([75, 200, 215, 370, 495, 540, 550])

#Issue: scikit-learn wants a table-like 2D structure of the input for x
#Currently we're giving it a 1D array of the shape (7,), meaning we got our 7 rows but there's no columns
#Our current array is [25, 100, 107, 200, 271, 299, 300] and in order to transform into (7,1) (bacause we do, after all, have only 1 column) it needs to look like:
#[[25],
# [100],
# [107],
# ...]
#We can hardcode it like so, but that's not great, thankfully, there's a function that can transform it for us
#The numpy function array.reshape(rows, columns) does exactly that, as long as it's possible
#https://www.w3schools.com/python/numpy/numpy_array_reshape.asp
#By passing -1 as a parameter we tell it to only order the direction we need, and do the rest automatically, great if you don't know if the size of your array is 8, 16 or something else but know you want it in 2 columns (Note: will fail with non-divisible options)
#This is great for us because we only care that the column is 1
x = x.reshape(-1, 1) #1 column, however many rows
#We don't, however, reshape y as it's the list of results and it can only ever be 1D in our case

#Now our data is finally the way we need it and we can import it in the model
model = LinearRegression()
model.fit(x, y)

#Then if we want to predict a price, we use the now trained model, do note it still has to be in a 2D array format, thus the [[254]] instead of just 254
prediction = model.predict([[254]])
print(prediction)
