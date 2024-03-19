from util import mid_point
import matplotlib.pyplot as plt

def mid_of_three(xpoints, ypoints):
    x1, x2 = mid_point(xpoints[0], xpoints[1]), mid_point(xpoints[1], xpoints[2])
    y1, y2 = mid_point(ypoints[0], ypoints[1]), mid_point(ypoints[1], ypoints[2])
    return [x1, mid_point(x1, x2), x2], [y1, mid_point(y1, y2), y2]

def bezierDnC(xpoints, ypoints, iter, final):

    if (iter > 0):
        xmid, ymid = mid_of_three(xpoints, ypoints)
        plt.plot(xmid, ymid, 'k.-', linewidth=0.25)
        #left
        bezierDnC([xpoints[0]] + xmid[:2], [ypoints[0]] + ymid[:2], iter-1, final)
        final[0].append(xmid[1])
        final[1].append(ymid[1])
        #right
        bezierDnC(xmid[-2:] + [xpoints[2]], ymid[-2:] + [ypoints[2]], iter-1, final)