#-*- coding=utf-8 -*-
#author: zhihua.ye@spreadtrum.com
# https://github.com/pyinstaller/pyinstaller/issues/1890
# pyinstaller's issue, add hook-openpyxl.py to
# C:\Python27\Lib\site-packages\PyInstaller\hooks


import os
from configobj import ConfigObj,ConfigObjError
import definition


class config():
    def __init__(self):
        try:
            configfile = definition.CONFIG_PATH + '/config.ini'
            tmpconfig = ConfigObj(configfile, file_error=True)
            self.config = dict()
            self.config['key'] = dict()
            self.config['key']['media'] = tmpconfig['keywords']['media']
            self.config['key']['avc'] = tmpconfig['keywords']['avc']
            self.config['version'] = tmpconfig['utils']['version']
        except (ConfigObjError, IOError) as e:
             print('Could not read "%s": %s' % ('config.ini', e))

    def getmkey(self):
        return self.config['key']['media']

    def getavckey(self):
        return self.config['key']['avc']

    def getversion(self):
        return self.config['version']



if __name__ == '__main__':
    config = config()
    print config.config['key']['media'], config.config['version']