# house-predictor-one-arg

With linear regression we're looking for a straight line (y = w*x + b) that fits the best to our data points (list of x)

The best fit is the one, such that with w and b the sum of all squared errors (the distance of each point to the line) is the smallest possible. We use squared errors instead of normal ones to penalize larger errors more.

As this is simple linear regression we will use points with x and y, meaning we'll be basing the prices (y) on only 1 parameter (x), which, in our case will be the houses' sizes.

Our input will be a 2 arrays - house size (x) as a column and price (y) (what we're predicting) as a separate 1D array.

When we calculate the line's slope (w) and y-intercept (b), we'll be able to input any x and predict it's price by calculating the y of the point using the equation above.

The libraries used are sklearn, specifically the LinearRegression module, and numpy for array operations.
