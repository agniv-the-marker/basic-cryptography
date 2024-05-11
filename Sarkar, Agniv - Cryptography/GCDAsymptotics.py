from matplotlib import pyplot as plt
from collections import Counter
from math import log2
import numpy as np
import matplotlib.patches as mpatches

def gcd_steps(a, b):
    if b == 0: return 1
    return gcd_steps(b, a%b) + 1

def plot_2d_function(f, n=10, s=1, cmap='gist_ncar'):
  """Plot the value of f(a,b) for each
        a, b in [0, ..., n-1].
  """
  X = np.array([[f(i,j) for i in range(j % s, n, s)] for j in range(0, n, s)])
  im = plt.imshow(X, cmap=cmap)
  values = range(X.max() + 1)
  colors = [ im.cmap(im.norm(value)) for value in values]
  plt.legend(handles=patches, bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0. )

  plt.xlabel(f'{s}a')
  plt.ylabel(f'{s}b')
  plt.gca().invert_yaxis()
  plt.show()

def plot_gcd_scatter(n=4000):
    avg = []
    data = set()
    for b in range(1, n):
      s = 0
      for a in range(1, b):
        steps = gcd_steps(a, b)
        s += steps
        data.add((b, steps))
      if b > 0:
        s /= b
      else:
        s = 0
        data.add((b, 0))
      avg.append(s)

    plt.scatter([d[0] for d in data], [d[1] for d in data], c='red')
    plt.scatter(list(range(1, n)), avg, c='blue')
    plt.plot(list(range(1, n)), [1.45 * log2(b) + 1.68 for b in range(1, n)], c='pink')
    plt.plot(list(range(1, n)), [0.85 * log2(b) + 0.14 for b in range(1, n)], c='cyan')

    plt.xlabel('b')
    plt.ylabel('Average steps to compute gcd(a, b)')
    plt.xscale('log')
    plt.show()

if __name__ == "__main__":
    plot_gcd_scatter()