import matplotlib.pyplot as plt
import numpy as np

x=np.arange(-10,10,0.1)
y=x**2
y2=x**2+4*x+4

plt.title("function")
plt.xlabel("x")
plt.ylabel("y")
plt.plot(x,y,label="X^2")
plt.plot(x,y2,label="X^2+4X+4")
plt.legend()
plt.show()


