import pandas as pd
from astropy import table
from astropy import units
import numpy as np

from replot import Axes

import matplotlib.pyplot as plt


def add_main_seq(sstars, data_path):
    """
    Add the main zero age sequence properties of the S-stars based on their K magnitude
    assuming distance 'r0' and K-band extinction of 'a_k'
    Matching S-stars K magnitude to
    Solar model ZAMainSeq_Z020.dat (Schaller et al 1992)
    """
    r0 = 8.1e3 # [pc]  Gravity Collaboration, 2018, A&A, 615, 10
    a_k = 2.4  # Fritz et al. 2011


    main_seq =  pd.read_csv(data_path + '/ZAMainSeq_Z020.dat',
                            sep='\s+', comment='#',
                            header=0, index_col=0)

    kmag = (sstars.Kmag - 5 * (np.log10(r0) - 1) - a_k).values

    sstars['zms_age'] = np.interp(kmag, main_seq.K, main_seq.T_MS/1e6)
    sstars['zms_mass'] = np.interp(kmag, main_seq.K, main_seq.M)
    sstars['zms_radius'] = np.interp(kmag, main_seq.K, main_seq.R)




def get_sstars_data(data_path='./data/'):
    """
    Get the orbital properties of the S-stars from  (Gillessen et al. 2017)
    and their zero age main sequence properties
    """

    R0 = 8.32e3 # [pc] (Gillessen et al. 2017)
    _TO_PC = (units.au/units.pc).to('')

    # Disk stars defined in Gillessen et al. 2017
    DISK_STARS = ('S66', 'S67', 'S83', 'S87', 'S91', 'S96', 'S97', 'R44')


    sstars = table.Table.read(data_path + '/apjaa5c41t3_mrt.txt',
                              format='cds').to_pandas().set_index('Star')
    stars_ages = pd.read_csv(data_path + '/apjaa876ft2_ascii.txt',
                            sep='\s+', comment='#',
                            header=0, index_col=0)
    sstars = sstars.join(stars_ages)
    sstars['sma'] = sstars.a*R0*_TO_PC
    sstars['sma_err'] = sstars.e_a*R0*_TO_PC
    sstars['disk'] =  sstars.index.to_series().apply(lambda x: x in DISK_STARS)
    add_main_seq(sstars, data_path)
    return sstars



if __name__ == '__main__':

    ax = Axes('s_stars_times.rplt')

    s_stars = get_sstars_data('./data/')

    s_stars = s_stars[s_stars.sma > 0]
    s_stars = s_stars[(s_stars.SpT  == 'e') | (s_stars.SpT  == 'l')]

    disk = s_stars[s_stars.disk]
    early_type = s_stars[s_stars.SpT == 'e']
    late_type = s_stars[s_stars.SpT == 'l']

    habibi_stars = s_stars[s_stars.age > 0]

    ax.plot(disk.sma, disk.zms_age, 'o', label='CW disk stars', mec=None, ms=10)

    # plt.plot(hills_stars.sma, hills_stars.zms_age, 'or', label='Hills stars',
    #          mec=None)

    ax.errorbar(early_type.sma, early_type.zms_age, xerr=early_type.sma_err,
                 fmt='k.',
                 label='Early type stars (ZMSA)')

    # ax.errorbar(late_type.sma, late_type.zms_age, xerr=late_type.sma_err,
    #              fmt='.',
    #              label='Late type stars')

    min_age = 1.0
    ax.set_ylim(min_age, 1e3)
    age_err_low = np.maximum(habibi_stars.age_err_low,
                              habibi_stars.age - min_age)

    ax.errorbar(habibi_stars.sma, habibi_stars.age,
                 yerr=np.array([age_err_low,  habibi_stars.age_err_high]),
                 fmt='.',
                 label='Habibi et al. 2019')



    for star, params in early_type.iterrows():
        ax.annotate(star, (params.sma, params.zms_age),
                     xytext=(params.sma*0.95,
                             params.zms_age*1.09),
                     color='C4',
                     fontsize=6, zorder=10)

    ax.set_xlim(1e-4, 1.0)
    ax.set_ylim(1.0, 1e4)
    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.set_xlabel('Semi-major axis $[\mathrm{pc}]$')
    ax.set_ylabel('Age $[\mathrm{Myr}]$')

    ax.legend(loc=2)
