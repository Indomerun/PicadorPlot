import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import host_subplot
from mpl_toolkits.axes_grid1 import host_axes
import matplotlib.gridspec as gridspec
from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes
from mpl_toolkits.axes_grid1.inset_locator import mark_inset


def createAxes(axesSettings):
    axes = {}
    for axisSettings in axesSettings:
        axes[axisSettings['name']] = createAxis(axes, axisSettings)
    return axes


def createAxis(axes, axisSettings):
    ax = initializeAxis(axes, axisSettings)
    return ax


def initializeAxis(axes, axisSettings):

    # TODO: Add sharex and sharey
    if 'axes_type' not in axisSettings.keys() or axisSettings['axes_type'] == 'subplot':
        subplot2grid_required = ['nrows', 'ncols', 'row', 'col']
        subplot2grid_optional = ['rowspan', 'colspan']
        if 'nrows' not in axisSettings.keys():
            axisSettings.add_value('nrows', 1)
        if 'ncols' not in axisSettings.keys():
            axisSettings.add_value('ncols', 1)
        if 'row' not in axisSettings.keys():
            axisSettings.add_value('row', 0)
        if 'col' not in axisSettings.keys():
            axisSettings.add_value('col', 0)
        if 'rowspan' not in axisSettings.keys():
            axisSettings.add_value('rowspan', 1)
        if 'colspan' not in axisSettings.keys():
            axisSettings.add_value('colspan', 1)
        gs = gridspec.GridSpec(axisSettings['nrows'], axisSettings['ncols'])
        ax = host_subplot(gs[axisSettings['row']:axisSettings['row']+axisSettings['rowspan'], axisSettings['col']:axisSettings['col']+axisSettings['colspan']], adjustable='box-forced')
        return ax

    elif axisSettings['axes_type'] == 'axes':
        axes_required = ['position']
        axes_optional = []
        kwargs = {}
        for key, value in axisSettings.items():
            if key in axes_optional:
                kwargs[key] = value
        ax = host_axes(axisSettings[axes_required[0]], **kwargs)
        return ax

    # TODO: Add sharex and sharey
    elif axisSettings['axes_type'] == 'subplot':
        subplot2grid_required = ['nrows', 'ncols', 'row', 'col']
        subplot2grid_optional = ['rowspan', 'colspan']
        gs = gridspec.GridSpec(axisSettings['nrows'], axisSettings['ncols'])
        if 'rowspan' not in axisSettings.keys():
            axisSettings.add_value('rowspan', 1)
        if 'colspan' not in axisSettings.keys():
            axisSettings.add_value('colspan', 1)
        ax = host_subplot(gs[axisSettings['row']:axisSettings['row']+axisSettings['rowspan'], axisSettings['col']:axisSettings['col']+axisSettings['colspan']], adjustable='box-forced')
        return ax

    # TODO: Add inset that doesn't rely on 'zoom'
    # TODO: Allow mark_inset for arbitrary axes
    elif axisSettings['axes_type'] == 'zoomed_inset':
        zoomed_inset_required = ['parent_axes', 'zoom']
        zoomed_inset_optional = ['loc']
        mark_inset_required = ['parent_axes', 'loc1', 'loc2']
        mark_inset_optional = ['ec']

        kwargs = {}
        marked_kwargs = {}
        for key, value in axisSettings.items():
            if key in zoomed_inset_required or key in zoomed_inset_optional:
                if key == 'parent_axes':
                    kwargs[key] = axes[value]
                else:
                    kwargs[key] = value
            if key in mark_inset_required or key in mark_inset_optional:
                if key == 'parent_axes':
                    marked_kwargs[key] = axes[value]
                else:
                    marked_kwargs[key] = value
        ax = zoomed_inset_axes(**kwargs)
        if set(mark_inset_required).issubset(set(axisSettings.keys())):
            mark_inset(inset_axes=ax, fc='none', **marked_kwargs)
        return ax

    # TODO: Allow twin, twinx and twiny
    # TODO: Fix unit rescaling to work with parasite axes
    elif axisSettings['axes_type'] == 'parasite':
        twin_required = ['host_axes', 'axis']
        twin_optional = ['axis_shift']

        if axisSettings['axis'] == 'x':
            parent_axes = axes[axisSettings['host_axes']]
            ax = parent_axes.twinx()
            ax.yaxis.tick_right()
            if 'axis_shift' in axisSettings.keys():
                ax.get_yaxis().get_offset_text().set_x(axisSettings['axis_shift'])
                ax.spines["right"].set_visible(True)
                ax.spines["right"].set_position(("axes", axisSettings['axis_shift']))
            return ax

        elif axisSettings['axis'] == 'y':
            parent_axes = axes[axisSettings['host_axes']]
            ax = parent_axes.twiny()
            ax.xaxis.offsetText.set_visible(False)
            #ax.get_xaxis().get_offset_text().set_x(0)
            #ax.tick_params(axis='x', which='both', labelbottom='off', labeltop='on')
            #ax.xaxis.set_label_position('top')
            #ax.xaxis.tick_top()
            if 'axis_shift' in axisSettings.keys():
                ax.get_xaxis().get_offset_text().set_y(axisSettings['axis_shift'])
                ax.spines["top"].set_visible(True)
                ax.spines["top"].set_position(("axes", axisSettings['axis_shift']))
            return ax
