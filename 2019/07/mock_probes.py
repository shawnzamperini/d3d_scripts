import oedge_plots
import pretty_plots as pp
import matplotlib.pyplot as plt

ncpath_unf = '/mnt/c/Users/Shawn/Documents/d3d_work/DIVIMP Runs/archive/Z0-167196-003.nc'
ncpath_fav = '/mnt/c/Users/Shawn/Documents/d3d_work/DIVIMP Runs/Z0-167196-064.nc'
datpath_unf = '/mnt/c/Users/Shawn/Documents/d3d_work/DIVIMP Runs/archive/Z0-167196-003.dat'
datpath_fav = '/mnt/c/Users/Shawn/Documents/d3d_work/DIVIMP Runs/Z0-167196-064.dat'

#ymin = -0.3; ymax = 0.4
#ymin = -0.5; ymax = 0.4
ymin = -0.4; ymax = 0.5

op_unf = oedge_plots.OedgePlots(ncpath_unf)
op_unf.add_dat_file(datpath_unf)
op_fav = oedge_plots.OedgePlots(ncpath_fav)
op_fav.add_dat_file(datpath_fav)

# A fake probe inserted on MiMES at the OMP.
omp_df_unf = op_unf.fake_probe(2.21, 2.36, -0.185, -0.185, 'Mach')
omp_df_fav = op_fav.fake_probe(2.21, 2.36, -0.185, -0.185, 'Mach')

# A fake crown area probe.
crown_df_unf = op_unf.fake_probe(1.5, 1.5, 0.915, 1.12, 'Mach')
crown_df_fav = op_fav.fake_probe(1.5, 1.5, 0.915, 1.12, 'Mach')

# A fake IMP probe.
imp_df_unf = op_unf.fake_probe(1.03, 1.09, 0, 0, 'Mach')
imp_df_fav = op_fav.fake_probe(1.03, 1.09, 0, 0, 'Mach')

# A fake inner divertor probe.
it_df_unf = op_unf.fake_probe(1.04, 1.04, -1.16, -0.9, 'Mach')
it_df_fav = op_fav.fake_probe(1.04, 1.04, -1.16, -0.9, 'Mach')

# A fake outer divertor probe.
ot_df_unf = op_unf.fake_probe(1.42, 1.7, -1.24, -1.24, 'Mach')
ot_df_fav = op_fav.fake_probe(1.42, 1.7, -1.24, -1.24, 'Mach')

# Create the figure and plot areas.
fig = plt.figure(figsize=(9,8))
ax_omp   = fig.add_subplot(336)
ax_crown = fig.add_subplot(332)
ax_imp   = fig.add_subplot(334)
ax_it    = fig.add_subplot(337)
ax_ot    = fig.add_subplot(339)

# Add the actual plots.
def add_plot(ax, df, color):
    ax.plot(df['Psin'], df['Mach']*-1, color=color, lw=3)
    ax.set_xlim([1.0, 1.1])
    ax.set_ylim([ymin, ymax])
    ax.axhline(color='k', linestyle='--')

add_plot(ax_omp,   omp_df_unf,   pp.tableau20[6])
add_plot(ax_crown, crown_df_unf, pp.tableau20[6])
add_plot(ax_imp,   imp_df_unf,   pp.tableau20[6])
add_plot(ax_it,    it_df_unf,    pp.tableau20[6])
add_plot(ax_ot,    ot_df_unf,    pp.tableau20[6])

add_plot(ax_omp,   omp_df_fav,   pp.tableau20[8])
add_plot(ax_crown, crown_df_fav, pp.tableau20[8])
add_plot(ax_imp,   imp_df_fav,   pp.tableau20[8])
add_plot(ax_it,    it_df_fav,    pp.tableau20[8])
add_plot(ax_ot,    ot_df_fav,    pp.tableau20[8])

fig.tight_layout()
fig.show()
