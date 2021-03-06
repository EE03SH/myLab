#-*- coding=utf-8 -*-
#author: zhihua.ye@spreadtrum.com
#record important event

import re
import json
import os
import sys
import re

from configobj import ConfigObj,ConfigObjError

path = os.path.dirname(os.path.realpath(__file__))
sys.path.append('./')
from logConf import logConf
import logging
from sprdErrCode import *
from collections import Counter
from reportHelper import *
from operator import itemgetter

class Msglevel():
    DEBUG = 1
    INFO = 2
    NORMAL = 3
    WARNING = 4
    ERROR = 5


def maplevel2color(level):
    if level == Msglevel.INFO:
        return "blue"
    elif level == Msglevel.WARNING:
        return "brown"
    elif level == Msglevel.ERROR:
        return "red"
    elif level == Msglevel.NORMAL:
        return "green"
    else:
        return "black"

#define some event types: user, phone, scenarioes, handover algo
class ReportType():
    USEREVENT_BASE = 0x1000
    CPEVENT_BASE = 0x2000
    PHONEEVENT_BASE = 0x3000
    SCEEVENT_BASE = 0x4000
    HOALGO_BASE = 0x5000

#1. these types are added in eventhandler.py
#2. constructReport will build the report
#3. fillReport will add timestamp
#4. genEventTable will generate the table


#define function to build report
#FIXME: there is reportBuilder which is not adding the line, lineno, timestamp
class reportObj():
    def __init__(self):
        self.report = dict()
        self.report['type'] = None
        self.report['event'] = None
        self.report['level'] = Msglevel.INFO
        self.report['errorstr'] = None
        self.report['lineno'] = None
        self.report['line'] =  None
        self.report['timestamp'] = None
    def getreport(self):
        return self.report


#TODO: add detailed event description: process, result


class ReportEvent():
    def __init__(self, configpath='..', reportpath=None):
        try:
            configfile = configpath + '/config.ini'
            config = ConfigObj(configfile, file_error=True)
            self.config = config
            self.reportpath = reportpath
            self.logger = logConf()

            #error event need to be marked red
            #use Msglevel.ERROR to indicate
            self.errorevent = list()

            #Msglevel.INFO ,blue
            self.infoevent = list()
            #Msglevel.WARNING, brown
            self.warnevent = list()
            #Msglevel.NORMAL, green
            self.normalevent = list()


            #record every report, the Raw Data
            self.reportlist = list()

            #event table, processed data
            #three kinds of tables:
            # 1. useraction: wfc, wifi,
            # 2. phone:      s2b, reg, ho
            # 3. scenario :  call/sms
            # 4. add one more ho algorithm table
            # 99. eventtable: all these tables above

            self.tables = dict()


            usertable = dict()
            usertable['list'] = list()
            usertable['name'] = "usertable"
            usertable['title'] = "User Action Statistics"
            usertable['flowname'] = "userflowtable"
            usertable['flowtitle'] = "User Action Flow"

            phonetable = dict()
            phonetable['list'] = list()
            phonetable['name'] = "phonetable"
            phonetable['flowname'] = "phoneflowtable"
            phonetable['title'] = "Phone Status Statistics"
            phonetable['flowtitle'] = "Phone Status Flow"

            scenariotable = dict()
            scenariotable['list'] = list()
            scenariotable['name'] = "scenariotable"
            scenariotable['flowname'] = "scenarioflowtable"
            scenariotable['title'] = "VoWiFi Service Statistics"
            scenariotable['flowtitle'] = "VoWiFi Service Flow"

            hoalgotable = dict()
            hoalgotable['list'] = list()
            hoalgotable['name'] = 'hoalgotable'
            hoalgotable['flowname'] = 'hoalgoflowtable'
            hoalgotable['title'] = "Handover Strategy Statistics"
            hoalgotable['flowtitle'] = "Handover Strategy Flow"

            cptable = dict()
            cptable['list'] = list()
            cptable['name'] = 'cptable'
            cptable['flowname'] = 'cpflowtable'
            cptable['title'] = 'CP Action Statistics'
            cptable['flowtitle'] = 'CP Action Flow'

            etable = dict()
            etable['list'] = list()
            etable['name'] = "etable"
            etable['title'] = "All Event"

            self.tables['usertable'] = usertable
            self.tables['phonetable'] = phonetable
            self.tables['scenariotable'] = scenariotable
            self.tables['etable'] = etable
            self.tables['hoalgotable'] = hoalgotable
            self.tables['cptable'] = cptable

            self.tableattr = dict()
            #for event table
            self.tableattr['etable'] = dict()
            self.tableattr['etable']['caption'] = "Event table"
            self.tableattr['etable']['thlist'] = ["No.", "Event name", "Occurence", 'Details']

            #ecaptionach error detail should have a different format

            self.tableattr['errtable'] = dict()
            #this caption should be overwritten
            self.tableattr['errtable']['caption'] = "Error table"
            self.tableattr['errtable']['thlist'] = ["No.", "Eventname","Timestamp","Error Code", 'lineno', 'line']
            self.tableattr['errtable']['tname'] = ""

            #some global id indexes
            self.idindexes = dict()
            self.idindexes['top'] = 'Top'

            self.htmlstr = ''

            self.errorcount = 0

            with open(self.reportpath, 'w') as rlog:
                rlog.truncate()

            #all report log
            self.reportlog = os.path.dirname(self.reportpath) + '/report.log'

            with open(self.reportlog, 'w') as rlog:
                rlog.truncate()

            #FIXME: add error redirect log
            #all error log
            self.errorlog = os.path.dirname(self.reportpath) + '/error.log'

            with open(self.errorlog, 'w') as elog:
                elog.truncate()


        except (ConfigObjError, IOError) as e:
             print 'Could not read "%s": %s' % (configpath + '/config.ini', e)

    #some getter function for eventtable attribute
    def getEventTableCaption(self):
        return self.tableattr['etable']['caption']
    def getEventTableThlist(self):
        return self.tableattr['etable']['thlist']


    def setTlist(self, tname, list):
        self.tables[tname]['list'] = list

    def getTlist(self, tname):
        return self.tables[tname]['list']

    def getTname(self, tname):
        return self.tables[tname]['name']

    def getTflowname(self, tname):
        return self.tables[tname]['flowname']

    def getTitle(self, tname):
        return self.tables[tname]['title']

    def getFlowTitle(self, tname):
        return self.tables[tname]['flowtitle']


    def getErrorIndex(self, index):
        return "#Error_" + str(index)
    def getErrorId(self, index):
        return "Error_" + str(index)

    def isValidTable(self, table):
        if type(table) is list and len(table) > 0 :
            return True
        else:
            return False

    def genEventTable(self, onereport, table):
        #each report will be added into the table

        ename = onereport['event']

        #check the eventname, if not exist, then added, if exist, count plus
        if name_in_list(ename, 'ename', table):
            updatereportEvent(onereport, table)
        else:
            newevent = constructreportEvent(onereport)
            table.append(newevent)

    def genEventDetails(self,errorlist):
        detailstr = ''
        if type(errorlist) is list and len(errorlist) > 0:
            for index, error in enumerate(errorlist):
                count = str(error['errorcount'])
                estr = error['errorstr']
                detailstr += estr + ': ' + count + ' Times<br>'

        return detailstr


    def fillReport(self, msg):
        #simply grep event by types:
        #1. user action: wifi conn/discon, wfc enabled/disabled, airplane
        #2. phone action: attach, reg, ho
        #3. scenario: call, conf, sms , etc

        #just to parse the report type.
        if type(msg) is dict and msg and 'report' in msg:
            report = msg['report']
            if report and 'type' in report:
                rtype = report['type']
                if rtype and int(rtype) >= ReportType.USEREVENT_BASE:
                    if type(report['event']) is str:
                        report['timestamp'] = msg['timestamp']
                        report['line'] = msg['line']
                        report['lineno'] = msg['lineno']
                        self.reportlist.append(report)
                        #add function to generate the event overview

                        #the report structure is
                        '''
                        {
                           'event':
                           'errorstr':
                           'timestamp':
                           'line':
                           'lineno':
                           'type':
                           'level':
                        }
                        '''
                        event = report['event'].strip('\n')
                        #record error event
                        if report['level'] == Msglevel.ERROR and event not in self.errorevent:
                            self.errorevent.append(event)

                        if report['level'] == Msglevel.NORMAL and event not in self.normalevent:
                            self.normalevent.append(event)

                        if report['level'] == Msglevel.INFO and event not in self.infoevent:
                            self.infoevent.append(event)

                        if report['level'] == Msglevel.WARNING and event not in self.warnevent:
                            self.warnevent.append(event)


                        #there will three kinds of tables
                        if rtype == ReportType.USEREVENT_BASE:
                            self.genEventTable(report, self.getTlist('usertable'))
                        elif rtype == ReportType.PHONEEVENT_BASE:
                            self.genEventTable(report, self.getTlist('phonetable'))
                        elif rtype == ReportType.SCEEVENT_BASE:
                            self.genEventTable(report, self.getTlist('scenariotable'))
                        elif rtype ==  ReportType.HOALGO_BASE:
                            self.genEventTable(report, self.getTlist('hoalgotable'))
                        elif rtype == ReportType.CPEVENT_BASE:
                            self.genEventTable(report, self.getTlist('cptable'))


    def genheaderopen(self):
        headeropenstr = ''
        headeropenstr += "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.01 Transitional//EN http://www.w3.org/TR/html4/loose.dtd\">\n"
        headeropenstr += "<html><head>"
        headeropenstr += "<meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\">\n"
        headeropenstr += "<style type=\"text/css\">\n"
        headeropenstr += "table {border-collapse: collapse;}\n"
        headeropenstr += "td {padding: 0px;text-align: center;}\n"
        headeropenstr += "</style></head><body>\n"
        return headeropenstr

    def genheaderclose(self):
        headerclosestr = ""
        headerclosestr += "</body>"
        headerclosestr += "</html>\n"
        return headerclosestr



    def gentableopen(self, caption, columnlist, tname):
        tableopenstr = ""
        if type(columnlist) is list and columnlist:
            tableopenstr += "<table border=\"1\">\n"
            tableopenstr += "<caption id=\"" + tname +"\"><b>" + caption + "</b></caption>"
            for index, column in enumerate(columnlist):
                tableopenstr +="<th>" + column +"</th>"
        return tableopenstr

    def genrowopen(self):
        rowopenstr = ""
        rowopenstr +="<tr>\n"
        return rowopenstr

    def gencolumn(self, content):
        #column color will be detemined internally
        bgcolor = "white"
        if content in self.errorevent:
            bgcolor = "red"
        elif content in self.warnevent:
            bgcolor = "brown"
        elif content in self.infoevent:
            bgcolor = "cyan"
        elif content in self.normalevent:
            bgcolor = "green"

        '''
        color debug...
        if 'TermCall' in content:
            self.logger.logger.info('zhihuaye' + content + '  ' + bgcolor)
        '''
        columnstr = ""
        columnstr += "<td style=\"background-color:" + bgcolor + "\">" + content + "</td>"
        return columnstr

    def genrowclose(self):
        rowclosestr = ""
        rowclosestr += "</tr>"
        return rowclosestr

    def gentableclose(self):
        tableclosestr = ""
        tableclosestr += "</table><br>\n"
        return tableclosestr

    def genulopen(self, idstr=''):
        ulstr = "<ul id=\""+ str(idstr) +"\">"
        return ulstr

    def genulclose(self):
        ulstr = "</ul>\n"
        return ulstr

    def genli(self, content):
        listr = ""
        listr += "<li>" + content + "</li>\n"
        return listr

    def genaref(self,content, href, id='', newtab=False):
        arefstr = ""
        if newtab:
            arefstr += "<a target=\"_blank\" href=\""+ href +"\"" +" id=\""+str(id)+"\" >" + content + "</a>\n"
        else:
            arefstr += "<a href=\""+ href +"\"" +" id=\""+str(id)+"\" >" + content + "</a>\n"
        return arefstr

    def genOverviewIndex(self):
        overviewstr = ''
        username = self.getTname('usertable')
        cpname = self.getTname('cptable')
        phonename = self.getTname('phonetable')
        scenarioname = self.getTname('scenariotable')
        hoalgoname = self.getTname('hoalgotable')
        astr1 = self.genaref("Event Overview", '#' + username)
        listr1 = self.genli(astr1)
        overviewstr += listr1

        overviewstr += self.genulopen()

        #add the id
        userastr = self.genaref(self.getTitle('usertable'), '#' + username)
        overviewstr += self.genli(userastr)

        cpastr = self.genaref(self.getTitle('cptable'), '#' + cpname)
        overviewstr += self.genli(cpastr)

        phoneastr = self.genaref(self.getTitle('phonetable'), '#' + phonename)
        overviewstr += self.genli(phoneastr)

        scenarioastr = self.genaref(self.getTitle('scenariotable'), '#' + scenarioname)
        overviewstr += self.genli(scenarioastr)

        hoalgoastr = self.genaref(self.getTitle('hoalgotable'), '#' + hoalgoname)
        overviewstr += self.genli(hoalgoastr)

        overviewstr += self.genulclose()

        return overviewstr

    def genErrorIndex(self):
        errorindex = ''

        astr = self.genaref("Error Scenarioes", "#ERROR_0")

        errorindex += self.genli(astr)

        errorindex += self.genulopen()
        etable = self.getTlist('etable')

        for index, eventdict in enumerate(etable):
            event = eventdict['ename']
            if event in self.errorevent:
                #add occurrence times:
                occurcount = len(eventdict['errordetailslist'])
                event = str(occurcount) + " times, " + event
                astrin= self.genaref(event, self.getErrorIndex(index))
                errorindex += self.genli(astrin)
        errorindex += self.genulclose()
        return errorindex

    def genFlowIndex(self):
        flowstr = ''


        username = self.getTflowname('usertable')
        phonename = self.getTflowname('phonetable')
        scenarioname = self.getTflowname('scenariotable')
        hoalgoname = self.getTflowname('hoalgotable')
        cpname = self.getTflowname('cptable')
        astr = self.genaref("Event Flow", '#' + username)
        flowstr += self.genli(astr)

        flowstr += self.genulopen()

        userastr = self.genaref(self.getFlowTitle('usertable'), '#' + username)
        flowstr += self.genli(userastr)

        cpastr = self.genaref(self.getFlowTitle('cptable'), '#' + cpname)
        flowstr += self.genli(cpastr)

        phoneastr = self.genaref(self.getFlowTitle('phonetable'), '#' + phonename)
        flowstr += self.genli(phoneastr)

        scenarioastr = self.genaref(self.getFlowTitle('scenariotable'), '#' + scenarioname)
        flowstr += self.genli(scenarioastr)

        hoalgoastr = self.genaref(self.getFlowTitle('hoalgotable'), '#' + hoalgoname)
        flowstr += self.genli(hoalgoastr)

        flowstr += self.genulclose()

        return flowstr

    def generateIndex(self):
        #parse the etable, generate the index and sub index
        indexstr = ""

        #generate the top index
        indexstr += self.genulopen(idstr=self.idindexes['top'])
        indexstr += self.genOverviewIndex()
        #if no error , the li is not used;
        #but for sprd, there will be always error.
        #error comes first
        indexstr += self.genErrorIndex()
        indexstr += self.genFlowIndex()

        return indexstr

    def genTitle(self, id, string):
        title = ''
        title += '<h2 id=\''+ str(id) + '\'>'+ string + '</h2>'
        return title

    def genBackToTop(self):
        bttstr = ''
        bttstr = self.genaref("Back To Top", '#' + self.idindexes['top'])

        return bttstr

    def genstatsrow(self,eventdict, index):
        rowstr = ''
        event = eventdict['ename']
        count = str(eventdict['enamecount'])
        detailstr = self.genEventDetails(eventdict['errorlist'])
        rowstr +=self.genrowopen()
        rowstr +=self.gencolumn(str(index+1))
        rowstr +=self.gencolumn(event)
        rowstr +=self.gencolumn(count)
        rowstr +=self.gencolumn(detailstr)
        rowstr +=self.genrowclose()
        return rowstr

    def genflowrow(self,eventdict, index):
        #["No.", "Eventname","Timestamp","Error Code", 'lineno', 'line']
        rowstr = ''
        event = eventdict['ename']
        timestamp = str(eventdict['timestamp'])
        error = eventdict['errorstr']
        lineno = str(eventdict['lineno'])
        line = str(eventdict['line'])
        rowstr +=self.genrowopen()
        rowstr +=self.gencolumn(str(index+1))
        rowstr +=self.gencolumn(event)
        rowstr +=self.gencolumn(timestamp)
        rowstr +=self.gencolumn(error)
        rowstr += self.gencolumn(lineno)
        rowstr += self.gencolumn(line)
        rowstr +=self.genrowclose()
        return rowstr



    def genOneTableHTML(self, caption, thlist, tablelist, tabletitle,tableid, rowgen):

        #get eventlist and iterate it, wirte it in right place

        tablehtml = ''

        tablehtml += self.genBackToTop()
        tablehtml += self.genTitle(tableid, tabletitle)
        tablehtml += self.gentableopen(caption, thlist, tableid)

        self.logger.logger.info('DEBUG----------------')
        self.logger.logger.info(tablelist)
        for index, eventdict in enumerate(tablelist):
             tablehtml += rowgen(eventdict,index)
        tablehtml +=self.gentableclose()

        #generate the back to top link
        tablehtml += self.genBackToTop()

        tablehtml += self.genhorizonline()
        return tablehtml

    def generateAllSTATSTableHTML(self):
        testcaption = self.getEventTableCaption()
        thlist = self.getEventTableThlist()

        etablehtml = ""
        etablehtml += self.genOneTableHTML(caption=testcaption, thlist=thlist,tablelist=self.getTlist('usertable'), tabletitle=self.getTitle('usertable'), tableid=self.getTname('usertable'), rowgen=self.genstatsrow)
        etablehtml += self.genOneTableHTML(caption=testcaption, thlist=thlist,tablelist=self.getTlist('cptable'), tabletitle=self.getTitle('cptable'), tableid=self.getTname('cptable'),rowgen=self.genstatsrow)
        etablehtml += self.genOneTableHTML(caption=testcaption, thlist=thlist,tablelist=self.getTlist('phonetable'), tabletitle=self.getTitle('phonetable'), tableid=self.getTname('phonetable'),rowgen=self.genstatsrow)
        etablehtml += self.genOneTableHTML(caption=testcaption, thlist=thlist,tablelist=self.getTlist('scenariotable'), tabletitle=self.getTitle('scenariotable'), tableid=self.getTname('scenariotable'),rowgen=self.genstatsrow)
        etablehtml += self.genOneTableHTML(caption=testcaption, thlist=thlist,tablelist=self.getTlist('hoalgotable'), tabletitle=self.getTitle('hoalgotable'), tableid=self.getTname('hoalgotable'),rowgen=self.genstatsrow)

        return etablehtml

    def genhorizonline(self):
        return "<hr>\n"

    def genOneErrorTable(self, dlist, index):
        errortablehtml = ''
        caption = self.tableattr['errtable']['caption']
        thlist = self.tableattr['errtable']['thlist']
        tname = str(index)
        errortablehtml += self.genBackToTop()
        errortablehtml += self.gentableopen(caption, thlist, tname)
        #["No.", "Timestamp","Error Code", 'lineno']
        for i, error in enumerate(dlist):
            no = i
            timestamp = error['timestamp']
            errorstr = error['errorstr']
            lineno = str(error['lineno'])
            line = str(error['line'])
            event = str(error['ename'])

            #append errorlog
            with open(self.errorlog, 'a+') as elog:
                #first line is event, timestamp, errorstr
                oneline = str(i+1) + '. '+  event.split('<br>',1)[0] + ',' + timestamp + ',' + errorstr
                elog.write(oneline + '\n')
                #second line is line
                elog.write(line)

            errortablehtml += self.genrowopen()
            errortablehtml +=self.gencolumn(str(no+1))
            errortablehtml +=self.gencolumn(event)
            errortablehtml +=self.gencolumn(timestamp)
            errortablehtml +=self.gencolumn(errorstr)
            errortablehtml +=self.gencolumn(lineno)
            errortablehtml +=self.gencolumn(line)
            errortablehtml += self.genrowclose()

        errortablehtml += self.gentableclose()
        #generate the back to top link
        errortablehtml += self.genBackToTop()
        #add horizon line
        errortablehtml += self.genhorizonline()

        return errortablehtml

    def genAllErrorTable(self):

        allerrortable = ''
        etable = self.getTlist('etable')

        for index, eventdict in enumerate(etable):
            event = eventdict['ename']
            detaillist = eventdict['errordetailslist']
            etableid =  self.getErrorId(index)

            if event in self.errorevent:
                #redirect error log here
                occurcount = len(detaillist)
                #split by <br>, EAP-AKA AUTH correctly<br>EAP-AKA校验成功
                summary = event.split('<br>',1)[0] + ' : '+str(occurcount) + " Times"

                with open(self.errorlog, 'a+') as elog:
                    elog.write('\n' + summary + '\n')
                #generate one error table
                allerrortable += self.genTitle(etableid, event)
                allerrortable += self.genOneErrorTable(detaillist, etableid)
        return allerrortable

    def formattables(self):
        etable = self.getTlist('etable')
        usertable = self.getTlist('usertable')
        phonetable = self.getTlist('phonetable')
        scenariotable = self.getTlist('scenariotable')
        hoalgotable  = self.getTlist('hoalgotable')
        cptable = self.getTlist('cptable')

        etable = usertable + phonetable + scenariotable + hoalgotable + cptable

        #sort the output by occurence descending
        usertable = sorted(usertable, key=itemgetter('enamecount'),  reverse=True)
        phonetable = sorted(phonetable, key=itemgetter('enamecount'),  reverse=True)
        cptable = sorted(cptable, key=itemgetter('enamecount'),  reverse=True)
        scenariotable = sorted(scenariotable, key=itemgetter('enamecount'),  reverse=True)
        etable = sorted(etable, key=itemgetter('enamecount'),  reverse=True)

        self.setTlist('etable',etable)
        self.setTlist('usertable',usertable)
        self.setTlist('phonetable', phonetable)
        self.setTlist('scenariotable',scenariotable)
        self.setTlist('cptable', cptable)

    def reorderdetaillist(self, table):
        '''
        error in errordetailslist may be not in order
        :param table:
        :return:
        '''
        errordetailslist = list()
        for index, eventdict in enumerate(table):
            elist = eventdict['errordetailslist']
            errordetailslist += elist
        #sort it, ascending
        errordetailslist = sorted(errordetailslist, key=itemgetter('timestamp'))
        print 'elist------'
        print errordetailslist
        return errordetailslist


    def genAllFlowTable(self):
        ftablestr = ''

        #each list shoud be ordered
        usertable = self.getTlist('usertable')
        usertablelist = self.reorderdetaillist(usertable)
        phonetable = self.getTlist('phonetable')
        phonetablelist = self.reorderdetaillist(phonetable)
        scenariotable = self.getTlist('scenariotable')
        scenariotablelist = self.reorderdetaillist(scenariotable)
        hoalgotable = self.getTlist('hoalgotable')
        hoalgotablelist = self.reorderdetaillist(hoalgotable)

        cptable = self.getTlist('cptable')
        cptablelist = self.reorderdetaillist(cptable)

        caption = "Flow Table"
        thlist = self.tableattr['errtable']['thlist']
        ftablestr += self.genOneTableHTML(caption=caption, thlist=thlist,tablelist=usertablelist, tabletitle=self.getFlowTitle('usertable'), tableid=self.getTflowname('usertable'), rowgen=self.genflowrow)

        ftablestr += self.genOneTableHTML(caption=caption, thlist=thlist,tablelist=cptablelist, tabletitle=self.getFlowTitle('cptable'), tableid=self.getTflowname('cptable'), rowgen=self.genflowrow)

        ftablestr += self.genOneTableHTML(caption=caption, thlist=thlist,tablelist=phonetablelist, tabletitle=self.getFlowTitle('phonetable'), tableid=self.getTflowname('phonetable'),rowgen=self.genflowrow)

        ftablestr += self.genOneTableHTML(caption=caption, thlist=thlist,tablelist=scenariotablelist, tabletitle=self.getFlowTitle('scenariotable'), tableid=self.getTflowname('scenariotable'),rowgen=self.genflowrow)

        ftablestr += self.genOneTableHTML(caption=caption, thlist=thlist,tablelist=hoalgotablelist, tabletitle=self.getFlowTitle('hoalgotable'), tableid=self.getTflowname('hoalgotable'),rowgen=self.genflowrow)

        return ftablestr

    def genHeadPara(self):
        hpara = ''
        elogstr = 'Trimmed log flow, please refer to ' + self.genaref("report.log", "./report.log", newtab=True) + "\n<br>"
        pdfstr = "For better view and Detailed Graphic Sequence flow , please refer to " + self.genaref("main.pdf", "./main.pdf",newtab=True) + "\n<br>"
        pdflogstr = 'Detailed Text log flow, please refer to ' + self.genaref("event.log", "./event.log",newtab=True) + "\n<br>"
        hpara += pdfstr
        hpara += pdflogstr
        hpara += elogstr

        contactstr = "Any Question or Suggestion, you can contact " + self.genaref("zhihua.ye@spreadtrum.com", "mailto:zhihua.ye@spreadtrum.com")
        hpara += contactstr
        return hpara

    def generateHTML(self):
        #first of all, combine all tables
        self.formattables()
        etable = self.getTlist('etable')

        if self.isValidTable(etable) > 0 :
            self.htmlstr += self.genheaderopen()
            self.htmlstr += self.genHeadPara()
            self.htmlstr += self.generateIndex()
            self.htmlstr += self.generateAllSTATSTableHTML()
            self.htmlstr += self.genAllErrorTable()
            self.htmlstr += self.genAllFlowTable()
            self.htmlstr += self.genheaderclose()
            with open(self.reportpath, 'a+') as rlog:
                rlog.write(self.htmlstr)

            etablelist = self.reorderdetaillist(etable)
            with open(self.reportlog, 'a+') as rlog:
                for index, event in enumerate(etablelist):
                    line = event['line']
                    rlog.write(line)


    def cloudpic(self):
        # yuntu which will demonstrate the relationship between modules
        pass
