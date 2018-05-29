"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['scoring.py']
DATA_FILES = ['team_check.py',
 'team-scores.txt',
 'constants.py',
 'players/bill.txt',
 'players/bob.txt',
 'players/jack.txt',
 'players/joe.txt']
OPTIONS = {'iconfile': '/Users/Nicholas/GitHub/world-cup/fifa.icns'}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
