#-*- coding=utf-8 -*-
#author: zhihua.ye@spreadtrum.com
#record important event
#write once and pass, Orz~~

import re
import json
import os
import sys
import re

'''
    the report event structure is like
    [
        {
            ename: "s2b failed",
            enamecount: 1,
            errorlist: [
                {
                    "error": "ping error",
                    "errorcount": 1
                },
                {
                    "error": "dpd error",
                    "errorcount": 1
                },

            ],
            errordetailslist:[
                {
                    "ename":
                    "timestamp":
                    "errorstr":
                    "lineno":

                },

            }
        }
    ]
'''


#some utils functions used for event table
def name_in_list(tname, tkey,tlist):
    #etable is list
    if type(tlist) is list and len(tlist) > 0:
        for index, element in enumerate(tlist):
            if element[tkey] == tname:
                return True
    return False


def constructreportEvent(report):
    '''
    :param ename:
    :param errorstr:
    :return:
    '''
    ename = report['event']
    errorstr = report['errorstr']
    timestamp = report['timestamp']
    line = report['line']
    lineno = report['lineno']

    newevent = dict()
    newevent['ename'] = ename
    newevent['enamecount'] = 1
    #errostr is a new list, may include different error str
    newevent['errorlist'] = list()
    # the complete error list
    newevent['errordetailslist'] = list()

    detailerror = dict()
    detailerror['ename'] = ename
    detailerror['errorstr'] = errorstr
    detailerror['timestamp'] = timestamp
    detailerror['line'] = line
    detailerror['lineno'] = lineno
    newevent['errordetailslist'].append(detailerror)

    if errorstr and len(errorstr):
        newerror = dict()
        newerror['errorstr'] = errorstr
        newerror['errorcount'] = 1
        newevent['errorlist'].append(newerror)

    return newevent

def updatereportEvent(report, etable):
    '''
    1. update ename count
    2. update errorlist
    :param ename:
    :param errorstr:
    :param etable: all the event table
    :return:
    '''
    ename = report['event']
    errorstr = report['errorstr']
    timestamp = report['timestamp']
    line = report['line']
    lineno = report['lineno']

    if type(etable) is list and len(etable) > 0:
        for index, element in enumerate(etable):
            if element['ename'] == ename:
                element['enamecount'] += 1
                #iterate the errorlist
                errorlist = element['errorlist']

                detailerror = dict()
                detailerror['errorstr'] = errorstr
                detailerror['timestamp'] = timestamp
                detailerror['line'] = line
                detailerror['lineno'] = lineno
                detailerror['ename'] = ename
                element['errordetailslist'].append(detailerror)

                if type(errorlist) is list and len(errorlist) > 0:
                    for eindex, error in enumerate(errorlist):
                        if error['errorstr'] == errorstr:
                            error['errorcount'] += 1
                            return
                    #if come here, so new error found
                    newerror = dict()
                    newerror['errorstr'] = errorstr
                    newerror['errorcount'] = 1
                    errorlist.append(newerror)

    else:
        #no etable exist, so invoke new one.
        return constructreportEvent(report)



