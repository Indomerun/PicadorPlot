import sys
sys.path.insert(0, '/pfs/nobackup/home/j/joelm/PicadorPlot/')

import mappablesettings as ms
from plot import Plot

axesSettings = ms.AxesSettingsContainer()
plotSettings = ms.PlotSettingsContainer()


# --- Constants from Input --- #
X_Min=-0.0024486282601243417739178553915735392366
Y_Min=-0.0030486282601243420466163858151276144781
Z_Min=-0.0000003721470044097097224873517840731951
X_Max=0.0006000000000000000558580959264531884401
Y_Max=0.0030486282601243420466163858151276144781
Z_Max=0.0000003721470044097097224873517840731951


# --- Define Axes --- #
axesSettings.append(
name='XY',
axis_type='subplot',
nrows=2,
ncols=4,
row=0,
col=0,
rowspan=2,
colspan=2,
xlim=[X_Min, X_Max],
ylim=[Y_Min, Y_Max],
xlabel='$x$',
xunits=r'\textmu m',
xunits_value=1e-4,
ylabel='$y$',
yunits=r'\textmu m',
yunits_value=1e-4,
ticks_out='both',
aspect='equal'
)

"""
axesSettings.append(
name='XY_inset',
axis_type='zoomed_inset',
parent_axis='XY',
inset_zoom=2,
inset_position=4,
xlim=[X_Min / 5, X_Max / 5],
ylim=[Y_Min / 5, Y_Max / 5],
hide_ticks=True,
hide_ticklabels='both',
xunits_value=1e-4,
yunits_value=1e-4,
corner1=1,
corner2=3,
color="0.75"
)
"""

axesSettings.append(
name='Ex2D_cbar',
axis_type='axes',
position=[0.4, 0.55, 0.4+0.025, 0.55+0.35]
)

axesSettings.append(
name='Electron2D_cbar',
axis_type='axes',
position=[0.4, 0.1, 0.4+0.025, 0.1+0.35]
)

axesSettings.append(
name='pxpy',
axis_type='subplot',
nrows=2,
ncols=4,
row=0,
col=2,
xlim=[-1, 1],
ylim=[-1, 1],
xlabel='$p_x$',
#xunits=r'\textmu m',
ylabel='$p_y$',
#yunits=r'\textmu m',
ticks_out='both',
aspect='equal'
)

axesSettings.append(
name='xpx',
axis_type='subplot',
nrows=2,
ncols=4,
row=1,
col=2,
xlim=[-1, 1],
ylim=[-1, 1],
xlabel='$x$',
#xunits=r'\textmu m',
ylabel='$p_x$',
#yunits=r'\textmu m',
ticks_out='both',
aspect='equal'
)

axesSettings.append(
name='pxpy_transition',
axis_type='subplot',
nrows=2,
ncols=4,
row=0,
col=3,
xlim=[-1, 1],
ylim=[-1, 1],
xlabel='$p_x$',
#xunits=r'\textmu m',
ylabel='$p_y$',
#yunits=r'\textmu m',
ticks_out='both',
aspect='equal'
)

# --- Define Plots --- #
plotSettings.append(
name='Ex2D',
data_folder='./Angles/StructuredTargets_2016-12-30_11-37-47/BasicOutput/data/',
data='Ex2D',
axis='XY',
data_type='2D',     # metadata
plot_type='rgba',
size=(4*1024, 2*1024),     # metadata
xMin=X_Min,            # metadata
xMax=X_Max,            # metadata
yMin=Y_Min,            # metadata
yMax=Y_Max,            # metadata
cmap='{royalblue}{deepskyblue}t{orange}{darkorange}',
clim=(-2.5e8, 2.5e8),
norm='linear',
show_cbar=True,
cax='Ex2D_cbar',
vlabel=r'$E_x$',
vunits=r'cgs$/10^7$',
vunits_value=1e7
)

plotSettings.append(
name='Electron2D',
data_folder='./Angles/StructuredTargets_2016-12-30_11-37-47/BasicOutput/data/',
data='Electron2D',
axis='XY',
data_type='2D',     # metadata
plot_type='rgba',
size=(4*1024, 2*1024),     # metadata
xMin=X_Min,            # metadata
xMax=X_Max,            # metadata
yMin=Y_Min,            # metadata
yMax=Y_Max,            # metadata
cmap='tGk',
clim=(1e4, 1e7),
norm='log',
show_cbar=True,
cax='Electron2D_cbar',
vlabel=r'$N_e$',
vunits=r'cgs'
)

plotSettings.append(
name='Electron_px_py',
data_folder='./Angles/StructuredTargets_2016-12-30_11-37-47/BasicOutput/data/',
data='Electron_px_py',
axis='pxpy',
data_type='2D',     # metadata
plot_type='rgba',
size=(1024, 1024),     # metadata
xMin=-1,            # metadata
xMax=1,            # metadata
yMin=-1,            # metadata
yMax=1,            # metadata
#cmap='plasma',
clim=(1e3, 1e6),
norm='symlog',
show_cbar=True,
#cax='Electron2D_cbar',
#vlabel=r'$N_e$',
#vunits=r'cgs'
)

plotSettings.append(
name='Electron_x_px',
data_folder='./Angles/StructuredTargets_2016-12-30_11-37-47/BasicOutput/data/',
data='Electron_x_px',
axis='xpx',
data_type='2D',     # metadata
plot_type='rgba',
size=(1024, 1024),     # metadata
xMin=-1,            # metadata
xMax=1,            # metadata
yMin=-1,            # metadata
yMax=1,            # metadata
#cmap='plasma',
clim=(1e3, 1e6),
norm='symlog',
show_cbar=True,
#cax='Electron2D_cbar',
#vlabel=r'$N_e$',
#vunits=r'cgs'
)

plotSettings.append(
name='TransitDistribution(Electron_yTransit_px_py)',
data_folder='./Angles/StructuredTargets_2016-12-30_11-37-47/',
data='TransitDistribution(Electron_yTransit_px_py)',
axis='pxpy_transition',
data_type='2D',     # metadata
plot_type='rgba',
size=(1024, 1024),     # metadata
xMin=-1,            # metadata
xMax=1,            # metadata
yMin=-1,            # metadata
yMax=1,            # metadata
#cmap='plasma',
clim=(1e3, 1e6),
norm='symlog',
show_cbar=True,
#cax='Electron2D_cbar',
#vlabel=r'$N_e$',
#vunits=r'cgs'
)

Plot(axesSettings, plotSettings, outputFolder='output/')
