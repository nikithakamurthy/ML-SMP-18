def Hypothesis(theta,x):

#Calculate the hypothesis function h(X1 , X2)

def Cost_Function(X,Y,theta,m):
	
#Calculate the cost function J


def Cost_Function_Derivative(X,Y,theta,j,m):
	
#Calculate derivatives dJ/dW1 and dJ/dW2

def Gradient_Descent(X,Y,theta, m, alpha):
	
#Perform the gradient descent update W1 = W1 - alpha* dJ/dW1 , W2 = W2 - alpha*dJ/dW2


def Linear_Regression(X,Y,alpha,theta,num_iters):
	m = len(X)
	for x in xrange(num_iters):
		new_theta = Gradient_Descent(X,Y,theta, m, alpha)
		theta = new_theta
		if x % 100 == 0:
			print 'theta ', theta
			print 'cost is ', Cost_Function(X,Y,theta,m)
	return new_theta



"""

After completing the functions , print the value of new_theta. Tell us what value you get

"""

# data to pass into the function as paramters 


# Y= [19, 20, 20.5, 21.5, 22, 23, 23, 25.5, 24]
# X = [[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7],[1,8],[1,9]]
#alpha = 0.1
#iterations = 2000
#Linear_Regression(x_raw,y_raw,alpha,theta,iterations)


    
