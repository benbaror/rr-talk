from replot import Axes
import h5py


def main():

    with h5py.File('BW_110.hdf5','r') as h5:
        D11 = h5['_drr_lnnp_cache'][str(dict(l=1,n=1,np=1,neval=100000))][0]
        D1m1 = h5['_drr_lnnp_cache'][str(dict(l=1,n=1,np=-1,neval=100000))][0]
        j = h5['j'].value

    ax = Axes('DRR_res.rplt')

    ax.set_xscale('log')
    ax.set_yscale('log')
    #ax.set_title('a = {:2.3} mpc'.format(drr.sma*1e3))
    ax.set_xlabel('$J/J_\mathrm{c}$')
    ax.set_ylabel('$D_{jj}$ [1/Myr]')
    ax.plot(j, D11 * 1e6, color='C1')
    ax.plot(j, D1m1 * 1e6, color='C2')
    ax.text(0.43, 5e-3, "(1:-1)", color='C2')
    ax.text(0.62, 5e-3, "(1:1)", color='C1')
    ax.set_xlim(0.08, 1)
    ax.set_ylim(1e-4, 3e-2)




if __name__ == '__main__':
    main()
