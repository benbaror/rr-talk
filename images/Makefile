
all: DRR.png DRR_res.png phase_space.png timescales.png  s_stars_times.png disk_interaction.png

s_stars_times.rplt: plot_sstars.py
	python $<

DRR_res.rplt: plot_DRR_res.py
	python $<

%.png: %.rplt matplotlibrc
	rplt --bb --savefig $@ $<




disk_interaction.png:  figIllustrationInteraction.eps
	convert -density 400 $< -trim -transparent white -fill white -opaque black  $@
