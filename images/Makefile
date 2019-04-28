
all: DRR.png DRR_res.png phase_space.png timescales.png timescales_novrr.png  s_stars_times.png disk_interaction.png example_0_model3_ex_subindex_0.png example_1_model3_ex_subindex_0.png example_2_model3_ex_subindex_0.png simple_R_f_enh_index_par1_0_index_par2_0_run02b_yscale_linear.png vrr_corr.png figIllustrationRandom.png  figIllustrationRandomFake.png sstars_few_P.png

s_stars_times.rplt: plot_sstars.py
	python $<

DRR_res.rplt: plot_DRR_res.py
	python $<

vrr_corr.rplt: plot_vrr_corr.py
	python $<

%.png: %.rplt matplotlibrc
	rplt --bb --savefig $@ $<


%.png: %.eps
	convert -density 400 $< -trim -transparent white -fill white -opaque black  $@
