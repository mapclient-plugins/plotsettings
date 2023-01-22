"""
MAP Client Plugin
"""

__version__ = '0.2.0'
__author__ = 'Hugh Sorby'
__stepname__ = 'Plot Settings'
__location__ = 'https://github.com/mapclient-plugins/plotsettings/archive/v0.1.0.zip'

# import class that derives itself from the step mountpoint.
from mapclientplugins.plotsettingsstep import step

# Import the resource file when the module is loaded,
# this enables the framework to use the step icon.
from . import resources_rc
