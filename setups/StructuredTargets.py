# import sys
# sys.path.insert(0, './Joels')

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
ncols=2,
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
position=[0.85, 0.7, 0.85+0.025, 0.7+0.25]
)

axesSettings.append(
name='Electron2D_cbar',
axis_type='axes',
position=[0.85, 0.4, 0.85+0.025, 0.4+0.25]
)

"""
axesSettings.append(
name='XY_inset_inset',
axis_type='zoomed_inset',
parent_axis='XY_inset',
inset_zoom=2,
inset_position=1,
xlim=[-1e-4, 1e-4],
ylim=[-1e-4, 1e-4],
hide_ticks=True,
hide_ticklabels='both',
xunits_value=1e-4,
yunits_value=1e-4,
corner1=2,
corner2=4,
color="0.75"
)
"""

# --- Define Plots --- #
plotSettings.append(
name='Ex2D',
data_folder='/Volumes/My Passport/StructuredTargets/1/',
data='Ex2D',
axis='XY',
data_type='2D',     # metadata
plot_type='rgba',
size=(1024, 1024),     # metadata
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
data_folder='/Volumes/My Passport/StructuredTargets/1/',
data='Electron2D',
axis='XY',
data_type='2D',     # metadata
plot_type='rgba',
size=(1024, 1024),     # metadata
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

Plot(axesSettings, plotSettings, outputFolder='output/', i=256)
