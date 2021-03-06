#-*- coding=utf-8 -*-
#author: zhihua.ye@spreadtrum.com
#some event helper for searchEvent in flowParser.py

#SOME NOTES here:
#   1. key logs are defined in constants.py
#   2. to add report , please refer to reportConverter.py,  use constructReport


import re
import json
import mobile_codes
from sprdErrCode import *
from reportEvent import *
from reportConverter import *







class eventdict():
    def __init__(self):
        self.msglevel = Msglevel.INFO
        self.color = "black"
        self.msg = None
        #report type, default is none, should be set in eventHandler
        self.report = dict()
        self.report['type'] = None
        self.report['event'] = None
        self.report['level'] = Msglevel.INFO
        self.report['errorstr'] = None
        self.report['lineno'] = None
        self.report['line'] =  None
        self.report['timestamp'] = None

class eventhandler():
    def __init__(self, match, color, groupnum):
        self.match = match
        self.color = color
        self.groupnum = groupnum
        self.retmsg = eventdict()
        #set the selected color
        self.retmsg.color = color

    def handler(self):
        #need to overwrite the handler.
        return None

    '''
       ######### main process #########
    '''
    def getret(self):
        grouplen = len(self.match.groups())
        if self.match and grouplen >= self.groupnum:
            return self.handler()
        else:
            return None

class demoinherit(eventhandler):
    def handler(self):
        self.retmsg = self.match.group(1).strip()
        return self.retmsg

#NOTE: color can be set from function input , or defined in function logic
class matchone(eventhandler):
    '''
    only match one , return one
    '''
    def handler(self):
        self.retmsg.msg = self.match.group(1)
        return self.retmsg


#function only match one, but need to generate the report
class wificonn(eventhandler):
    def handler(self):
        self.retmsg.msg = self.match.group(1)
        self.retmsg.msglevel = Msglevel.NORMAL
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        event=mapzhphrase("wificonn", ReportHandoverphrase)
        self.retmsg.report = constructReport(type=ReportType.USEREVENT_BASE, event=event, level=self.retmsg.msglevel)
        return self.retmsg

class wificonn2(eventhandler):
     def handler(self):
        wifi = str(self.match.group(1)).strip()
        if wifi == 'true':
            wifistr = "Connected"
        else:
            wifistr = "Disconnected"

        self.retmsg.msg = "WiFi is " + wifistr
        self.retmsg.msglevel = Msglevel.NORMAL
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        return self.retmsg
#function only match one, but need to generate the report
class cmendcall(eventhandler):
    def handler(self):
        self.retmsg.msg = self.match.group(1)
        self.retmsg.msglevel = Msglevel.ERROR
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        event = mapzhphrase("cmendcall", ReportHandoverphrase)
        self.retmsg.report = constructReport(type=ReportType.PHONEEVENT_BASE, event=event, level=self.retmsg.msglevel)
        return self.retmsg

class wifidisconn(eventhandler):
    def handler(self):
        self.retmsg.msg = self.match.group(1)
        self.retmsg.msglevel = Msglevel.WARNING
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        event = mapzhphrase("wifidisconn", ReportHandoverphrase)
        self.retmsg.report = constructReport(type=ReportType.USEREVENT_BASE, event=event, level=self.retmsg.msglevel)
        return self.retmsg

class wifipreclose(eventhandler):
    def handler(self):
        pdnstate = str(self.match.group(1).lower())
        if pdnstate == 'false':
            pdnstatestr = "PDN State: Actived"
        else:
            pdnstatestr = "PDN State: DeActived"
        self.retmsg.msg = "WiFi PreClose\n" + pdnstatestr
        self.retmsg.msglevel = Msglevel.WARNING
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        return self.retmsg


class airon(eventhandler):
    def handler(self):
        self.retmsg.msg = self.match.group(1)
        self.retmsg.msglevel = Msglevel.WARNING
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        event = mapzhphrase("airon", ReportHandoverphrase)
        self.retmsg.report = constructReport(type=ReportType.USEREVENT_BASE, event=event, level=self.retmsg.msglevel)
        return self.retmsg

class airoff(eventhandler):
    def handler(self):
        self.retmsg.msg = self.match.group(1)
        self.retmsg.msglevel = Msglevel.WARNING
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        event = mapzhphrase("airoff", ReportHandoverphrase)
        self.retmsg.report = constructReport(type=ReportType.USEREVENT_BASE, event=event, level=self.retmsg.msglevel)
        return self.retmsg

class poweroff(eventhandler):
    def handler(self):
        self.retmsg.msg = "Phone is shutting down"
        self.retmsg.msglevel = Msglevel.WARNING
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        return self.retmsg

class callcard(eventhandler):
    def handler(self):
        #
        action = self.match.group(1)
        callid = str(self.match.group(2))
        state = self.match.group(3).strip()

        fmsg = action + '\n'
        fmsg += "TeleCallid : " + callid  + '\n'
        fmsg +=  "CallState: " + state
        self.retmsg.msglevel = Msglevel.WARNING
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        self.retmsg.msg = fmsg
        #TODO: add report according to different action
        return self.retmsg

class invalidSimCard(eventhandler):
    def handler(self):
        self.retmsg.msglevel = Msglevel.ERROR
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        self.retmsg.msg = "SimCard is not in VoWiFi whitelist"
        event = mapzhphrase("invalidsim", ReportHandoverphrase)
        self.retmsg.report = constructReport(type=ReportType.PHONEEVENT_BASE, event=event, level=self.retmsg.msglevel)
        return self.retmsg

class idlehowifi(eventhandler):
    def handler(self):
        self.retmsg.msg = self.match.group(1)
        self.retmsg.msglevel = Msglevel.INFO
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        event = mapzhphrase("idlehowifi", ReportHandoverphrase)
        self.retmsg.report = constructReport(type=ReportType.PHONEEVENT_BASE, event=event, level=self.retmsg.msglevel)
        return self.retmsg

class idleholte(eventhandler):
    def handler(self):
        self.retmsg.msg = self.match.group(1)
        self.retmsg.msglevel = Msglevel.INFO
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        event = mapzhphrase("idleholte", ReportHandoverphrase)
        self.retmsg.report = constructReport(type=ReportType.PHONEEVENT_BASE, event=event, level=self.retmsg.msglevel)
        return self.retmsg

class callhowifi(eventhandler):
    def handler(self):
        self.retmsg.msg = self.match.group(1)
        self.retmsg.msglevel = Msglevel.INFO
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        event = mapzhphrase("callhowifi", ReportHandoverphrase)
        self.retmsg.report = constructReport(type=ReportType.PHONEEVENT_BASE, event=event, level=self.retmsg.msglevel)
        return self.retmsg



class callholte(eventhandler):
    def handler(self):
        self.retmsg.msg = self.match.group(1)
        self.retmsg.msglevel = Msglevel.INFO
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        event = mapzhphrase("callholte", ReportHandoverphrase)
        self.retmsg.report = constructReport(type=ReportType.PHONEEVENT_BASE, event=event, level=self.retmsg.msglevel)
        return self.retmsg

class oneclickconf(eventhandler):
    '''
    the one click conf participants, one pattern
    '''
    def handler(self):
        partner = str(self.match.group(1)).strip()
        self.retmsg.msg = "Start Conf with " + partner
        self.retmsg.msglevel = Msglevel.INFO
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        return self.retmsg

class acceptcall(eventhandler):
    '''
    accept call , one pattern, calltype
    '''
    def handler(self):
        calltype = str(self.match.group(1).strip())
        calltype = mapcode2str(calltype, Constantcalltype)
        self.retmsg.msglevel = Msglevel.WARNING
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        self.retmsg.msg = "Accept As " + calltype
        event = mapzhphrase(calltype, ReportScenariophrase)
        self.retmsg.report = constructReport(type=ReportType.SCEEVENT_BASE, event=event, level=self.retmsg.msglevel)
        return self.retmsg

class rejectcall(eventhandler):
    '''
    reject call,
    '''
    def handler(self):
        rejectreason = str(self.match.group(1).strip())
        rejectreason = mapcode2str(rejectreason,Constantimsreason)
        self.retmsg.msglevel = Msglevel.WARNING
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        self.retmsg.msg = "Reject As :" + rejectreason
        event = mapzhphrase("rejectcall", ReportScenariophrase, post=rejectreason)
        self.retmsg.report = constructReport(type=ReportType.SCEEVENT_BASE, event=event, level=self.retmsg.msglevel)
        return self.retmsg

class termcall(eventhandler):
    '''
    term call, one pattern, term reason
    '''
    def handler(self):
        reasonstr = str(self.match.group(1)).strip()
        reasonstr = mapcode2str(reasonstr, Constantimsreason)
        self.retmsg.msglevel = Msglevel.WARNING
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        self.retmsg.msg = "Term Call As :" + reasonstr
        event = mapzhphrase("termcall", ReportScenariophrase, post=reasonstr)
        self.retmsg.report = constructReport(type=ReportType.SCEEVENT_BASE, event=event, level=self.retmsg.msglevel)
        return self.retmsg

def parsemprofile(mprofile):
    if mprofile:
        profilekey = "{ audioQuality=(.*), audioDirection=(.*), videoQuality=(.*), videoDirection=(.*) }"
        profilepattern = re.compile(profilekey)
        match = profilepattern.search(mprofile)

        if match:
            mlen = len(match.groups())
            if mlen == 4:
                aq = str(match.group(1)).strip()
                ad = str(match.group(2)).strip()
                vq = str(match.group(3)).strip()
                vd = str(match.group(4)).strip()
                #define the format
                ret = dict()
                ret['audio'] = dict()
                ret['audio']['codec'] = mapcode2str(aq, ConstantAudioQ)
                ret['audio']['direct'] = mapcode2str(ad, Constantdirection)
                ret['video'] = dict()
                ret['video']['codec'] = mapcode2str(vq, ConstantVideoQ)
                ret['video']['direct'] = mapcode2str(vd, Constantdirection)
                return ret
            else:
                return None
    else:
        return None


class holdcall(eventhandler):
    '''
    hold call, one COMPLEX pattern
    { audioQuality=2, audioDirection=2, videoQuality=1, videoDirection=2 }
    '''
    def handler(self):
        mprofile = self.match.group(1)
        if mprofile:
            self.retmsg.msglevel = Msglevel.WARNING
            self.retmsg.color = maplevel2color(self.retmsg.msglevel)
            parsedprofile = parsemprofile(mprofile)
            if parsedprofile:
                acodec = parsedprofile['audio']['codec']
                adirect = parsedprofile['audio']['direct']
                vcodec = parsedprofile['video']['codec']
                vdirect = parsedprofile['video']['direct']
                holdmsg = "Hold Call\n"
                holdmsg += "Audio: " + acodec + " , "+ adirect +'\n'

                if vdirect != Constantdirection[str(DIRECTION_INVALID)]:
                    holdmsg += "Video: " + vcodec + " , "+ vdirect +'\n'


                event = mapzhphrase("holdcall", ReportScenariophrase)
                self.retmsg.report = constructReport(type=ReportType.SCEEVENT_BASE, event=event, level=self.retmsg.msglevel)
                self.retmsg.msg = holdmsg
                return self.retmsg
        else:
            return None

class resumecall(eventhandler):
    '''
    resume call, one COMPLEX pattern
    { audioQuality=2, audioDirection=3, videoQuality=1, videoDirection=3 }
    '''
    def handler(self):
        #almost the same as holdcall
        mprofile = self.match.group(1)
        if mprofile:
            self.retmsg.msglevel = Msglevel.WARNING
            self.retmsg.color = maplevel2color(self.retmsg.msglevel)
            parsedprofile = parsemprofile(mprofile)
            if parsedprofile:
                acodec = parsedprofile['audio']['codec']
                adirect = parsedprofile['audio']['direct']
                vcodec = parsedprofile['video']['codec']
                vdirect = parsedprofile['video']['direct']
                holdmsg = "Resume Call\n"
                holdmsg += "Audio: " + acodec + " , "+ adirect +'\n'
                if vdirect != Constantdirection[str(DIRECTION_INVALID)]:
                    holdmsg += "Video: " + vcodec + " , "+ vdirect +'\n'

                event = mapzhphrase("resumecall", ReportScenariophrase)
                self.retmsg.report = constructReport(type=ReportType.SCEEVENT_BASE, event=event, level=self.retmsg.msglevel)
                self.retmsg.msg = holdmsg
                return self.retmsg
        else:
            return None

class removepart(eventhandler):
    def handler(self):
        self.retmsg.msglevel = Msglevel.WARNING
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        part = self.match.group(1)
        self.retmsg.msg = "Remove " + part + " From ConfCall"
        return self.retmsg

class dtmf(eventhandler):
    def handler(self):
        self.retmsg.msglevel = Msglevel.INFO
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        code = str(self.match.group(1)).strip()
        self.retmsg.msg = "Press DTMF " + code
        return self.retmsg

class ussd(eventhandler):
    def handler(self):
        self.retmsg.msglevel = Msglevel.INFO
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        ussdmsg = str(self.match.group(1)).strip()
        self.retmsg.msg = "Send USSD " + ussdmsg
        return self.retmsg


class startcamera(eventhandler):
    '''
    camera pattern, two pattern, one is cameraid, two is callid
    '''
    def handler(self):
        self.retmsg.msglevel = Msglevel.INFO
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        cameraid = str(self.match.group(1)).strip()
        callid = str(self.match.group(2)).strip()
        fmsg = "Start Camera\n"
        fmsg += "Cameraid : " + cameraid+ '\n'
        fmsg += "StackCallid : " + callid
        self.retmsg.msg = fmsg
        return self.retmsg

class startcamerafailed(eventhandler):
    def handler(self):
        self.retmsg.msglevel = Msglevel.ERROR
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        cameraid = str(self.match.group(1)).strip()
        fmsg = "Start Camera Failed\n"
        fmsg += "Cameraid : " + cameraid+ '\n'
        self.retmsg.msg = fmsg
        return self.retmsg

class stopcamera(eventhandler):
    def handler(self):
        self.retmsg.msglevel = Msglevel.INFO
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        callid = str(self.match.group(1)).strip()
        fmsg = "Stop Camera\n"
        fmsg += "StackCallid : " + callid
        self.retmsg.msg = fmsg
        return self.retmsg


class stopcamerafailed(eventhandler):
    def handler(self):
        self.retmsg.msglevel = Msglevel.ERROR
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        fmsg = "Stop Camera Failed\n"
        self.retmsg.msg = fmsg
        return self.retmsg


class startlocalrender(eventhandler):
    def handler(self):
        self.retmsg.msglevel = Msglevel.INFO
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        callid = str(self.match.group(1)).strip()
        fmsg = "Start localrender\n"
        fmsg += "StackCallid : " + callid
        self.retmsg.msg = fmsg
        return self.retmsg

class stoplocalrender(eventhandler):
    def handler(self):
        self.retmsg.msglevel = Msglevel.INFO
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        callid = str(self.match.group(1)).strip()
        fmsg = "Stop localrender\n"
        fmsg += "StackCallid : " + callid
        self.retmsg.msg = fmsg
        return self.retmsg

class startremoterender(eventhandler):
    def handler(self):
        self.retmsg.msglevel = Msglevel.INFO
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        callid = str(self.match.group(1)).strip()
        fmsg = "Start remoterender\n"
        fmsg += "StackCallid : " + callid
        self.retmsg.msg = fmsg
        return self.retmsg

class stopremoterender(eventhandler):
    def handler(self):
        self.retmsg.msglevel = Msglevel.INFO
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        callid = str(self.match.group(1)).strip()
        fmsg = "Stop remoterender\n"
        fmsg += "StackCallid : " + callid
        self.retmsg.msg = fmsg
        return self.retmsg

class startcapture(eventhandler):
    '''
    three pattern: callid, cameraid, qualityid
    '''
    def handler(self):
        callid = str(self.match.group(1)).strip()
        cameraid = str(self.match.group(2)).strip()
        qualityid = str(self.match.group(3)).strip()
        qualitystr = mapcode2str(qualityid,ConstantVTResolution)
        fmsg = "Start Capture\n"
        fmsg += "Resolution: " + qualitystr + '\n'
        fmsg += "StackCallid: " + callid + '\n'
        fmsg += "Cameraid: " + cameraid + '\n'
        self.retmsg.msglevel = Msglevel.INFO
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        self.retmsg.msg = fmsg
        return self.retmsg

class stopcapture(eventhandler):
    def handler(self):
        self.retmsg.msglevel = Msglevel.INFO
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        callid = str(self.match.group(1)).strip()
        fmsg = "Stop Capture\n"
        fmsg += "StackCallid : " + callid
        self.retmsg.msg = fmsg
        return self.retmsg

class startvideo(eventhandler):
    def handler(self):
        self.retmsg.msglevel = Msglevel.INFO
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        callid = str(self.match.group(1)).strip()
        fmsg = "Start Video\n"
        fmsg += "StackCallid : " + callid
        self.retmsg.msg = fmsg
        return self.retmsg

class startvideofailed(eventhandler):
    def handler(self):
        self.retmsg.msglevel = Msglevel.ERROR
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        callid = str(self.match.group(1)).strip()
        fmsg = "Start Video Failed\n"
        fmsg += "StackCallid : " + callid
        self.retmsg.msg = fmsg
        return self.retmsg

class stopvideo(eventhandler):
    def handler(self):
        self.retmsg.msglevel = Msglevel.INFO
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        callid = str(self.match.group(1)).strip()
        fmsg = "Stop Video\n"
        fmsg += "StackCallid : " + callid
        self.retmsg.msg = fmsg
        return self.retmsg

class stopvideofailed(eventhandler):
    def handler(self):
        self.retmsg.msglevel = Msglevel.ERROR
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        callid = str(self.match.group(1)).strip()
        fmsg = "Stop Video Failed\n"
        fmsg += "StackCallid : " + callid
        self.retmsg.msg = fmsg
        return self.retmsg

class rotatelocalrender(eventhandler):
    def handler(self):
        self.retmsg.msglevel = Msglevel.INFO
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        callid = str(self.match.group(1)).strip()
        fmsg = "Rotate local render\n"
        fmsg += "StackCallid : " + callid
        self.retmsg.msg = fmsg
        return self.retmsg

class rotatelocalrenderfailed(eventhandler):
    def handler(self):
        self.retmsg.msglevel = Msglevel.ERROR
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        callid = str(self.match.group(1)).strip()
        fmsg = "Rotate local Failed\n"
        fmsg += "StackCallid : " + callid
        self.retmsg.msg = fmsg
        return self.retmsg

class rotateremoterender(eventhandler):
    def handler(self):
        self.retmsg.msglevel = Msglevel.INFO
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        callid = str(self.match.group(1)).strip()
        fmsg = "Rotate remote render \n"
        fmsg += "StackCallid : " + callid
        self.retmsg.msg = fmsg
        return self.retmsg

class rotateremoterenderfailed(eventhandler):
    def handler(self):
        self.retmsg.msglevel = Msglevel.ERROR
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        callid = str(self.match.group(1)).strip()
        fmsg = "Rotate remote Failed\n"
        fmsg += "StackCallid : " + callid
        self.retmsg.msg = fmsg
        return self.retmsg

class modifyrequest(eventhandler):
    def handler(self):
        self.retmsg.msglevel = Msglevel.WARNING
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        isvideo = str(self.match.group(1)).strip().lower()
        if isvideo == "true":
            self.retmsg.msg = "Upgrade Video"
            event = mapzhphrase("upgradecall", ReportScenariophrase)
        else:
            self.retmsg.msg = "Downgrade Video"
            event = mapzhphrase("downgradecall", ReportScenariophrase)

        self.retmsg.report = constructReport(type=ReportType.SCEEVENT_BASE,event=event, level=self.retmsg.msglevel)

        return self.retmsg


class invite2conf(eventhandler):
    def handler(self):
        self.retmsg.msglevel = Msglevel.WARNING
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        callid = str(self.match.group(1).strip())
        confid = str(self.match.group(2).strip())
        callidstr = "StackCallid: " + callid + "\n"
        confidstr = "Confid: " + confid
        self.retmsg.msg = "Invite Call to Conference\n" + callidstr + confidstr
        return self.retmsg

class modifyrequestfailed(eventhandler):
    def handler(self):
        self.retmsg.msglevel = Msglevel.ERROR
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        event=mapzhphrase("mdyfailed", ReportScenariophrase)
        self.retmsg.report = constructReport(type=ReportType.SCEEVENT_BASE, event=event, level=self.retmsg.msglevel)
        msg = str(self.match.group(1).strip())
        self.retmsg.msg = msg
        return self.retmsg

class startcall(eventhandler):
    '''
    imsservice start call : one pattern
    VoWiFiCall/VoLTECall
    '''
    def handler(self):
        callbearer = self.match.group(1)
        self.retmsg.msg = "start " + callbearer
        self.retmsg.msglevel = Msglevel.INFO
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)

        if callbearer == "VoWifiCall":
            event = mapzhphrase("startvowificall", ReportScenariophrase)
        else:
            event = mapzhphrase("startvoltecall", ReportScenariophrase)
        self.retmsg.report = constructReport(type=ReportType.SCEEVENT_BASE,event=event, level=self.retmsg.msglevel)
        return self.retmsg

class regupdate(eventhandler):
    def handler(self):
        self.retmsg.msglevel = Msglevel.INFO
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        clistate = self.match.group(1)
        eventstr = " VoWiFi Status Update to " + mapcode2str(str(clistate), Constantregstatecode)
        self.retmsg.msg = eventstr
        return self.retmsg

class servicecallback(eventhandler):
    '''
    complex handler to parse #####Vowifiserservice.java######
    the pattern is only one, the callback json
    sample:
    Notify the event: {"event_code":104,"event_name":"call_talking","id":2,"phone_num":"+917011821207","is_video":false}
    Notify the event: {"event_code":105,"event_name":"call_terminate","id":3,"state_code":335}
    Notify the event: {"event_code":110,"event_name":"call_hold_received","id":2}
    Notify the event: {"event_code":302,"event_name":"remote_video_resize","video_width":240,"video_height":320}
    Notify the event:  {"event_code":103,"event_name":"call_alerted","alert_type":57899,"id":3,"phone_num":"+917011821207","is_video":true}
    Notify the event: {"event_code":118,"event_name":"call_rtp_received","id":1,"rtp_received":true,"is_video":false}
    Notify the event: {"event_code":209,"event_name":"conf_part_update","id":23,"phone_num":"+917011821118","sip_uri":"sip:+917011821118@ims.mnc872.mcc405.3gppnetwork.org","conf_part_new_status":"disconnected"}
    '''
    def handler(self):
        servicestr = self.match.group(1).strip()
        try:
            servicejson = json.loads(servicestr)
            #event_name is must
            #enumerate the key in Constants.java
            eventstr = termreason = callidstr = alertstr = isvideostr = phonenumstr = sipuristr = ''
            videohight = videowidth = videoorient = rtprecv = confpartstatus = ''
            msgstr = ''
            #there will event skipped, which means other key will have better phrase
            skipevent = list()
            skipevent.append('call_terminate')
            skipevent.append("call_rtp_received")
            skipevent.append("conf_rtp_received")


            #event to be ignored, like rtcp changed
            ignoreevent = list()
            ignoreevent.append('call_rtcp_changed')
            ignoreevent.append('conf_rtcp_changed')

            #event should be colored blue
            infoevent = list()
            infoevent.append("call_incoming")
            infoevent.append("call_talking")
            infoevent.append("call_terminate") #actually it is skipped
            infoevent.append("call_hold_ok")
            infoevent.append("call_resume_ok")
            infoevent.append("call_hold_received")
            infoevent.append("call_resume_received")
            infoevent.append("call_add_video_ok")
            infoevent.append("call_remove_video_ok")
            infoevent.append("call_add_video_request")
            infoevent.append("call_add_video_cancel")
            infoevent.append("call_rtp_received") #actually it is skipped
            infoevent.append("call_is_focus")
            infoevent.append("conf_connected")
            infoevent.append("conf_disconnected")
            infoevent.append("conf_invite_accept")
            infoevent.append("conf_kick_accept")
            infoevent.append("conf_part_update")
            infoevent.append("conf_hold_ok")
            infoevent.append("conf_resume_ok")
            infoevent.append("conf_hold_received")
            infoevent.append("conf_resume_received")

            infoevent.append("conf_outgoing")
            infoevent.append("call_outgoing")

            #some browncolor, other infoevent will be green
            browncolor = list()
            browncolor.append("call_incoming")
            browncolor.append("call_add_video_request")
            browncolor.append("call_add_video_cancel")
            browncolor.append("conf_disconnected")
            browncolor.append("conf_outgoing")
            browncolor.append("call_outgoing")
            browncolor.append("conf_part_update")
            #event should be colored red
            errevent = list()
            errevent.append("call_hold_failed")
            errevent.append("call_resume_failed")
            errevent.append("call_add_video_failed")
            errevent.append("call_remove_video_failed")
            errevent.append("conf_invite_failed")
            errevent.append("conf_kick_failed")
            errevent.append("conf_hold_failed")
            errevent.append("conf_resume_failed")

            self.retmsg.msglevel = Msglevel.INFO
            self.retmsg.color = maplevel2color(self.retmsg.msglevel)

            if 'event_name' in servicejson:
                curevent = str(servicejson['event_name']).strip()
                #rtcp changed is too verbose , so ignore it.
                if curevent in ignoreevent:
                    return None

                if curevent not in skipevent:
                    #some event should be highlighted
                    #just change the color here, phrase is not converted.
                    if curevent in infoevent:
                        if curevent in browncolor:
                            self.retmsg.msglevel = Msglevel.WARNING
                            self.retmsg.color = maplevel2color(self.retmsg.msglevel)
                        else:
                            self.retmsg.msglevel = Msglevel.NORMAL
                            self.retmsg.color = maplevel2color(self.retmsg.msglevel)
                        event = mapzhphrase(curevent, ReportScenariophrase)
                        self.retmsg.report = constructReport(type=ReportType.SCEEVENT_BASE,event=event, level=self.retmsg.msglevel)
                    elif curevent in errevent:
                        self.retmsg.msglevel = Msglevel.ERROR
                        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
                        event = mapzhphrase(curevent, ReportScenariophrase)
                        self.retmsg.report = constructReport(type=ReportType.SCEEVENT_BASE,event=event, level=self.retmsg.msglevel)

                    eventstr = 'Event: ' + curevent + '\n'
                if curevent == "call_terminate":
                    if 'state_code' in servicejson:
                        imsreason =  mapcode2str(str(servicejson['state_code']), Constantimsreason)
                        termreason = 'Term Call: ' + imsreason + '\n'
                        self.retmsg.msglevel = Msglevel.WARNING
                        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
                        event = mapzhphrase("call_terminate", ReportScenariophrase, post=imsreason)
                        self.retmsg.report = constructReport(type=ReportType.SCEEVENT_BASE,event=event, level=self.retmsg.msglevel)

                if curevent == "call_rtp_received" or curevent == "conf_rtp_received":
                    if 'rtp_received' in servicejson and 'is_video' in servicejson:
                        #python will convert true to True, false to False
                        rtpstate = str(servicejson['rtp_received']).lower()
                        isvideo = str(servicejson['is_video']).lower()
                        if rtpstate == 'true':

                            self.retmsg.msglevel = Msglevel.NORMAL
                            self.retmsg.color = maplevel2color(self.retmsg.msglevel)
                            if curevent == "call_rtp_received" :
                                if isvideo == 'false':
                                    rtprecv = "Voice RTP received\n"
                                    event = mapzhphrase("voicecallrtp", ReportScenariophrase)
                                else:
                                    rtprecv = "Video RTP received\n"
                                    event = mapzhphrase("videocallrtp", ReportScenariophrase)
                            else:
                                if isvideo == 'false':
                                    rtprecv = "Conf Voice RTP received\n"
                                    event = mapzhphrase("voiceconfrtp", ReportScenariophrase)
                                else:
                                    rtprecv = "Conf Video RTP received\n"
                                    event = mapzhphrase("videoconfrtp", ReportScenariophrase)
                            self.retmsg.report = constructReport(type=ReportType.SCEEVENT_BASE,event=event, level=self.retmsg.msglevel)
                        else:
                            #show error msg.
                            #service no rtp ,but need ImsCM confirm
                            self.retmsg.msglevel = Msglevel.WARNING
                            self.retmsg.color = maplevel2color(self.retmsg.msglevel)
                            if curevent == "call_rtp_received":
                                if isvideo == 'false':
                                    rtprecv = "No Voice RTP received\n"
                                    event = mapzhphrase("voicecallnortp", ReportScenariophrase)
                                else:
                                    rtprecv = "No Video RTP received\n"
                                    event = mapzhphrase("video", ReportScenariophrase)
                            else:
                                if isvideo == "false":
                                    rtprecv = "Conf No Voice RTP received\n"
                                    event = mapzhphrase("voiceconfnortp", ReportScenariophrase)
                                else:
                                    rtprecv = "Conf No Video RTP received\n"
                                    event = mapzhphrase("videoconfnortp", ReportScenariophrase)
                            self.retmsg.report = constructReport(type=ReportType.SCEEVENT_BASE,event=event, level=self.retmsg.msglevel)

            if 'id' in servicejson:
                callidstr = "StackCallid: " + str(servicejson['id']) + '\n'
            if 'alert_type' in servicejson:
                alertstr = "User Alert: " + mapcode2str(str(servicejson['alert_type']), Constantcallcode) + '\n'
            if 'is_video' in servicejson:
                if str(servicejson['is_video']).lower() == "false":
                    isvideostr = "calltype: Voice Call\n"
                else:
                    isvideostr = "calltype: Video Call\n"
            if 'phone_num' in servicejson:
                phonenumstr = "PhoneNum :" + servicejson['phone_num'] + '\n'
            if 'sip_uri' in servicejson:
                #seems not useful, so comment here
                #sipuristr = "SIP URI :" + servicejson['sip_uri'] + '\n'
                sipuristr = ''
            if 'video_height' in servicejson:
                videohight = "Video Height :" + str(servicejson['video_height']) + '\n'
            if 'video_width' in servicejson:
                videowidth = "Video Width :" + str(servicejson['video_width']) + '\n'
            if 'video_orientation' in servicejson:
                #seems dead code ... Orz~
                pass
            if 'conf_part_new_status' in servicejson:
                confpartstatus = "Conf Part State: " + str(servicejson['conf_part_new_status'])
            #assemble the str
            self.retmsg.msg = eventstr + rtprecv + termreason + callidstr + alertstr + isvideostr + phonenumstr + sipuristr + \
                         videohight + videowidth + videoorient + confpartstatus
            return self.retmsg
        except ValueError:
            return None

class loginstatus(eventhandler):
    '''
    login status, two patterns: ip, pcscf ip
    '''
    def handler(self):
        ip = self.match.group(1).strip()
        pcscfip = self.match.group(2).strip()
        ipstr = "IP: " + ip + '\n'
        pcscfipstr = "P-CSCF: " + pcscfip + '\n'
        self.retmsg.msglevel = Msglevel.INFO
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        self.retmsg.msg = 'Login \n' + ipstr + pcscfipstr
        return self.retmsg


class logoutstatus(eventhandler):
    '''
    logout pattern: Constantregstate
    '''
    def handler(self):
        regstr = mapcode2str(str(self.match.group(1)).strip(),Constantregstate)
        self.retmsg.msglevel = Msglevel.WARNING
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        self.retmsg.msg = "Try to Logout \n"+"RegState is " + regstr
        return self.retmsg

class drstatus(eventhandler):
    '''
    data route pattern, one: volte/vowifi/none
    '''
    def handler(self):
        drstate = str(self.match.group(1))
        drstr = "Update data router to "+drstate
        self.retmsg.msglevel = Msglevel.INFO
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        self.retmsg.msg = drstr
        event = mapzhphrase("drstatus", ReportScenariophrase, post=drstate)
        self.retmsg.report = constructReport(type=ReportType.SCEEVENT_BASE,event=event, level=self.retmsg.msglevel)
        return self.retmsg

class wfcmode(eventhandler):
    def handler(self):
        mode = str(self.match.group(1))
        modestr = "WiFi-Calling Mode: " + mode
        self.retmsg.msglevel = Msglevel.WARNING
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        self.retmsg.msg = modestr
        return self.retmsg

class wfcstatus(eventhandler):
    '''
    wificalling flag, one pattern
    database has changed, mIsWifiCallingEnabled = true
    '''
    def handler(self):
        wfcdb = str(self.match.group(1))
        wfcstr = ""
        if wfcdb == "true":
            wfcstr = "Enable WiFi-Calling"
            event = mapzhphrase("enwfc", ReportHandoverphrase)
        else:
            wfcstr = "Disable WiFi-Calling"
            event = mapzhphrase("disenwfc", ReportHandoverphrase)

        self.retmsg.msglevel = Msglevel.WARNING
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        self.retmsg.msg = wfcstr

        self.retmsg.report = constructReport(type=ReportType.USEREVENT_BASE,event=event, level=self.retmsg.msglevel)

        return self.retmsg

class geticon(eventhandler):
    '''
    get vowifi/volte icon
    '''
    def handler(self):
        ltestr = self.match.group(1)
        wifistr = self.match.group(2)
        if ltestr == "true":
            if wifistr == "true":
                iconstr = "show VoWiFi and VoLTE signal icons"
                level = Msglevel.ERROR
            else:
                iconstr = "show VoLTE signal icon"
                level = Msglevel.NORMAL

        else:
            if wifistr == "true":
                iconstr = "show VoWiFi signal icon"
                level = Msglevel.NORMAL
            else:
                iconstr = "No VoLTE/VoWiFi signal icon"
                level = Msglevel.WARNING
        self.retmsg.msg = iconstr
        self.retmsg.msglevel = level
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        return self.retmsg

class setimsregaddr(eventhandler):
    '''
    set ims reg addr, one pattern
    '''
    def handler(self):
        regaddr = self.match.group(1).strip()
        self.retmsg.msg = "SetIMSRegAddr:\n   " + regaddr
        self.retmsg.msglevel = Msglevel.INFO
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        return self.retmsg

class getimsregaddr(eventhandler):
    '''
    set ims reg addr, one pattern
    '''
    def handler(self):
        regaddr = self.match.group(1).strip()
        self.retmsg.msglevel = Msglevel.INFO
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        self.retmsg.msg = "GetIMSRegAddr:\n   " + regaddr
        return self.retmsg

class getpcscfregaddr(eventhandler):
    '''
    set ims reg addr, one pattern
    '''
    def handler(self):
        pcscfaddr = self.match.group(1).strip()
        self.retmsg.msglevel = Msglevel.INFO
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        self.retmsg.msg = "GetPCSCFAddr:\n   " + pcscfaddr
        return self.retmsg


class turnmute(eventhandler):
    def handler(self):
        self.retmsg.msglevel = Msglevel.WARNING
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        mute = str(self.match.group(1)).strip().lower()
        mutestr = ""
        if mute == "false":
            mutestr = "Unmuted"
        else:
            mutestr = "Muted"
        self.retmsg.msg = mutestr
        return self.retmsg

class mutestatus(eventhandler):
    '''
    mute status: one pattern
    true muted; false unmute
    '''
    def handler(self):
        muteval = str(self.match.group(1))
        self.retmsg.msglevel = Msglevel.WARNING
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        if muteval == 'true':
            self.retmsg.msg = "Muted"
        else:
            self.retmsg.msg = "UnMuted"

        return self.retmsg

class defaultfailed(eventhandler):
    def handler(self):
        self.retmsg.msglevel = Msglevel.ERROR
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        self.retmsg.msg = str(self.match.group(1))
        event = mapzhphrase("callfailed", ReportScenariophrase)
        self.retmsg.report = constructReport(type=ReportType.SCEEVENT_BASE ,event=event, level=self.retmsg.msglevel)
        return self.retmsg

class makecallstatus(eventhandler):
    '''
    make call , one pattern , callee number
    '''
    def handler(self):
        callee = str(self.match.group(1)).strip()
        self.retmsg.msglevel = Msglevel.WARNING
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        self.retmsg.msg = "Make call to " + callee
        event = mapzhphrase("apmakecall", ReportScenariophrase, post=callee)
        self.retmsg.report = constructReport(type=ReportType.SCEEVENT_BASE ,event=event, level=self.retmsg.msglevel)
        return self.retmsg



class akastatus(eventhandler):
    '''
    aka status
    one pattern DB means auth correctly, DC means sync failure
    '''
    def handler(self):
        akatag = str(self.match.group(1)).strip()[:2]
        if akatag == "DB":
            akastr = "EAP-AKA AUTH correctly"
            self.retmsg.msglevel = Msglevel.NORMAL
            self.retmsg.color = maplevel2color(self.retmsg.msglevel)
            self.retmsg.msg = akastr
            event = mapzhphrase("akaok", ReportScenariophrase)
            self.retmsg.report = constructReport(type=ReportType.SCEEVENT_BASE ,event=event, level=self.retmsg.msglevel)
            return self.retmsg
        elif akatag == "DC":
            akastr = "EAP-AKA AUTH SYNC Failure"
            self.retmsg.msglevel = Msglevel.ERROR
            self.retmsg.color = maplevel2color(self.retmsg.msglevel)
            self.retmsg.msg = akastr
            event = mapzhphrase("akafailed", ReportScenariophrase)
            self.retmsg.report = constructReport(type=ReportType.SCEEVENT_BASE ,event=event, level=self.retmsg.msglevel)
            return self.retmsg
        else:
            return None


class reregstatus(eventhandler):
    '''
    re-register info, two pattern: access type and access info
    '''
    def handler(self):
        acctype = str(self.match.group(1).strip())
        acctype = mapcode2str(acctype, Constantaccnettype)
        accinfo = self.match.group(2)
        self.retmsg.msglevel = Msglevel.INFO
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        acctypestr = "Access Type:" + acctype + '\n'
        accinfostr =  "Access Info:" + accinfo + '\n'
        self.retmsg.msg = "start to Re-Register\n" + acctypestr + accinfostr
        return self.retmsg


class regstatus(eventhandler):
    '''
    Get the register state changed callback: {\"event_code\":.*,\"event_name\":\"(.*)\",\"state_code\":(.*)}"
    event name , state code
    '''
    def handler(self):

        regstr = self.match.group(1).strip()
        try:
            regjson = json.loads(regstr)
            eventname = regjson['event_name']
            statecode = regjson['state_code']
            #only return when statecode >= 0xE100 or -1

            #seems MTC_CLI_REG_BASE+16: other error is not error,
            if isRegError(statecode):
                self.retmsg.msglevel = Msglevel.ERROR
                self.retmsg.color = maplevel2color(self.retmsg.msglevel)
                eventstr = map2phrase(eventname, Reportregphrase) + '\n'
                mappedstr = str(statecode) + '-->' + mapcode2str(str(statecode),Constantregerrcode)
                statestr = "state: " + mappedstr

                event = mapzhphrase(eventname, Reportregphrase)
                self.retmsg.report = constructReport(event=event, level=self.retmsg.msglevel, errorstr=mappedstr)
                self.retmsg.msg = eventstr + statestr
                return self.retmsg
            else:
                #in service's log, -1 is default value when login_ok or refresh_ok
                #login_ok, login_failed, logouted,refresh_ok, refresh_failed
                if eventname == "login_failed" or eventname == "refresh_failed":
                    self.retmsg.msglevel = Msglevel.ERROR
                elif eventname == "login_ok" or eventname == "refresh_ok":
                    self.retmsg.msglevel = Msglevel.NORMAL
                else:
                    self.retmsg.msglevel = Msglevel.INFO
                self.retmsg.color = maplevel2color(self.retmsg.msglevel)
                eventstr = map2phrase(eventname, Reportregphrase)

                if eventname == "state_update":
                    #this code is not working here, mtc_cli.h
                    #[VoWifiService]RegisterService: Get the register state changed callback, register state: 1, code: 57600
                    #[Adapter]VoWifiRegisterManager: Get the register state changed callback: {"event_code":6,"event_name":"state_update","state_code":1}
                    eventstr += " to " + mapcode2str(str(statecode), Constantregstatecode)
                    #hard code here, we use service to track
                    return None
                else:
                    #state_update event is some kind of verbose, will not be included in report
                    event = mapzhphrase(eventname, Reportregphrase)
                    self.retmsg.report = constructReport(event=event, level=self.retmsg.msglevel)

                self.retmsg.msg = eventstr
                return self.retmsg
        except ValueError:
            return None

class subs504(eventhandler):
    def handler(self):
        self.retmsg.msglevel = Msglevel.ERROR
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        self.retmsg.msg = "Server send 504 Timeout, Re-Register"
        return self.retmsg

class news2bstatus(eventhandler):
    def handler(self):
        s2bstr = self.match.group(1).strip()
        try:
            s2bjson = json.loads(s2bstr)
            #notifyS2bAttachSuccess, notifyS2bResult
            #we only care about attach_successed, attach_stopped, attach_failed
            # {"event_code":1,"event_name":"attach_successed","session_id":1,"local_ip4":"10.135.191.151","local_ip6":"2404:8d00:80b:8156:7bab:a1e2:cd9e:2f50","pcscf_ip4":"10.34.129.240;10.34.193.240","pcscf_ip6":"2407:ed00:1200:1000::1;2407:ed00:2200:1000::1","pref_ip4":false,"is_sos":false}
            # {"event_code":4,"event_name":"attach_stopped","session_id":1,"state_code":53760}
            action = s2bjson['event_name']
            if action == "attach_successed":
                statestr = "epdg attach successfully\n"
                ipv4str = ipv6str = pcscfv4str = dnsv4str = dnsv6str= pcscfv6str = prefipv4str = issosstr = sessidstr = ''
                if 'local_ip4' in s2bjson:
                    ipv4str = "     IPv4: " + s2bjson['local_ip4'] + '\n'
                if 'local_ip6' in s2bjson:
                    ipv6str = "     IPv6: " + s2bjson['local_ip6'] + '\n'
                if 'dns_ip4' in s2bjson:
                    dnsv4str = "DNS IPv4: " + s2bjson['dns_ip4'] + '\n'
                if 'dns_ip6' in s2bjson:
                    dnsv6str = "DNS IPv6: " + s2bjson['dns_ip6'] + '\n'
                if 'pcscf_ip4' in s2bjson:
                    pcscfv4str = "   PCSCF IPv4: " + s2bjson['pcscf_ip4'] + '\n'
                if 'pcscf_ip6' in s2bjson:
                    pcscfv6str = "   PCSCF IPv6: " + s2bjson['pcscf_ip6'] + '\n'
                if 'pref_ip4' in s2bjson:
                    prefipv4str = "Prefered IPv4: " + str(s2bjson['pref_ip4']) + '\n'
                if 'is_sos' in s2bjson:
                    issosstr = " Tunnel For Sos: " + str(s2bjson['is_sos']) + '\n'
                if 'session_id' in s2bjson:
                    sessidstr = " Session id: " + str(s2bjson['session_id']) + '\n'
                self.retmsg.msglevel = Msglevel.NORMAL
                self.retmsg.color = maplevel2color(self.retmsg.msglevel)
                self.retmsg.msg = statestr + ipv4str + ipv6str + dnsv4str+ dnsv6str +pcscfv4str + pcscfv6str + prefipv4str + issosstr + sessidstr
                event = mapzhphrase("successed", Reports2bphrase)
                self.retmsg.report = constructReport(event=event, level=self.retmsg.msglevel)

            elif action == "attach_stopped":
                sessidstr = ''
                errorcode = ''
                if 'state_code' in s2bjson:
                    errorcode = s2bjson['state_code']
                if 'session_id' in s2bjson:
                    sessidstr = " Session id: " + str(s2bjson['session_id']) + '\n'
                statestr = "epdg attach stopped\n"
                #add three spaces for alignment, not working...Orz...
                mappedstr = str(errorcode) + '-->' + mapcode2str(str(errorcode), Constants2berrcode)
                errorstr = " StateCode: " + mappedstr + '\n'

                #in s2b stopped, the statecode should be checked
                if isS2bError(errorcode):
                    self.retmsg.msglevel = Msglevel.ERROR
                    event = mapzhphrase("stopped_abnormally", Reports2bphrase)
                    self.retmsg.report = constructReport(event=event, level=self.retmsg.msglevel, errorstr=mappedstr)
                else:
                    self.retmsg.msglevel = Msglevel.WARNING
                    event = mapzhphrase("stopped", Reports2bphrase)
                    self.retmsg.report = constructReport(event=event, level=self.retmsg.msglevel, errorstr=mappedstr)

                self.retmsg.color = maplevel2color(self.retmsg.msglevel)
                self.retmsg.msg = statestr + errorstr + sessidstr

            elif action == "attach_failed":
                sessidstr = ''
                errorcode = ''
                if 'state_code' in s2bjson:
                    errorcode = str(s2bjson['state_code'])
                if 'session_id' in s2bjson:
                    sessidstr = " Session id: " + str(s2bjson['session_id']) + '\n'
                statestr = "epdg attach failed\n"
                mappedstr = str(errorcode) + '-->' + mapcode2str(str(errorcode), Constants2berrcode)
                errorstr = "   stateCode: " +  mappedstr + '\n'

                self.retmsg.msglevel = Msglevel.ERROR
                self.retmsg.color = maplevel2color(self.retmsg.msglevel)
                self.retmsg.msg = statestr + errorstr + sessidstr

                event = mapzhphrase("failed", Reports2bphrase)
                self.retmsg.report = constructReport(event=event, level=self.retmsg.msglevel, errorstr=mappedstr)

            else:
                return None
            return self.retmsg
        except ValueError:
            return None

class s2binfo(eventhandler):
    def handler(self):
        s2btype = mapcode2str(str(self.match.group(1).strip()), ConstantS2bType)
        imsi = str(self.match.group(2).strip())
        hplmn = str(self.match.group(3).strip())
        vplmn = str(self.match.group(4).strip())
        s2btypestr = "S2b Type: " + s2btype + '\n'
        imsistr = "imsi: " + imsi + '\n'
        hplmnstr = "HPLMN: " + hplmn + '\n'
        vplmnstr = "VPLMN: " + vplmn + '\n'
        statestr = "Start Epdg with:\n"
        self.retmsg.msglevel = Msglevel.INFO
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        self.retmsg.msg = statestr + s2btypestr + imsistr + hplmnstr + vplmnstr
        return self.retmsg

class olds2bstatus(eventhandler):
    '''
    s2b status check
    three kinds:
    {"security_json_action":"security_json_action_s2b_failed","security_json_param_error_code":53760}
    {"security_json_action":"security_json_action_s2b_stopped","security_json_param_error_code":53959,"security_json_param_handover":true}
    {"security_json_action":"security_json_action_s2b_successed","security_json_param_local_ip4":"192.168.1.11","security_json_param_local_ip6":"2001:0:0:2::1","security_json_param_pcscf_ip4":"192.168.1.12;","security_json_param_pcscf_ip6":"2001:0:0:2::2;","security_json_param_dns_ip4":"0.0.0.0","security_json_param_pref_ip4":false}
    '''
    def handler(self):
        #input str is ALWAYS json string.
        s2bstr = self.match.group(1).strip()
        try:
            s2bjson = json.loads(s2bstr)
            action = s2bjson['security_json_action']

            if action == 'security_json_action_s2b_failed':
                errorcode = s2bjson['security_json_param_error_code']
                statestr = "epdg attach failed\n"
                mappedstr = str(errorcode) + '-->' + mapcode2str(str(errorcode), Constants2berrcode)
                errorstr = "   stateCode: " +  mappedstr

                self.retmsg.msglevel = Msglevel.ERROR
                self.retmsg.color = maplevel2color(self.retmsg.msglevel)
                self.retmsg.msg = statestr + errorstr

                event = mapzhphrase("failed", Reports2bphrase)
                self.retmsg.report = constructReport(event=event, level=self.retmsg.msglevel, errorstr=mappedstr)
            elif action == "security_json_action_s2b_stopped":
                errorcode = s2bjson['security_json_param_error_code']
                ishandover = s2bjson['security_json_param_handover']
                statestr = "epdg attach stopped\n"
                #add three spaces for alignment, not working...Orz...
                hostr = " ishandover: " + str(ishandover) + '\n'
                mappedstr = str(errorcode) + '-->' +mapcode2str(str(errorcode), Constants2berrcode)
                errorstr = " StateCode: " + mappedstr

                #in s2b stopped, the statecode should be checked
                if isS2bError(errorcode):
                    self.retmsg.msglevel = Msglevel.ERROR
                    event = mapzhphrase("stopped_abnormally", Reports2bphrase)
                    self.retmsg.report = constructReport(event=event, level=self.retmsg.msglevel, errorstr=mappedstr)
                else:
                    self.retmsg.msglevel = Msglevel.WARNING
                    event = mapzhphrase("stopped", Reports2bphrase)
                    self.retmsg.report = constructReport(event=event, level=self.retmsg.msglevel, errorstr=mappedstr)

                self.retmsg.color = maplevel2color(self.retmsg.msglevel)
                self.retmsg.msg = statestr + hostr + errorstr

            elif action == "security_json_action_s2b_successed":
                statestr = "epdg attach successfully\n"
                ipv4str = ipv6str = pcscfv4str = pcscfv6str = dnsv4str = dnsv6str = ''
                if 'security_json_param_local_ip4' in s2bjson:
                    ipv4str = "     IPv4: " + s2bjson['security_json_param_local_ip4'] + '\n'
                if 'security_json_param_local_ip6' in s2bjson:
                    ipv6str = "     IPv6: " + s2bjson['security_json_param_local_ip6'] + '\n'
                if 'security_json_param_pcscf_ip4' in s2bjson:
                    pcscfv4str = "   PCSCF IPv4: " + s2bjson['security_json_param_pcscf_ip4'] + '\n'
                if 'security_json_param_pcscf_ip6' in s2bjson:
                    pcscfv6str = "   PCSCF IPv6: " + s2bjson['security_json_param_pcscf_ip6'] + '\n'
                if 'security_json_param_dns_ip4' in s2bjson:
                    dnsv4str = "   DNS IPv4: " + s2bjson['security_json_param_dns_ip4'] + '\n'
                if 'security_json_param_dns_ip6' in s2bjson:
                    dnsv6str = "   DNS IPv6: " + s2bjson['security_json_param_dns_ip6'] + '\n'
                self.retmsg.msglevel = Msglevel.NORMAL
                self.retmsg.color = maplevel2color(self.retmsg.msglevel)
                self.retmsg.msg = statestr + ipv4str + ipv6str + pcscfv4str + pcscfv6str + dnsv4str + dnsv6str
                event = mapzhphrase("successed", Reports2bphrase)
                self.retmsg.report = constructReport(event=event, level=self.retmsg.msglevel)
            else:
                return None

            return self.retmsg
        except ValueError:
            return None

class simstatus(eventhandler):
    '''
    Note: *HEAVILY* rely on definition
    two patterns, one is sim action(get/update), two is plmn
    updateSimState: get primary USIM card plmn = 001010
    '''
    def handler(self):
        simaction = str(self.match.group(1)).strip()
        plmn = str(self.match.group(2)).strip()
        self.retmsg.msglevel = Msglevel.INFO
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)

        if simaction == "get":
            simstr = "Get Primary Sim Card\n"
        elif simaction == "update":
            simstr = "Change Primary Sim Card\n"
        else:
            return None
        plmnstr = "PLMN: " + plmn + '\n'
        operatorstr = ""
        if len(plmn) >= 5:
            mnc = plmn[0:3]
            mcc = plmn[3:]
            try:
                mcode = mobile_codes.mcc_mnc(mnc, mcc)
                operator = mcode.operator
                operatorstr = "Operator: " + operator + '\n'
            except KeyError,e:
                operatorstr = ""
        self.retmsg.msg = simstr + plmnstr + operatorstr
        return self.retmsg

class newsimstatus(eventhandler):
    '''
    Note: *HEAVILY* rely on definition
    two patterns, one is sim action(get/update), two is plmn
    updateSimState: get primary USIM card plmn = 001010
    '''
    def handler(self):
        plmn = str(self.match.group(1)).strip()
        self.retmsg.msglevel = Msglevel.INFO
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)

        plmnstr = "PLMN: " + plmn + '\n'
        operatorstr = ""
        if len(plmn) >= 5:
            mnc = plmn[0:3]
            mcc = plmn[3:]
            try:
                mcode = mobile_codes.mcc_mnc(mnc, mcc)
                operator = mcode.operator
                operatorstr = "Operator: " + operator + '\n'
            except KeyError,e:
                operatorstr = ""
        self.retmsg.msg = plmnstr + operatorstr
        return self.retmsg

class simchanged7(eventhandler):
    '''
    just to match android 7.0's sim changed logic in ImsCM
    '''
    def handler(self):
        self.retmsg.msglevel = Msglevel.WARNING
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        self.retmsg.msg = "Primary Sim Card Changed."
        return self.retmsg

class telepdgfail(eventhandler):
    def handler(self):
        self.retmsg.msglevel = Msglevel.ERROR
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        self.retmsg.msg = "Epdg Attach Failed"
        return self.retmsg

class telepdgsuccess(eventhandler):
    def handler(self):
        self.retmsg.msglevel = Msglevel.NORMAL
        self.retmsg.msg = "Epdg Attach Successfully"
        switchrequest = str(self.match.group(1)).strip()
        if switchrequest == "null":
            self.retmsg.msglevel = Msglevel.ERROR
            self.retmsg.msg = "Epdg Attached\n but No FeatureSwitchRequest"
            event = mapzhphrase("attachexception", ReportTelphrase)
            self.retmsg.report = constructReport(event=event, level=self.retmsg.msglevel)
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        return self.retmsg

class telvowifiunavail(eventhandler):
    def handler(self):
        pdnstate = str(self.match.group(1)).strip()
        if pdnstate == "false":
            pdnstatestr = "PDN Deactived"
        else:
            pdnstatestr = "PDN Actived"
        self.retmsg.msglevel = Msglevel.ERROR
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        self.retmsg.msg = "VoWiFi Unavailable\n" +pdnstatestr
        return self.retmsg

class switcherror(eventhandler):
    def handler(self):
        self.retmsg.msglevel = Msglevel.ERROR
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        regtype = str(self.match.group(1)).strip()
        regtypestr = mapcode2str(regtype, ConstantFeatureType)
        self.retmsg.msg = "Don't switch to " + regtypestr
        return self.retmsg

class slotstatus(eventhandler):
    '''
    two pattern: slot id,  status str
    '''
    def handler(self):
        self.retmsg.msglevel = Msglevel.INFO
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        slot = str(self.match.group(1)).strip()
        #simstatus may contain "
        simstatus = str(self.match.group(2)).strip().replace('"','').replace("'", '')
        slotstr = "SimCard Slot " + slot + '\n'
        simstatusstr = "Status " + simstatus
        self.retmsg.msg = slotstr + simstatusstr
        return self.retmsg

class imscmpending(eventhandler):
    def handler(self):
        self.retmsg.msglevel = Msglevel.WARNING
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        curreq = str(self.match.group(1)).strip().replace('"', '').replace("'",'')
        pendreq = str(self.match.group(2)).strip().replace('"', '').replace("'",'')
        curreq = mapcode2str(curreq, ConstantImsReq)
        pendreq = mapcode2str(pendreq, ConstantImsReq)

        curreqstr = "Current Req:" + curreq  + '\n'
        pendreqstr ="Pending Req:" + pendreq + '\n'
        self.retmsg.msg = curreqstr + pendreqstr
        return self.retmsg

class qos2volte(eventhandler):
    '''
    one pattern: audio, video
    loopAudioCallQos: Vowifi handover to Volte
    loopVideoCallQos: Vowifi handover to Volte
    '''
    def handler(self):
        calltype = str(self.match.group(1)).strip()
        self.retmsg.msglevel = Msglevel.INFO
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        hostr = "Poor " + calltype + " Qos\n" #" or Strong LTE signal\n"
        hostr += calltype + " Call Handover to VoLTE\n"
        if calltype == "Video":
            event=mapzhphrase("videoqos2lte", ReportHandoverphrase)
        else:
            event=mapzhphrase("voiceqos2lte", ReportHandoverphrase)

        self.retmsg.report = constructReport(type=ReportType.HOALGO_BASE, event=event, level=self.retmsg.msglevel)
        self.retmsg.msg = hostr
        return self.retmsg

class callthreshholdho(eventhandler):
    '''
    two pattern: calltype, ho direct
        loopAudioCallThreshold: Volte handover to Vowifi
        loopAudioCallThreshold: Vowifi handover to Volte
        loopVideoCallThreshold: Vowifi handover to Volte
        loopVideoCallThreshold: Volte handover to VoWifi
    '''
    def handler(self):
        calltype = str(self.match.group(1)).strip()
        hodirect = str(self.match.group(2)).strip()
        hostr = ''
        self.retmsg.msglevel = Msglevel.INFO
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        if hodirect == "Vowifi":
            hostr = "Strong WiFi signal\n"
            event=mapzhphrase("incallrssiho2wifi", ReportHandoverphrase)
            self.retmsg.report = constructReport(type=ReportType.HOALGO_BASE, event=event, level=self.retmsg.msglevel)
        else:
            hostr = "Strong LTE signal\n"

        hostr += calltype + " Call Handover to " + hodirect
        self.retmsg.msg = hostr
        return self.retmsg

class idlethreshholdho(eventhandler):
    '''
    one pattern: hodirect
    loopProcessIdleThreshold: Vowifi switch to Volte
    loopProcessIdleThreshold: Volte switch to Vowifi
    '''
    def handler(self):
        hodirect = str(self.match.group(1)).strip()
        self.retmsg.msglevel = Msglevel.INFO
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        hostr = ''
        if hodirect == "Vowifi":
            hostr = "Strong WiFi signal\n"
            event=mapzhphrase("rssiho2wifi", ReportHandoverphrase)
            self.retmsg.report = constructReport(type=ReportType.HOALGO_BASE, event=event, level=self.retmsg.msglevel)
        else:
            hostr = "Weak WiFi signal\n"
        hostr +=  " Idle Handover to " + hodirect
        self.retmsg.msg = hostr
        return self.retmsg

class idleautovowifi(eventhandler):
    def handler(self):
        self.retmsg.msglevel = Msglevel.INFO
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        hostr = "Idle switch to VoWiFi"
        event=mapzhphrase("autowifi", ReportHandoverphrase)
        self.retmsg.report = constructReport(type=ReportType.HOALGO_BASE, event=event, level=self.retmsg.msglevel)
        self.retmsg.msg = hostr
        return self.retmsg

class imscmhandlemsgerror(eventhandler):
    '''
    one pattern: errormsg
    '''
    def handler(self):
        errorstr = str(self.match.group(1)).strip()
        self.retmsg.msglevel = Msglevel.ERROR
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        self.retmsg.msg = "Error happened when " + errorstr
        event=mapzhphrase(errorstr, ReportHandoverphrase)
        self.retmsg.report = constructReport(type=ReportType.PHONEEVENT_BASE, event=event, level=self.retmsg.msglevel)
        return self.retmsg

class imscmnortp(eventhandler):
    '''
    two pattern: call type, isvideo

    '''
    def handler(self):
        calltype = str(self.match.group(1)).strip()
        isvideo = str(self.match.group(2)).strip().lower()
        if isvideo == "true":
            nortp = "Video"
            event = mapzhphrase("videonortp", ReportHandoverphrase)
        else:
            nortp = "Audio"
            event = mapzhphrase("voicenortp", ReportHandoverphrase)

        nortpstr = "No " + nortp  + " in " + calltype
        self.retmsg.msglevel = Msglevel.ERROR
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        self.retmsg.msg = nortpstr
        self.retmsg.report = constructReport(type=ReportType.PHONEEVENT_BASE, event=event, level=self.retmsg.msglevel)
        return self.retmsg

class imscmnortp2(eventhandler):
    '''
    two pattern: call type, isvideo

    '''
    def handler(self):
        callmode = str(self.match.group(1)).strip()
        calltype = str(self.match.group(2)).strip()
        isvideo = str(self.match.group(3)).strip().lower()
        if isvideo == "true":
            nortp = "Video"
            event = mapzhphrase("videonortp", ReportHandoverphrase)
        else:
            nortp = "Audio"
            event = mapzhphrase("voicenortp", ReportHandoverphrase)

        nortpstr = callmode + " No " + nortp  + " in " + calltype
        self.retmsg.msglevel = Msglevel.ERROR
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        self.retmsg.msg = nortpstr
        self.retmsg.report = constructReport(type=ReportType.PHONEEVENT_BASE, event=event, level=self.retmsg.msglevel)
        return self.retmsg

class imscmopfailed(eventhandler):
    '''
    two pattern: operation, reason
    operationFailed: id = 1, type = "OPERATION_HANDOVER_TO_VOLTE", failed reason = VOLTE pdn failed
    '''
    def handler(self):
        self.retmsg.msglevel = Msglevel.ERROR
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        operation = str(self.match.group(1)).strip()
        reason = str(self.match.group(2)).strip()
        operationstr = operation + " Failed\n"
        reasonstr = "Reason: " + mapcode2str(reason,Constants2berrcode)
        self.retmsg.msg = operationstr + reasonstr
        #add report
        event = mapzhphrase(operation, ReportHandoverphrase, pre="Failed to ", post=reasonstr)
        self.retmsg.report = constructReport(type=ReportType.PHONEEVENT_BASE, event=event, level=self.retmsg.msglevel)
        return self.retmsg

class imscmopfailed2(eventhandler):
    '''
    two pattern: operation, reason
    operationFailed: id = 1, type = "OPERATION_HANDOVER_TO_VOLTE", failed reason = VOLTE pdn failed
    '''
    def handler(self):
        self.retmsg.msglevel = Msglevel.ERROR
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        operation = str(self.match.group(2)).strip()
        reason = str(self.match.group(1)).strip()
        operationstr = operation + " Failed\n"
        reasonstr = "Reason: " + mapcode2str(reason,Constants2berrcode)
        self.retmsg.msg = operationstr + reasonstr
        #add report
        event = mapzhphrase(operation, ReportHandoverphrase, pre="Failed to ", post=reasonstr)
        self.retmsg.report = constructReport(type=ReportType.PHONEEVENT_BASE, event=event, level=self.retmsg.msglevel)
        return self.retmsg

class imscmopsuccessed(eventhandler):
    '''
    one pattern: operation
    '''
    def handler(self):
        self.retmsg.msglevel = Msglevel.NORMAL
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        operation = str(self.match.group(1)).strip()
        operationstr = operation + " Succeeded\n"
        self.retmsg.msg = operationstr
        #add report
        event = mapzhphrase(operation, ReportHandoverphrase, post=" Successfully")
        self.retmsg.report = constructReport(type=ReportType.PHONEEVENT_BASE, event=event, level=self.retmsg.msglevel)
        return self.retmsg

class imswaitvoltereg(eventhandler):
    def handler(self):
        self.retmsg.msglevel = Msglevel.ERROR
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        self.retmsg.msg = "After VoLte Call End\nWait for Volte to register\nBlock HO to VoWiFi"
        return self.retmsg

class imsrepeatvolte(eventhandler):
    def handler(self):
        self.retmsg.msglevel = Msglevel.WARNING
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        self.retmsg.msg = "VoLTE already registered\n Not HO to VoLTE"
        return self.retmsg

class imsrepeatvowifi(eventhandler):
    def handler(self):
        self.retmsg.msglevel = Msglevel.WARNING
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        self.retmsg.msg = "VoWiFi already registered\n Not HO to VoWiFi"
        return self.retmsg

class wpaselect(eventhandler):
    '''
    two patterns: wifi mac, ssid
    '''
    def handler(self):
        self.retmsg.msglevel = Msglevel.INFO
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        mac = str(self.match.group(1)).strip()
        ssid = str(self.match.group(2)).strip()
        ssidstr = "Select New WiFi AP: " + ssid + '\n'
        macstr = "AP Mac: " + mac
        self.retmsg.msg =  ssidstr + macstr
        event = mapzhphrase("wpaselect", ReportScenariophrase, post=ssid)
        self.retmsg.report = constructReport(type=ReportType.USEREVENT_BASE, event=event, level=self.retmsg.msglevel)
        return self.retmsg


class wpaconn(eventhandler):
    def handler(self):
        self.retmsg.msglevel = Msglevel.INFO
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        self.retmsg.msg = "Connected to WiFi AP"
        event = mapzhphrase("wpaconn", ReportScenariophrase)
        self.retmsg.report = constructReport(type=ReportType.USEREVENT_BASE, event=event, level=self.retmsg.msglevel)
        return self.retmsg

class dhcpdiscover(eventhandler):
    def handler(self):
        self.retmsg.msglevel = Msglevel.DEBUG
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        self.retmsg.msg = "DHCP Discover"
        return self.retmsg

class dhcpack(eventhandler):
    '''
    one pattern: dhcp ip
     DhcpClient: Received packet: 00:27:15:74:63:47 ACK: your new IP /10.1.63.66, netmask /255.255.252.0, gateway /10.1.60.1 DNS servers: /10.0.0.8 , lease time 600
    '''
    def handler(self):
        ip = str(self.match.group(1)).strip()
        self.retmsg.msglevel = Msglevel.INFO
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        self.retmsg.msg = "DHCP Get new IP: " + ip
        return self.retmsg


class pingfail(eventhandler):
    def handler(self):
        self.retmsg.msg = self.match.group(1)
        self.retmsg.msglevel = Msglevel.ERROR

        event=mapzhphrase("pingfail", ReportScenariophrase)
        self.retmsg.report = constructReport(type=ReportType.SCEEVENT_BASE, event=event, level=self.retmsg.msglevel)
        return self.retmsg

class pingmsg(eventhandler):
    '''
    two pattern:  ping times, pingstring
    pingCount = 0 this time ping www.bing.com success
    '''
    def handler(self):
        pingcount = str(int(self.match.group(1))+1).strip()
        pingstring = str(self.match.group(2)).strip()
        self.retmsg.msglevel = Msglevel.INFO
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        index = "th"
        if pingcount == "1":
            index = "st"
        elif pingcount == "2":
            index = "nd"
        elif pingcount == "3":
            index = "rd"
        self.retmsg.msg = pingcount + index + " Ping \n" + pingstring
        return self.retmsg

class ikeroaming(eventhandler):
    '''
    four pattern: roaming type, hplmn, vplmn, static address
    '''
    def handler(self):
        roamingtype = str(self.match.group(1)).strip()
        roamingtype = mapcode2str(roamingtype, Constantikeroaming)
        hplmn = str(self.match.group(2)).strip()
        vplmn = str(self.match.group(3)).strip()
        static = str(self.match.group(4)).strip()
        self.retmsg.msglevel = Msglevel.INFO
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        roamstr = "Roaming Type: " + roamingtype + '\n'
        hplmnstr = "HPLMN: " + hplmn + '\n'
        vplmnstr = "VPLMN: " + vplmn + '\n'
        staticstr = "Static FQDN: " + static
        self.retmsg.msg = roamstr + hplmnstr + vplmnstr + staticstr
        return self.retmsg

class networktype(eventhandler):
    def handler(self):
        self.retmsg.msglevel = Msglevel.DEBUG
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        networktype = str(self.match.group(1)).strip()
        networktype = mapcode2str(networktype, ConstantNetworkType)
        self.retmsg.msg = "Network Type: " + networktype
        return self.retmsg

class srvcclogout(eventhandler):
    def handler(self):
        self.retmsg.msglevel = Msglevel.INFO
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        self.retmsg.msg = "logout after SRVCC"
        return self.retmsg

class teleaction(eventhandler):
    def handler(self):
        self.retmsg.msglevel = Msglevel.INFO
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        msgtype = str(self.match.group(1)).strip()
        msgtype = mapcode2str(msgtype, Constanttelemsg)
        self.retmsg.msg = msgtype
        return self.retmsg

class adddrerror(eventhandler):
    def handler(self):
        self.retmsg.msglevel = Msglevel.ERROR
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)

        drerror = "Failed to update the data router state"
        self.retmsg.msg = drerror
        event = mapzhphrase("adddrerror", ReportScenariophrase)
        self.retmsg.report = constructReport(type=ReportType.SCEEVENT_BASE, event=event, level=self.retmsg.msglevel)
        return self.retmsg

class regstatewrongcallfail(eventhandler):
    def handler(self):
        self.retmsg.msglevel = Msglevel.ERROR
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        self.retmsg.msg = "VoWiFi not Registered.\nEnd Call!"
        event=mapzhphrase("unregcallfail", ReportScenariophrase)
        self.retmsg.report = constructReport(type=ReportType.SCEEVENT_BASE, event=event, level=self.retmsg.msglevel)
        return self.retmsg

class sendsms(eventhandler):
    '''
    retry times , messageref, smsmsg
    '''
    def handler(self):
        self.retmsg.msglevel = Msglevel.INFO
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        retry = str(self.match.group(1)).strip()
        #idstr = "messageRef: " + str(self.match.group(2)).strip() + '\n'
        smsmsg = str(self.match.group(2)).strip()
        retrystr = ""
        if int(retry) >= 1:
            retrystr = "Retry: " + retry + " times"
        self.retmsg.msg = "Send Sms: " + smsmsg + '\n' + retrystr
        event=mapzhphrase("sendsms", ReportScenariophrase)
        self.retmsg.report = constructReport(type=ReportType.SCEEVENT_BASE, event=event, level=self.retmsg.msglevel)
        return self.retmsg


class smspair(eventhandler):
    '''
    messageref, id
    '''
    def handler(self):
        self.retmsg.msglevel = Msglevel.INFO
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        messageRefstr = "messageRef: " + str(self.match.group(1)).strip() + '\n'
        idstr = "ID: " + str(self.match.group(2)).strip() + '\n'
        self.retmsg.msg = messageRefstr + idstr
        return self.retmsg

class sendsmsok(eventhandler):
    '''
    id, smstype
    '''
    def handler(self):
        self.retmsg.msglevel = Msglevel.NORMAL
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        idstr = "ID: " + str(self.match.group(1)).strip() + '\n'
        smstype = str(self.match.group(2)).strip()
        smstype = mapcode2str(smstype, ConstantSmsType)
        smsstr = "Sms Type: " +  smstype + '\n'
        self.retmsg.msg = "Send Sms OK\n" + idstr + smsstr

        event=mapzhphrase("sendsmsok", ReportScenariophrase, post=smstype)
        self.retmsg.report = constructReport(type=ReportType.SCEEVENT_BASE, event=event, level=self.retmsg.msglevel)
        return self.retmsg

class sendsmsok2(eventhandler):
    '''
    msgref
    '''
    def handler(self):
        self.retmsg.msglevel = Msglevel.NORMAL
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        msgrefstr = "messageRef: " + str(self.match.group(1)).strip() + '\n'
        self.retmsg.msg = "Send Sms OK\n" + msgrefstr
        return self.retmsg

class sendsmsfailed(eventhandler):
    '''
    messageRef, smstype, errorcode
    '''
    def handler(self):
        self.retmsg.msglevel = Msglevel.ERROR
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        idstr = "ID: " + str(self.match.group(1)).strip() + '\n'
        smstype = str(self.match.group(2)).strip()
        smstype = mapcode2str(smstype, ConstantSmsType)
        smsstr = "Sms Type: " +  smstype + '\n'
        error = str(self.match.group(3)).strip()
        errorstr = "Error State: " + error+ '-->' + mapcode2str(error, ConstantImmsg)
        event=mapzhphrase("sendsmsfailed", ReportScenariophrase, post=smstype)
        self.retmsg.report = constructReport(type=ReportType.SCEEVENT_BASE, event=event, level=self.retmsg.msglevel)
        self.retmsg.msg = "Send Sms Failed!\n" + idstr + smsstr + errorstr
        return self.retmsg

class smstimeout(eventhandler):
    def handler(self):
        self.retmsg.msglevel = Msglevel.ERROR
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        messageRefstr = "messageRef: " + str(self.match.group(1)).strip() + '\n'
        self.retmsg.msg = "Send Sms timeout!\n" + messageRefstr
        event=mapzhphrase("sendsmstimeout", ReportScenariophrase)
        self.retmsg.report = constructReport(type=ReportType.SCEEVENT_BASE, event=event, level=self.retmsg.msglevel)
        return self.retmsg

class recvsms(eventhandler):
    def handler(self):
        self.retmsg.msglevel = Msglevel.INFO
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        idstr = "ID: " + str(self.match.group(1)).strip() + '\n'
        self.retmsg.msg = "Receive Sms \n" + idstr
        event=mapzhphrase("recvsms", ReportScenariophrase)
        self.retmsg.report = constructReport(type=ReportType.SCEEVENT_BASE, event=event, level=self.retmsg.msglevel)
        return self.retmsg

class recvsms2(eventhandler):
    def handler(self):
        self.retmsg.msglevel = Msglevel.INFO
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        msgrefstr = "messageRef: " + str(self.match.group(1)).strip() + '\n'
        self.retmsg.msg = "Receive Sms \n" + msgrefstr
        return self.retmsg

class smsack(eventhandler):
    def handler(self):
        self.retmsg.msglevel = Msglevel.INFO
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        msgrefstr = "messageRef: " + str(self.match.group(1)).strip() + '\n'
        self.retmsg.msg = "Send Sms ACK\n" + msgrefstr
        event=mapzhphrase("sendsmsack", ReportScenariophrase)
        self.retmsg.report = constructReport(type=ReportType.SCEEVENT_BASE, event=event, level=self.retmsg.msglevel)
        return self.retmsg

class cpmediaset(eventhandler):
    def handler(self):
        self.retmsg.msglevel = Msglevel.INFO
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        atcmd = str(self.match.group(1)).strip()
        #format is operation, channel_id, state, enable_ipv6
        fields = atcmd.split(',')
        op = str(fields[0])
        cid = str(fields[1])
        state = str(fields[2])
        opstr = "Media Operation: "
        if op == '1':
            opstr += 'Start'
        elif op == '2':
            opstr += 'Stop'
        elif op == '3':
            opstr += 'Change'

        cidstr = "Channel id: " + cid
        statestr = "Media Direct: "
        if state == '0':
            statestr += "none"
        elif state == '1':
            statestr += 'recvonly'
        elif state == '2':
            statestr += 'sendonly'
        elif state == '3':
            statestr += 'sendrecv'

        msg = "CP Media AT CMD"
        self.retmsg.msg = msg + '\n' + cidstr + '\n' + opstr + '\n' + statestr

        return self.retmsg

class nonceerror(eventhandler):
    def handler(self):
        self.retmsg.msglevel = Msglevel.ERROR
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        self.retmsg.msg = "Auth Nonce is null"
        event=mapzhphrase("nonceerror", ReportScenariophrase)
        self.retmsg.report = constructReport(type=ReportType.SCEEVENT_BASE, event=event, level=self.retmsg.msglevel)
        return self.retmsg

class akaerror(eventhandler):
    def handler(self):
        self.retmsg.msglevel = Msglevel.ERROR
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        self.retmsg.msg = str(self.match.group(1)).strip()
        event=mapzhphrase("akaerror", ReportScenariophrase)
        self.retmsg.report = constructReport(type=ReportType.SCEEVENT_BASE, event=event, level=self.retmsg.msglevel)
        return self.retmsg

class notmeetpolicy(eventhandler):
    def handler(self):
        self.retmsg.msglevel = Msglevel.WARNING
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        wfc = str(self.match.group(1)).strip()
        wifi = str(self.match.group(2)).strip()
        lte = str(self.match.group(3)).strip()
        if wfc == "true":
            wfcstr = "Enabled"
        else:
            wfcstr = "Disabled"
        if wifi == "true":
            wifistr = "Connected"
        else:
            wifistr = "Disconnected"

        msgstr = "ImsCM Policy Not started:\n"
        msgstr += "WiFi-Calling: " + wfcstr + '\n'
        msgstr += "WiFi:" + wifistr + '\n'
        msgstr += "LTE Network: " + lte
        self.retmsg.msg = msgstr
        return self.retmsg

class notmeetpolicy2(eventhandler):
    def handler(self):
        task = str(self.match.group(1)).strip()
        self.retmsg.msglevel = Msglevel.WARNING
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        msgstr = "ImsCM Release Task: " + task + '\n'
        msgstr += "Due to condition not satisfied."
        self.retmsg.msg = msgstr
        return self.retmsg

class notask(eventhandler):
    def handler(self):
        self.retmsg.msglevel = Msglevel.WARNING
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        self.retmsg.msg = "2G/3G Network, Do not camp on volte"
        return self.retmsg

class hosignal(eventhandler):
    def handler(self):
        self.retmsg.msglevel = Msglevel.INFO
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        rssi = str(self.match.group(1)).strip()
        rsrp = str(self.match.group(2)).strip()
        msg = "WIFI Rssi: " + rssi + '\n'
        msg += "LTE Rsrp: " + rsrp
        self.retmsg.msg = msg
        return self.retmsg

class cmregstat(eventhandler):
    def handler(self):
        self.retmsg.msglevel = Msglevel.WARNING
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        imsfeature = str(self.match.group(1)).strip()
        regstate = str(self.match.group(2)).strip()
        msg = "IMS Feature: " + imsfeature + '\n'
        msg += "VOLTE Regstate: " + regstate
        self.retmsg.msg = msg
        return self.retmsg

class audioqos(eventhandler):
    def handler(self):
        self.retmsg.msglevel = Msglevel.INFO
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        loss = str(self.match.group(1)).strip()
        jitter = str(self.match.group(2)).strip()
        rtt = str(self.match.group(3)).strip()
        msg = "Audio Loss: " + loss + '\n'
        msg += "Audio Jitter: " + jitter + '\n'
        msg+= "Audio Rtt: " + rtt
        self.retmsg.msg = msg
        return self.retmsg

class audioqosinvideo(eventhandler):
    def handler(self):
        self.retmsg.msglevel = Msglevel.INFO
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        loss = str(self.match.group(1)).strip()
        jitter = str(self.match.group(2)).strip()
        rtt = str(self.match.group(3)).strip()
        msg = "Audio Loss: " + loss + '\n'
        msg += "Audio Jitter: " + jitter + '\n'
        msg+= "Audio Rtt: " + rtt
        self.retmsg.msg = msg
        return self.retmsg


class videoqosinvideo(eventhandler):
    def handler(self):
        self.retmsg.msglevel = Msglevel.INFO
        self.retmsg.color = maplevel2color(self.retmsg.msglevel)
        loss = str(self.match.group(1)).strip()
        jitter = str(self.match.group(2)).strip()
        rtt = str(self.match.group(3)).strip()
        msg = "Video Loss: " + loss + '\n'
        msg += "Video Jitter: " + jitter + '\n'
        msg+= "Video Rtt: " + rtt
        self.retmsg.msg = msg
        return self.retmsg



if __name__ == '__main__':
    key = 'abc'
    line = "abc"
    pattern = re.compile(key)
    match = pattern.search(line)
    color = "black"

    demohandler =  demoinherit(match, "black", 1)

    mprofile ="{ audioQuality=2, audioDirection=3, videoQuality=1, videoDirection=3 }"
    print parsemprofile(mprofile)
    print demohandler.getret()
