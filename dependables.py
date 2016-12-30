import matplotlib as mpl
import transparentcolormaps as tc
import numpy as np


def calculate_dependables(axesSettings, plotSettings):
    for settings in plotSettings:
        for axisSettings in axesSettings:
            if axisSettings['name'] == settings['ax']:
                axSettings = axisSettings
        calculateDependables(axSettings, settings, axesSettings)


def calculateDependables(axisSettings, plotSettings, axesSettings):
    # Get rescaling factors for parasite axes from host axes
    if 'axes_type' in axisSettings.keys() and axisSettings['axes_type'] == 'parasite':
        for aSettings in axesSettings:
            if aSettings['name'] == axisSettings['host_axes']:
                if 'axis' in axisSettings.keys() and axisSettings['axis'] == 'x':
                    axisSettings.add_value('xunits_value', aSettings['xunits_value'])
                if 'axis' in axisSettings.keys() and axisSettings['axis'] == 'y':
                    axisSettings.add_value('yunits_value', aSettings['yunits_value'])

    # Get axis rescaling factors for plot settings from axes settings
    for dim in ['x', 'y']:
        key = dim + 'units_value'
        plotSettings.add_value(key, 1)
        if key in axisSettings.keys():
            plotSettings.add_value(key, axisSettings[key])

    if plotSettings['plot_type'] == 'xline':
        plotSettings.add_value('Min', plotSettings['xMin']/plotSettings['xunits_value'])
        plotSettings.add_value('Max', plotSettings['xMax']/plotSettings['xunits_value'])

    if plotSettings['plot_type'] == 'yline':
        plotSettings.add_value('Min', plotSettings['yMin']/plotSettings['yunits_value'])
        plotSettings.add_value('Max', plotSettings['yMax']/plotSettings['yunits_value'])

    if plotSettings['plot_type'] == 'line':
        if 'axis' not in plotSettings.keys() or plotSettings['axis'] == 'x':
            plotSettings.add_value('Min', plotSettings['xMin']/plotSettings['xunits_value'])
            plotSettings.add_value('Max', plotSettings['xMax']/plotSettings['xunits_value'])
        elif plotSettings['axis'] == 'y':
            plotSettings.add_value('Min', plotSettings['xMin']/plotSettings['yunits_value'])
            plotSettings.add_value('Max', plotSettings['xMax']/plotSettings['yunits_value'])

    if plotSettings['plot_type'] == 'rgba':
        # Get axis rescaling factors
        if 'cbarunits_value' not in plotSettings.keys():
            plotSettings.add_value('cbarunits_value', 1)

        # Rescale extent according to units
        plotExtent = np.array([plotSettings['xMin'], plotSettings['xMax'], plotSettings['yMin'], plotSettings['yMax']])
        plotExtent[:2] = plotExtent[:2] / plotSettings['xunits_value']
        plotExtent[2:] = plotExtent[2:] / plotSettings['yunits_value']
        plotSettings.add_value('plotExtent', plotExtent)


        if plotSettings['data_type'] == '2D':
            # Defaults
            if 'norm' not in plotSettings.keys():
                plotSettings.add_value('norm', 'linear')
            if 'cmap' not in plotSettings.keys():
                plotSettings.add_value('cmap', 'viridis')

            # norm
            if 'norm' in plotSettings.keys():
                if plotSettings['norm'] == 'linear':
                    if 'clim' not in plotSettings.keys():
                        cbar_norm = norm = mpl.colors.Normalize()
                    else:
                        norm = mpl.colors.Normalize(vmin=plotSettings['clim'][0], vmax=plotSettings['clim'][1])
                        cbar_norm = mpl.colors.Normalize(vmin=plotSettings['clim'][0] / plotSettings['cbarunits_value'], vmax=plotSettings['clim'][1] / plotSettings['cbarunits_value'])
                if plotSettings['norm'] == 'log':
                    if 'clim' not in plotSettings.keys():
                        cbar_norm = norm = mpl.colors.LogNorm()
                    else:
                        norm = mpl.colors.LogNorm(vmin=plotSettings['clim'][0], vmax=plotSettings['clim'][1])
                        cbar_norm = mpl.colors.LogNorm(vmin=plotSettings['clim'][0] / plotSettings['cbarunits_value'], vmax=plotSettings['clim'][1] / plotSettings['cbarunits_value'])
                if plotSettings['norm'] == 'symlog':
                    if 'clim' not in plotSettings.keys():
                        cbar_norm = norm = mpl.colors.SymLogNorm()
                    else:
                        norm = mpl.colors.SymLogNorm(plotSettings['clim'][0], vmin=plotSettings['clim'][0], vmax=plotSettings['clim'][1])
                        cbar_norm = mpl.colors.LogNorm(vmin=plotSettings['clim'][0] / plotSettings['cbarunits_value'], vmax=plotSettings['clim'][1] / plotSettings['cbarunits_value'])

            plotSettings.add_value('norm', norm)
            plotSettings.add_value('cbar_norm', cbar_norm)

            # cmap
            try:
                tc.make_alphablended_cmap(plotSettings['cmap'], 'cbar_'+plotSettings['cmap'])
            except ValueError:
                tc.make_linear_colormap(plotSettings['cmap'], plotSettings['cmap'])
                tc.make_alphablended_cmap(plotSettings['cmap'], 'cbar_'+plotSettings['cmap'])
            except AttributeError:
                tc.make_linear_colormap(plotSettings['cmap'], plotSettings['cmap'])
                tc.make_alphablended_cmap(plotSettings['cmap'], 'cbar_'+plotSettings['cmap'])

            # mappable
            mappable = mpl.cm.ScalarMappable()
            mappable.set_array((0, 1))
            mappable.set_cmap(plotSettings['cmap'])
            mappable.set_norm(plotSettings['norm'])
            plotSettings.add_value('mappable', mappable)

            cbar_mappable = mpl.cm.ScalarMappable()
            cbar_mappable.set_array((0, 1))
            cbar_mappable.set_cmap('cbar_'+plotSettings['cmap'])
            cbar_mappable.set_norm(plotSettings['cbar_norm'])
            plotSettings.add_value('cbar_mappable', cbar_mappable)
