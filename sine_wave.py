import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

L = [10, 12]


def sine(i):
    sinegraph.set_data(X[:i], Y[:i])
    dot.set_data(X[i], Y[i])


for l in L:
    X = np.linspace(0, 4 * np.pi, 100)
    Y = np.sin(X)

    fig, ax = plt.subplots(1, 1)
    # plt.title('10 seconds')
    plt.title('{} seconds'.format(l))

    ax.set_xlim([0, 4 * np.pi])
    ax.set_ylim([-1.1, 1.1])

    sinegraph, = ax.plot([], [])
    dot, = ax.plot([], [], 'o', color='red')
    print(len(X))
    # anim = animation.FuncAnimation(fig, sine, frames=len(X), interval=500)
    anim = animation.FuncAnimation(fig, sine, frames=len(X), interval=200)
    # anim = animation.FuncAnimation(fig, sine, frames=60, interval=1)

    # 12.5
    # anim.save(r'sine_wave_12s.gif', writer="imagemagick", fps=8)

    # 10
    # anim.save(r'sine_wave_10s.gif', writer="imagemagick", fps=5)
    anim.save(r'sine_wave_{}s.gif'.format(l), writer="imagemagick", fps=len(X) / l / 2)
    print("save {} gif".format(l))
    # plt.show()
