from replot import Axes
import numpy as np


def main():
    ax = Axes('vrr_corr.rplt')
    tnbody, nbody = np.loadtxt('resCtWMeanScaledMinus.csv', delimiter=',').T
    t, pred = np.loadtxt('predCtWNaiveScaledMinus.csv', delimiter=',').T
    t_show = np.logspace(-2,2, 100)
    nbody_show = np.interp(t_show,  tnbody, nbody)
    ax.plot(t_show, nbody_show, 'o', label='Effective N-body')
    ax.plot(t, pred, 'k', label='Analytical prediction')
    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.set_xlim(t[1], t[-1])
    ax.set_ylim(1e-3, 1.5)
    ax.set_xlabel('$\Delta t / T_\mathrm{VRR}$')
    ax.set_ylabel(r'$\langle|\Delta \mathbf{L}|^2\rangle$')
    ax.legend(loc=0)

if __name__ == '__main__':
    main()
