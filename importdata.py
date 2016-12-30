import numpy as np
#from PIL import Image
#import os


def fetch_data(plotSettings, loadedData, frameNumber):
    if plotSettings['data_name'] in loadedData.keys():
        data = loadedData[plotSettings['data_name']]
    else:
        data = import_data(plotSettings, frameNumber)
        loadedData[plotSettings['data_name']] = data
    return data


def import_data(plotSettings, frameNumber):
    dataFolder = plotSettings['data_folder']
    if plotSettings['data_type'] == '1D':
        fileName = dataFolder + plotSettings['data_name'] + '_' + str(frameNumber) + '.bin'
        data = np.fromfile(fileName, dtype='f')
        return data
    if plotSettings['data_type'] == '2D':
        fileName = dataFolder + plotSettings['data_name'] + '/' + ("%06d" % frameNumber) + '.bin'
        #data = (np.fromfile(plotSettings['name'] + os.path.sep + fileName, dtype='f')).reshape(plotSettings['size'])
        #fileName = dataFolder + plotSettings['data_name'] + '/' + str(frameNumber) + '.bin'
        data = np.fromfile(fileName, dtype='f').reshape(plotSettings['size'])
        return data
#    if plotSettings['data_type'] == 'bmp':
#        img = Image.open(fileName)
#        return np.asarray(img)
    if plotSettings['data_type'] == 'line':
        x = np.linspace(plotSettings['xMin'], plotSettings['xMax'], plotSettings['size'])
        data = np.array([x, np.sin(x)])
        return data
