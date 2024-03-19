from util import mid_point
import matplotlib.pyplot as plt

def outer_midpoints(xpoints, ypoints):
    xpoints.insert(1, mid_point(xpoints[0], xpoints[1]))
    ypoints.insert(1, mid_point(ypoints[0], ypoints[1]))
    n = len(xpoints)
    for i in range(2, n-1):
        xpoints[i] = mid_point(xpoints[i], xpoints[i+1])
        ypoints[i] = mid_point(ypoints[i], ypoints[i+1])

def inner_midpoints(xpoints, ypoints):
    innerx = []
    innery = []
    n = len(xpoints)
    for i in range (1, n-2):
        innerx.append(mid_point(xpoints[i], xpoints[i+1]))
        innery.append(mid_point(ypoints[i], ypoints[i+1]))
    return innerx, innery
    
def bezierBruteForce(xpoints, ypoints, iter):

    outer_midpoints(xpoints, ypoints)
    plt.plot(xpoints, ypoints, 'k.-', linewidth=0.25)
    innerx, innery = inner_midpoints(xpoints, ypoints)

    if (iter == 1):
        innerx.insert(0, xpoints[0])
        innery.insert(0, ypoints[0])
        innerx.append(xpoints[-1])
        innery.append(ypoints[-1])

        plt.plot(innerx, innery, 'b.-', linewidth=2)
    else:
        for i in range (1, len(innerx) + 1):
            xpoints.insert(i*2, innerx[i-1])
            ypoints.insert(i*2, innery[i-1])
        
        bezierBruteForce(xpoints, ypoints, iter-1)