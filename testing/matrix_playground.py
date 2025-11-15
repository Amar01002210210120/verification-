import numpy as np
import matplotlib.pyplot as plt
def apply_matrix(A, points):
    return points @ A.T
def unit_square(num_points=100):
    t = np.linspace(0,1, num_points)
    bottom = np.c_[t, np.zeros_like(t)]
    right = np.c_[ np.ones_like(t), t]
    top = np.c_[t[::-1], np.ones_like(t)]
    left = np.c_[np.zeros_like(t), t[::-1]]
    square = np.vstack([bottom, right, top, left])
    return square 
def plot_transform(A, title="Matrix Transform"):
    square = unit_square()
    transformed = apply_matrix(A, square)
    plt.figure()
    plt.plot(square[:,0], square[:,1], label="Original")
    plt.plot(transformed[:,0], transformed[:,1], label="Transformed")
    plt.axhline(0, linewidth=0.5)
    plt.axhline(0, linewidth=0.5)
    plt.gca().set_aspect("equal", adjustable="box")
    plt.legend()
    plt.title(title)
    plt.grid(True)
    plt.show()
if __name__ == "__main__":
        A = np.array([[3,0],
                      [0,2]])

        plot_transform(A, title="M1 Stretch") # Python script meant to show matrix transformation just a little beta test for whats coming soon
