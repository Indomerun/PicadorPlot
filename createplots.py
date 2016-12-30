import matplotlib.pyplot as plt
import numpy as np
import transparentcolormaps as tc
from importdata import fetch_data


def add_plots(axes, plotSettings, frameNumber):
    loadedData = {}
    nPlots = len(plotSettings)
    for i in range(nPlots):
        add_plot(axes, plotSettings[i], loadedData, frameNumber)


def add_plot(axes, plotSettings, loadedData, frameNumber):
    data = fetch_data(plotSettings, loadedData, frameNumber)
    if plotSettings['plot_type'] == 'rgba':
        plot_rgba(axes, data, plotSettings)
        if 'show_cbar' in plotSettings.keys() and plotSettings['show_cbar']:
            plot_cbar(axes, plotSettings)
    elif plotSettings['plot_type'] == 'line':
        plot_line(axes, data, plotSettings)
    elif plotSettings['plot_type'] == 'xline':
        plot_xline(axes, data, plotSettings)
    elif plotSettings['plot_type'] == 'yline':
        plot_yline(axes, data, plotSettings)


def plot_rgba(axes, data, plotSettings):
    if plotSettings['data_type'] == '2D':
        data_RGBA = plotSettings['mappable'].to_rgba(data)
    elif plotSettings['data_type'] == 'bmp':
        data_RGBA = np.ones(data.shape)
        data_RGBA[..., :3] = np.flipud(data)/255
    ax = axes[plotSettings['ax']]
    im = ax.get_images()
    if len(im) == 0:
        blendedData = tc.alphaBlend(data_RGBA, np.ones(data_RGBA.shape))
        ax.imshow(blendedData, extent=plotSettings['plotExtent'], origin='lower', aspect='auto', interpolation='nearest')
        #ax.imshow(data_RGBA, extent=plotSettings['plotExtent'], origin='lower', aspect='auto', interpolation='nearest')
    elif len(im) == 1:
        imdata = im[0].get_array()
        blendedData = tc.alphaBlend(data_RGBA, imdata)
        #blendedData = tc.physicalBlend(data_RGBA, imdata)
        im[0].set_data(blendedData)


def plot_cbar(axes, plotSettings):
    if 'cax' in plotSettings.keys():
        cbar = plt.colorbar(plotSettings['cbar_mappable'], cax=axes[plotSettings['cax']])
    else:
        cbar = plt.colorbar(plotSettings['cbar_mappable'], ax=axes[plotSettings['ax']])
    if 'cbarlabel' in plotSettings.keys():
        cbar.set_label(plotSettings['cbarlabel'])


def plot_line(axes, data, plotSettings):
    ax = axes[plotSettings['ax']]
    ax.plot(np.linspace(plotSettings['Min'], plotSettings['Max'], data.size), data)


def plot_xline(axes, data, plotSettings):
    ax = axes[plotSettings['ax']]
    ax.plot(np.linspace(plotSettings['Min'], plotSettings['Max'], data.shape[1]), np.sum(data,0))


def plot_yline(axes, data, plotSettings):
    ax = axes[plotSettings['ax']]
    ax.plot(np.sum(data,1), np.linspace(plotSettings['Min'], plotSettings['Max'], data.shape[0]))


#def plot_line(axes, data, plotSettings):
#    ax = axes[plotSettings['ax']]
#    ax.plot(data[0, :], data[1, :])
