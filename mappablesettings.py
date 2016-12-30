import auxiliaries as aux


class MappableSettings(object):
    _default_mappings = {}

    def __init__(self, **settings):
        self._settings = settings.copy()

        self._mappings = self._default_mappings
        self._is_mapped = False

    def set_settings(self, settings):
        self._settings = settings.copy()
        self._is_mapped = False

    def set_mappings(self, mappings):
        self._mappings = mappings.copy()
        self._is_mapped = False

    def map_settings(self):
        self._mapped_settings = {}
        for key, value in self._mappings.items():
            try:
                if type(value) == str:
                    if value == '':
                        self._mapped_settings[key] = self._settings[key]
                    else:
                        self._mapped_settings[key] = self._settings[value]
                else:
                    self._mapped_settings[key] = value(self._settings)
            except KeyError:
                pass
        self._is_mapped = True

    def __getitem__(self, key):
        return self._mapped_settings[key]

    def keys(self):
        return self._mapped_settings.keys()

    def values(self):
        return self._mapped_settings.values()

    def items(self):
        return self._mapped_settings.items()

    def add_dependencies(self, dependencies):
        for key, value in dependencies.items():
            self._mapped_settings[key] = value

    def add_value(self, key, value):
        self._mapped_settings[key] = value


class FigureSettings(MappableSettings):
    _default_mappings = dict(name='',
                             pixels='')


class AxisSettings(MappableSettings):
    _default_mappings = dict(name='',
                             axes_type='axis_type',

                             # axis_type = 'subplot'
                             nrows='',
                             ncols='',
                             row='',
                             col='',
                             shape=lambda x: [x['nrows'], x['ncols']],
                             loc=lambda x: [x['row'], x['col']] if ('row' in x.keys() and 'col' in x.keys()) else x['inset_position'],
                             rowspan='',
                             colspan='',

                             # axis_type = 'axes'
                             position=lambda x: [x['position'][0], x['position'][1], x['position'][2]-x['position'][0], x['position'][3]-x['position'][1]],

                             # axis_type = 'zoomed_inset'
                             parent_axes='parent_axis',
                             zoom='inset_zoom',
                             #loc='inset_position',

                             # mark_inset
                             #parent_axes='parent_axis',
                             loc1='corner1',
                             loc2='corner2',
                             ec='color',

                             # axis_type = 'parasite'
                             host_axes='host_axis',
                             axis='',
                             axis_shift='',

                             # Other settings
                             title='',
                             aspect='',
                             xlabel=lambda x: aux.get_label(x, 'xlabel', 'xunits'),
                             xunits_value='',
                             xlim='',#lambda x: [x['xMin'], x['xMax']],
                             xscale='xScale',
                             ylabel=lambda x: aux.get_label(x, 'ylabel', 'yunits'),
                             yunits_value='',
                             ylim='',#lambda x: [x['yMin'], x['yMax']],
                             yscale='yScale',
                             hide_axis='',                      # True or False
                             hide_ticks='',                     # True or False
                             hide_border='',                    # True or False
                             hide_ticklabels='',                # 'x', 'y' or 'both'
                             ticks_out='',                      # 'x', 'y' or 'both'
                             hide_xticks='',                    # 'top', 'bottom', or 'both'
                             hide_xborder='',                   # 'top', 'bottom', or 'both'
                             xlabel_top='',                     # True or False
                             hide_yticks='',                    # 'left', 'right', or 'both'
                             hide_yborder='',                   # 'left', 'right', or 'both'
                             ylabel_right='',                   # True or False
                             )


class PlotSettings(MappableSettings):
    _default_mappings = dict(name='',
                             data_folder='',
                             data_name='data',

                             # Required
                             ax='axis',
                             plot_type='',
                             data_type='',
                             size='',#lambda x: [x['MatrixSize_Y'], x['MatrixSize_X']],

                             # plot_type = rgba
                             xMin='',
                             xMax='',
                             yMin='',
                             yMax='',
                             cmap='',
                             clim='',#lambda x: [x['vMin'], x['vMax']],
                             cbarlabel=lambda x: aux.get_label(x, 'vlabel', 'vunits'),
                             cbarunits_value='vunits_value',
                             norm='',
                             show_cbar='',
                             cax='',
                             )


class AxesSettingsContainer(list):
    def append(self, **kwargs):
        super(AxesSettingsContainer, self).append(AxisSettings(**kwargs))


class PlotSettingsContainer(list):
    def append(self, **kwargs):
        super(PlotSettingsContainer, self).append(PlotSettings(**kwargs))
