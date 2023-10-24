import numpy as np
from sympy import Abs, symbols, S, Max, Min, solve
from sympy.abc import x, y

INPUT_FROM_USER = False

#-------------------
#BOTTLENECK DISTANCE
#-------------------

#Numpy Bottleneck (no symbolic calculus)
def bottleneck(p,q):
    #p, q points the upper diagonal half-plane of R^2
    max1 = np.max([np.abs(p[0]-q[0]),np.abs(p[1]-q[1])])
    max2 = np.max([(p[1]-p[0])/2, (q[1]-q[0])/2])
    return np.min([max1,max2])

#Sympy Bottleneck (with symbolic calculus)
def symBottleneck(u,v):
    #u, v points the upper diagonal half-plane of R^2
    p0,p1,q0,q1 = symbols("p0,p1,q0,q1")
    m1 = Max(Abs(p0-q0), Abs(p1-q1))
    m2 = Max((p1-p0)/2, (q1-q0)/2)
    return Min(m1,m2).subs({p0:u[0],p1:u[1],q0:v[0],q1:v[1]})

#----------------
#POSITION THEOREM
#----------------

#Intersection between filtering line and contour
def intersImproper(va,f):
    #Intersects r_{(a,b)} with contour of equation f
    b = symbols("b")
    equations = [f, (1-va)*x - va*y - b]
    return solve(equations, x, y, dict=True)

def main():
    """ Main program """
    if INPUT_FROM_USER:
        notvalid = True
        while notvalid:
            p0,p1 = input("Enter point p coordinates:").split()
            if p0 > p1:
                print("The point p does not belong to the upper half-plane. Choose another point.")
            else: 
                notvalid = False
        notvalid = True
        while notvalid:
            q0,q1 = input("Enter point q coordinates:").split()
            if q0 > q1:
                print("The point q does not belong to the upper half-plane. Choose another point.")
            else: 
                notvalid = False
        p = [int(p0),int(p1)]
        q = [int(q0),int(q1)]

        print(bottleneck(p,q))

    bot = symBottleneck([0,1],[0,2])
    print(bot)

    x1,x2,x3,x4,x5,b = symbols("x1,x2,x3,x4,x5,b")
    f = x**2 + y**2 - x5**2
    print(intersImproper(1/2,f))

if __name__ == "__main__":
    main()