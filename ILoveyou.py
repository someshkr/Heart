import numpy as np
import matplotlib.pyplot as plot
import math
#plot.rcParams["figure.figsize"] = (50,30)

'''
x^2 + (y - x ^ (2/3))^2 = 1
=> (y - x ^ (2/3))^2 = 1- (x^2)
=> y - x ^ (2/3) = sqrt(1 - (x^2))2
=> y = x^(2/3)-(sqrt(1-x^2))

'''
x = np.linspace(-1,1,200)
y = (np.cbrt(x ** 2))+(np.lib.scimath.sqrt(1-(x ** 2)))
z = (np.cbrt(x ** 2))-(np.lib.scimath.sqrt(1-(x ** 2)))

plot.plot(np.real(y))
plot.plot(np.real(z))

plot.xlabel('y')
#plot.ylabel('y = x^(2/3)-(sqrt(1-x^2)) ')
plot.ylabel('y = heart ')
plot.grid(True,which = 'both')
plot.show()
