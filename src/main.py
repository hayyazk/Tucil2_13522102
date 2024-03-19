from dividenconquer import bezierDnC
from bruteforce import bezierBruteForce
from util import file_input, manual_input
import matplotlib.pyplot as plt
import time

inp_method = int(input("1. Command line\n2. File\n Pilih metode input: "))
while (inp_method != 1 and inp_method != 2):
    print("Input tidak sesuai.")
    inp_method = int(input("Pilih metode input: "))

if (inp_method == 1):
    xpoints, ypoints, n_iter = manual_input()
else:
    xpoints, ypoints, n_iter = file_input()

# Divide and Conquer
start = time.time()
plt.figure(1)
final = [[], []]
plt.plot(xpoints, ypoints, 'k.-', linewidth=0.25)
bezierDnC(xpoints, ypoints, n_iter, final)
plt.plot([xpoints[0]] + final[0] + [xpoints[2]], [ypoints[0]] + final[1] + [ypoints[2]], 'b.-', linewidth=2)
elapsed = time.time() - start
plt.title("Divide and Conquer")
plt.figtext(0, 0, 'Elapsed time = ' + str(elapsed))

#Brute Force
start = time.time()
plt.figure(2)
plt.plot(xpoints, ypoints, 'k.-', linewidth=0.25)
bezierBruteForce(xpoints, ypoints, n_iter)
elapsed = time.time() - start
plt.title("Brute Force")
plt.figtext(0, 0, 'Elapsed time = ' + str(elapsed))

plt.show()