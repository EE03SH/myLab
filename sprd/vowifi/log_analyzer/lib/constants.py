#-*- coding=utf-8 -*-
#author: zhihua.ye@spreadtrum.com

Q850map = dict()

Q850map['1'] = dict()
Q850map['1']['isdn'] = "unallocated number"
Q850map['1']['sip'] = "404 Not found"

Q850map['2'] = dict()
Q850map['2']['isdn'] = "no route to network"
Q850map['2']['sip'] = "404 Not found"

Q850map['3'] = dict()
Q850map['3']['isdn'] = "no route to destination"
Q850map['3']['sip'] = "404 Not found"

Q850map['6'] = dict()
Q850map['6']['isdn'] = "CHANNEL_UNACCEPTABLE"
Q850map['6']['sip'] = ""

Q850map['7'] = dict()
Q850map['7']['isdn'] = "CALL_AWARDED_DELIVERED"
Q850map['7']['sip'] = ""

Q850map['16'] = dict()
Q850map['16']['isdn'] = "NORMAL_CLEARING"
Q850map['16']['sip'] = ""

Q850map['17'] = dict()
Q850map['17']['isdn'] = "17 user busy"
Q850map['17']['sip'] = "486 Busy here"

Q850map['18'] = dict()
Q850map['18']['isdn'] = "no user responding"
Q850map['18']['sip'] = "408 Request Timeout"

Q850map['19'] = dict()
Q850map['19']['isdn'] = "no answer from the user"
Q850map['19']['sip'] = "480 Temporarily unavailable"

Q850map['20'] = dict()
Q850map['20']['isdn'] = "subscriber absent"
Q850map['20']['sip'] = "480 Temporarily unavailable"

Q850map['21'] = dict()
Q850map['21']['isdn'] = "call rejected"
Q850map['21']['sip'] = "603 Decline"


Q850map['22'] = dict()
Q850map['22']['isdn'] = "number changed"
Q850map['22']['sip'] = "410 Gone"

Q850map['23'] = dict()
Q850map['23']['isdn'] = "redirection to new destination"
Q850map['23']['sip'] = "410 Gone"


Q850map['25'] = dict()
Q850map['25']['isdn'] = "EXCHANGE_ROUTING_ERROR"
Q850map['25']['sip'] = "483 Too Many Hops"

Q850map['26'] = dict()
Q850map['26']['isdn'] = "non-selected user clearing"
Q850map['26']['sip'] = "404 Not Found"

Q850map['27'] = dict()
Q850map['27']['isdn'] = "destination out of order"
Q850map['27']['sip'] = "502 Bad Gateway"

Q850map['28'] = dict()
Q850map['28']['isdn'] = "address incomplete"
Q850map['28']['sip'] = "484 Address incomplete"

Q850map['29'] = dict()
Q850map['29']['isdn'] = "facility rejected"
Q850map['29']['sip'] = "501 Not implemented"

Q850map['30'] = dict()
Q850map['30']['isdn'] = "RESPONSE_TO_STATUS_ENQUIRY"
Q850map['30']['sip'] = ""

Q850map['31'] = dict()
Q850map['31']['isdn'] = "normal unspecified"
Q850map['31']['sip'] = "480 Temporarily unavailable"

Q850map['34'] = dict()
Q850map['34']['isdn'] = "no circuit available"
Q850map['34']['sip'] = "503 Service unavailable"

Q850map['38'] = dict()
Q850map['38']['isdn'] = "network out of order"
Q850map['38']['sip'] = "503 Service unavailable"

Q850map['41'] = dict()
Q850map['41']['isdn'] = "temporary failure"
Q850map['41']['sip'] = "503 Service unavailable"

Q850map['42'] = dict()
Q850map['42']['isdn'] = "switching equipment congestion"
Q850map['42']['sip'] = "503 Service unavailable"

Q850map['43'] = dict()
Q850map['43']['isdn'] = "ACCESS_INFO_DISCARDED"
Q850map['43']['sip'] = ""

Q850map['44'] = dict()
Q850map['44']['isdn'] = "REQUESTED_CHAN_UNAVAIL"
Q850map['44']['sip'] = "503 Service unavailable"

Q850map['45'] = dict()
Q850map['45']['isdn'] = "PRE_EMPTED"
Q850map['45']['sip'] = ""

Q850map['47'] = dict()
Q850map['47']['isdn'] = "resource unavailable"
Q850map['47']['sip'] = "503 Service unavailable"

Q850map['50'] = dict()
Q850map['50']['isdn'] = "FACILITY_NOT_SUBSCRIBED"
Q850map['50']['sip'] = ""

Q850map['52'] = dict()
Q850map['52']['isdn'] = "OUTGOING_CALL_BARRED"
Q850map['52']['sip'] = "403 Forbidden"


Q850map['54'] = dict()
Q850map['54']['isdn'] = "incoming calls barred"
Q850map['54']['sip'] = "403 Forbidden"

Q850map['57'] = dict()
Q850map['57']['isdn'] = "bearer capability not authorized"
Q850map['57']['sip'] = "403 Forbidden"

Q850map['58'] = dict()
Q850map['58']['isdn'] = "BEARERCAPABILITY_NOTAVAIL"
Q850map['58']['sip'] = "503 Service unavailable"

Q850map['65'] = dict()
Q850map['65']['isdn'] = "BEARERCAPABILITY_NOTIMPL"
Q850map['65']['sip'] = "488 Not Acceptable Here"

Q850map['66'] = dict()
Q850map['66']['isdn'] = "CHAN_NOT_IMPLEMENTED"
Q850map['66']['sip'] = ""

Q850map['69'] = dict()
Q850map['69']['isdn'] = "FACILITY_NOT_IMPLEMENTED"
Q850map['69']['sip'] = "501 Not implemented"

Q850map['70'] = dict()
Q850map['70']['isdn'] = "only restricted digital available"
Q850map['70']['sip'] = "488 Not Acceptable Here"

Q850map['79'] = dict()
Q850map['79']['isdn'] = "SERVICE_NOT_IMPLEMENTED"
Q850map['79']['sip'] = "501 Not implemented"


Q850map['81'] = dict()
Q850map['81']['isdn'] = "INVALID_CALL_REFERENCE"
Q850map['81']['sip'] = ""

Q850map['87'] = dict()
Q850map['87']['isdn'] = "user not member of CUG"
Q850map['87']['sip'] = "403 Forbidden"

Q850map['88'] = dict()
Q850map['88']['isdn'] = "incompatible destination"
Q850map['88']['sip'] = "503 Service unavailable"

Q850map['95'] = dict()
Q850map['95']['isdn'] = "INVALID_MSG_UNSPECIFIED"
Q850map['95']['sip'] = ""

Q850map['96'] = dict()
Q850map['96']['isdn'] = "MANDATORY_IE_MISSING"
Q850map['96']['sip'] = ""

Q850map['97'] = dict()
Q850map['97']['isdn'] = "MESSAGE_TYPE_NONEXIST"
Q850map['97']['sip'] = ""

Q850map['98'] = dict()
Q850map['98']['isdn'] = "WRONG_MESSAGE"
Q850map['98']['sip'] = ""

Q850map['100'] = dict()
Q850map['100']['isdn'] = "INVALID_IE_CONTENTS"
Q850map['100']['sip'] = ""

Q850map['101'] = dict()
Q850map['101']['isdn'] = "WRONG_CALL_STATE"
Q850map['101']['sip'] = ""

Q850map['103'] = dict()
Q850map['103']['isdn'] = "MANDATORY_IE_LENGTH_ERROR"
Q850map['103']['sip'] = ""

Q850map['102'] = dict()
Q850map['102']['isdn'] = "recovery of timer expiry"
Q850map['102']['sip'] = "504 Gateway timeout"

Q850map['111'] = dict()
Q850map['111']['isdn'] = "protocol error"
Q850map['111']['sip'] = "500 Server internal error"


Q850map['127'] = dict()
Q850map['127']['isdn'] = "inter-working unspecified"
Q850map['127']['sip'] = "500 Server internal error"


Q850map['487'] = dict()
Q850map['487']['isdn'] = "ORIGINATOR_CANCEL"
Q850map['487']['sip'] = "487 Request Terminated"

Q850map['500'] = dict()
Q850map['500']['isdn'] = "CRASH"
Q850map['500']['sip'] = ""

Q850map['501'] = dict()
Q850map['501']['isdn'] = "SYSTEM_SHUTDOWN"
Q850map['501']['sip'] = ""

Q850map['502'] = dict()
Q850map['502']['isdn'] = "LOSE_RACE"
Q850map['502']['sip'] = ""

Q850map['503'] = dict()
Q850map['503']['isdn'] = "MANAGER_REQUEST"
Q850map['503']['sip'] = ""

Q850map['600'] = dict()
Q850map['600']['isdn'] = "BLIND_TRANSFER"
Q850map['600']['sip'] = ""

Q850map['601'] = dict()
Q850map['601']['isdn'] = "ATTENDED_TRANSFER"
Q850map['601']['sip'] = ""


Q850map['602'] = dict()
Q850map['602']['isdn'] = "ALLOTTED_TIMEOUT"
Q850map['602']['sip'] = ""


Q850map['603'] = dict()
Q850map['603']['isdn'] = "USER_CHALLENGE"
Q850map['603']['sip'] = ""

Q850map['604'] = dict()
Q850map['604']['isdn'] = "MEDIA_TIMEOUT"
Q850map['604']['sip'] = ""

Q850map['605'] = dict()
Q850map['605']['isdn'] = "PICKED_OFF"
Q850map['605']['sip'] = ""


Q850map['606'] = dict()
Q850map['606']['isdn'] = "USER_NOT_REGISTERED"
Q850map['606']['sip'] = ""


Q850map['607'] = dict()
Q850map['607']['isdn'] = "PROGRESS_TIMEOUT"
Q850map['607']['sip'] = ""

Q850map['609'] = dict()
Q850map['609']['isdn'] = "GATEWAY_DOWN"
Q850map['609']['sip'] = ""


def getQ850isdn(cause):
    if cause in Q850map:
        if 'isdn' in Q850map[cause]:
            return Q850map[cause]['isdn']
    else:
        return cause

#ike notify error type
ikenotifyerror = [
"UNSUPPORTED_CRITICAL_PAYLOAD",
"INVALID_IKE_SPI",
"INVALID_MAJOR_VERSION",
"INVALID_SYNTAX",
"INVALID_MESSAGE_ID",
"INVALID_SPI",
"NO_PROPOSAL_CHOSEN",
"INVALID_KE_PAYLOAD",
"AUTHENTICATION_FAILED",
"SINGLE_PAIR_REQUIRED",
"NO_ADDITIONAL_SAS",
"INTERNAL_ADDRESS_FAILURE",
"FAILED_CP_REQUIRED",
"TS_UNACCEPTABLE",
"INVALID_SELECTORS",
"UNACCEPTABLE_ADDRESSES",
"TEMPORARY_FAILURE",
"CHILD_SA_NOT_FOUND",
#"INITIAL_CONTACT",
#"SET_WINDOW_SIZE",
#"ADDITIONAL_TS_POSSIBLE",
#"IPCOMP_SUPPORTED",
#"NAT_DETECTION_SOURCE_IP",
#"NAT_DETECTION_DESTINATION_IP",
#"COOKIE",
#"USE_TRANSPORT_MODE",
#"HTTP_CERT_LOOKUP_SUPPORTED",
#"REKEY_SA",
#"ESP_TFC_PADDING_NOT_SUPPORTED",
#"NON_FIRST_FRAGMENTS_ALSO",
#"MOBIKE_SUPPORT",
#"NO_ADDITIONAL_ADDRESSES",
#"UPDATE_SA_ADDRESSES",
#"COOKIE2",
#"AUTH_LIFETIME",
#"MULTIPLE_AUTH_SUPPORTED",
#"EAP_ONLY_AUTHENTICATION"
]

mypayloadtype = [
    "Security Assocoation (33)",
    "Key Exchange (34)",
    "Traffic Selector - Initiator (44)",
    "Traffic Selector - Responder (45)",
    "Extensible Authentication (48)",
    "Encrypted and Authenticated (46)",
    "Authentication (39)",
    "Notify (41)",
    "Nonce (40)",
    "Nonce",
    "Configuration",
    "Delete (42)"
]


#bug 580143, MT_Call_Deattach can be a good example

from eventhandler import *
#CAUSTION: the name must be same as the java tag, example listed below:
#private static final String TAG = "[ImsCM] "
module_UE="UE"

module_Phone="Phone"
module_Ims="Ims"
module_ImsCM="ImsCM"
module_Adapter="Adapter"

module_Service="Service"
module_Security="Security"
#module_Lemon="Sip Stack"
module_CP="CP"
module_dialer="Dialer"
module_CallCardPresenter="CallCardPresenter"
module_CallButtonPresenter="CallButtonPresenter"
module_systemserver="systemserver"
module_wpasupplicant="wpasupplicant"

class eventType():
    SEPERATOR = 1 #seperator line
    SELFREF = 2   #self reference edge
    EDGE = 3      # normal edge


class eventObj():
    def __init__(self):
        self.array = list()
        #define subprocess, list of string
        self.subprocess = list()
        self.name = ''

    def addEvent(self, key, module, eventType = eventType.SEPERATOR, eventHandler = matchone, color= "black", groupnum=0, display=True):
        event = dict()
        event['key'] = key
        event['module'] = module
        event['eventType'] = eventType
        event['eventHandler'] = eventHandler
        event['color'] = color
        event['groupnum'] = groupnum
        event['display'] = display

        self.array.append(event)

    def getarray(self):
        return self.array

    def getsubprocess(self):
        return self.subprocess

    def addWholeEvent(self, event):
        self.array.append(event)

    def addsubprocess(self,process):
        self.subprocess.append(process)

    def setName(self,name):
        self.name = name

    def getName(self):
        return self.name

class searchType():
    WORDINLINE = 0
    TAGMATCH = 1
    TAGPARTIALMATCH = 2



class newSubproc():
    def __init__(self, key='key', search=None):
        self.subproc = dict()
        self.subproc['key'] = key
        self.subproc['search'] = search

    def getsubproc(self):
        return self.subproc

    def getKey(self):
        return self.subproc['key']

    def getSearch(self):
        return self.subproc['search']

def wordInline(word, line):
    if word in line:
        return True
    else:
        return False

import re
def tagInline(word, lineinfo, field,partial=False):
    tag = lineinfo[field]
    if partial == True:
        regex = re.compile(r"^" + word)
        if regex.match(tag):
            return True
        else:
            return False
    else:
        if word == tag:
            return True
        else:
            return False


dialerEvent = eventObj()
dialerEvent.setName(module_dialer)
cbpsearch = dict()
cbpsearch['type'] = searchType.TAGMATCH
#03-30 21:46:40.263  1638  1638 I InCall  : CallCardPresenter
cbpsearch['field'] = 7
CallButtonPresentersubproc = newSubproc(key=module_CallButtonPresenter, search=cbpsearch)

ccpsearch = dict()
ccpsearch['type'] = searchType.TAGMATCH
#03-30 21:46:40.263  1638  1638 I InCall  : CallCardPresenter
ccpsearch['field'] = 7
CallCardPresentersubproc = newSubproc(key=module_CallCardPresenter, search=ccpsearch)

dialerEvent.addsubprocess(CallButtonPresentersubproc)
dialerEvent.addsubprocess(CallCardPresentersubproc)

imscmEvent = eventObj()
imscmEvent.setName(module_ImsCM)

phoneEvent = eventObj()
imssearch = dict()
imssearch['type'] = searchType.WORDINLINE
#03-30 21:46:40.380   927   927 D [ImsCM] ImsConnectionManagerService:
imssearch['field'] = None
imscmsubproc = newSubproc(key='[ImsCM]', search=imssearch)
phoneEvent.addsubprocess(imscmsubproc)

adaptersearch = dict()
adaptersearch['type'] = searchType.WORDINLINE
adaptersearch['field'] = None
adaptersubproc = newSubproc(key='[Adapter]', search=adaptersearch)
phoneEvent.addsubprocess(adaptersubproc)

imssearch = dict()
imssearch['type'] = searchType.TAGPARTIALMATCH
#03-30 21:43:48.030   927   927 D ImsRegister: [ImsRegister0]
imssearch['field'] = 5
imssubproc = newSubproc(key=module_Ims, search=imssearch)
phoneEvent.addsubprocess(imssubproc)
phoneEvent.setName(module_Phone)

securityEvent = eventObj()
securityEvent.setName(module_Security)
serviceEvent = eventObj()
serviceEvent.setName(module_Service)
systemserverEvent = eventObj()
systemserverEvent.setName(module_systemserver)
wpaEvent = eventObj()
wpaEvent.setName(module_wpasupplicant)


processmap = dict()
processmap['com.sprd.ImsConnectionManager'] = imscmEvent
processmap['com.android.phone'] = phoneEvent
processmap['com.android.dialer'] = dialerEvent
processmap['com.sprd.vowifi.security'] = securityEvent
processmap['com.spreadtrum.vowifi'] = serviceEvent
processmap['system_server'] = systemserverEvent
processmap['wpa_supplicant'] = wpaEvent


#we should add sub-process handler



#dialer part
### hold
#FIXME: later should add more phrase to indicate


#hold
dialerEvent.addEvent("(Putting the call on hold)", module_CallButtonPresenter, eventType = eventType.EDGE)
# resume
dialerEvent.addEvent("(Removing the call from hold)", module_CallButtonPresenter, eventType = eventType.EDGE)
#mute
dialerEvent.addEvent("CallButtonPresenter - turning on mute: (.*)", module_CallButtonPresenter, eventType=eventType.EDGE, eventHandler=turnmute)

dialerEvent.addEvent("(Swapping the call)", module_CallButtonPresenter, eventType = eventType.EDGE)

dialerEvent.addEvent("(switchCameraClicked - useFrontFacingCamera)", module_CallButtonPresenter, eventType = eventType.EDGE)

#TODO: add more default about the call info
dialerEvent.addEvent("(Disconnecting call):.*Call_(\d+), (.*), \[Capabilities", module_CallCardPresenter, groupnum=3,eventType = eventType.EDGE , eventHandler=callcard, display=True)
dialerEvent.addEvent("(Swapping call to foreground):.*Call_(\d+), (.*), \[Capabilities", module_CallCardPresenter, groupnum=3, eventType = eventType.EDGE,eventHandler=callcard, display=True)

dialerEvent.addEvent("(Primary call):.*Call_(\d+), (.*), \[Capabilities", module_CallCardPresenter, groupnum=3, eventType = eventType.EDGE,eventHandler=callcard, display=False)
dialerEvent.addEvent("(Secondary call):.*Call_(\d+), (.*), \[Capabilities", module_CallCardPresenter, groupnum=3, eventType = eventType.EDGE,eventHandler=callcard, display=False)




#------------------------------------------------------------------------------------
#ImsCM part
##ImsConnectionManagerMonitor
###start up wfc status
#imscmEvent.addEvent("(Wifi-calling is.*)", module_ImsCM)
###bind service
imscmEvent.addEvent("(\[bind.*)", module_ImsCM, eventType = eventType.EDGE)

imscmEvent.addEvent("(mPrimaryOperatorId value is invalid, please check)", module_ImsCM, eventType=eventType.EDGE, eventHandler=invalidSimCard)
#post-ping
##wifi connected
imscmEvent.addEvent('(wifi is connected)', module_ImsCM, eventType = eventType.EDGE, color="blue", eventHandler=wificonn)
#imscmEvent.addEvent("NetworkUtils: (Local IP address is:.*)", module_ImsCM)


##airplane open
imscmEvent.addEvent(': (.*pen airplane mode)', module_ImsCM , eventType = eventType.EDGE, color="blue", eventHandler=airon)
##airplaneclose
imscmEvent.addEvent(': (.*lose airplane mode)', module_ImsCM,eventType = eventType.EDGE, color="blue", eventHandler=airoff)
##receive INTENT ACTION_SHUTDOWN
imscmEvent.addEvent('(.*hut down device)', module_ImsCM,eventType = eventType.EDGE, color="red", eventHandler=poweroff)
##lte network


imscmEvent.addEvent('Lte network, networkType = (.*)', module_ImsCM, eventType = eventType.EDGE, eventHandler=networktype)

##wifi disconnected
imscmEvent.addEvent('(wifi is disconnected)', module_ImsCM, eventType = eventType.EDGE, color="blue", eventHandler=wifidisconn)
##wifi calling
imscmEvent.addEvent('database has changed, mIsWifiCallingEnabled = (.*)', module_ImsCM, eventType = eventType.EDGE, eventHandler=wfcstatus)
imscmEvent.addEvent('database has changed.*IsWfcEnabled = (.*),', module_ImsCM, eventType = eventType.EDGE, eventHandler=wfcstatus)

##default wifi calling
imscmEvent.addEvent('(Wifi-calling is .*)', module_ImsCM, eventType = eventType.EDGE, color = "blue")

imscmEvent.addEvent('Wifi-calling mode is \"(.*)\"', module_ImsCM, eventType = eventType.EDGE,  eventHandler=wfcmode)
### sim card only used in android 6
imscmEvent.addEvent("(turn off primary SIM card)", module_ImsCM,eventType = eventType.EDGE, color="red")
imscmEvent.addEvent("(turn on primary SIM card)", module_ImsCM,eventType = eventType.EDGE, color="red")

imscmEvent.addEvent("onWifiPreClose: mIsImsPdnDeactive = (\w+)", module_ImsCM, eventType = eventType.EDGE, eventHandler=wifipreclose)

##Utils
###switch to wifi
imscmEvent.addEvent("\[(Switch to Vowifi)\]", module_ImsCM, eventType = eventType.EDGE, color = "blue", eventHandler=idlehowifi)
###switch to volte
imscmEvent.addEvent("\[(Switch to Volte)\]", module_ImsCM, eventType = eventType.EDGE, color = "blue", eventHandler=idleholte)
###Handover to Vowifi
imscmEvent.addEvent("\[(Handover to Vowifi)\]", module_ImsCM, eventType = eventType.EDGE, color = "blue", eventHandler=callhowifi)
###Handover to Volte
imscmEvent.addEvent("\[(Handover to Volte)\]", module_ImsCM,  eventType = eventType.EDGE, color = "blue", eventHandler=callholte)
###Release Vowifi resource
imscmEvent.addEvent("\[(Release Vowifi resource)\]", module_ImsCM, eventType = eventType.EDGE)
###Set Vowifi unavailable
imscmEvent.addEvent("\[(Set Vowifi unavailable)\]", module_ImsCM, eventType = eventType.EDGE, color = "red")
###[Cancel current request]
imscmEvent.addEvent("\[(Cancel current request)\]", module_ImsCM)
###[hung up Vowifi call]
imscmEvent.addEvent("(hung up IMS call)", module_ImsCM, eventType=eventType.EDGE, color = "red", eventHandler=cmendcall)
###[popup Vowifi unavailable notification]
imscmEvent.addEvent("(popup Vowifi unavailable notification)", module_ImsCM, eventType=eventType.EDGE, color = "blue")


##ImsConnectionManagerMonitor.java
###init sim card, change sim card
#android 6.0 logic...
imscmEvent.addEvent(': (\w+) primary USIM card plmn = (\w+)' , module_ImsCM, eventType = eventType.EDGE, eventHandler=simstatus, groupnum=2)
#slot status
imscmEvent.addEvent('card (\d) status :(.*)' , module_ImsCM, eventType = eventType.EDGE, eventHandler=slotstatus, groupnum=2)



#TODO: android 7.0 logic need to be verified
#android 7.0 logic
#sim card plmn
imscmEvent.addEvent(': updateSubscriptionInfo: (\w+) primary USIM card plmn, mPrimaryPlmn = (\w+)' , module_ImsCM, eventType = eventType.EDGE, eventHandler=simstatus, groupnum=2)
imscmEvent.addEvent('getPrimaryPlmn: get primary PLMN from getSimOperatorNumericForPhone.*: (\d+)' , module_ImsCM, eventType = eventType.EDGE, eventHandler=newsimstatus)

#slot status
imscmEvent.addEvent('updateSimState: Slot (\d) status is (.*)' , module_ImsCM, eventType = eventType.EDGE, eventHandler=slotstatus, groupnum=2)
imscmEvent.addEvent('updateSimState: Slot (\d) simState = (.*)' , module_ImsCM, eventType = eventType.EDGE, eventHandler=slotstatus, groupnum=2)
#mDefaultDataSubscriptionObserver
imscmEvent.addEvent('(primary card id has changed)' , module_ImsCM, eventType = eventType.EDGE, eventHandler=simchanged7)


#ims task policy
imscmEvent.addEvent("createPolicyTimerTask: Conditions are not satisfied, don't create timer task, isWfcEnabled = (.*), isWifiConnected = (.*), isLteCellularNetwork = (.*)", module_ImsCM, eventType = eventType.EDGE, eventHandler=notmeetpolicy )
imscmEvent.addEvent("create.*Conditions are not satisfied, release \[(.*)\]", module_ImsCM, eventType = eventType.EDGE, eventHandler=notmeetpolicy2)
imscmEvent.addEvent("(don't create timer task during Vowifi and 2/3G or UNKNOWN network)", module_ImsCM, eventType = eventType.EDGE, eventHandler=notask)
imscmEvent.addEvent("wifi isConnected\(\): (.*)", module_ImsCM, eventType = eventType.EDGE, eventHandler=wificonn2 )

#pending logic
imscmEvent.addEvent('handleMessage.*: \"(.*)\", mCurPendingMsgId = \"(.*)\",' , module_ImsCM, eventType = eventType.EDGE, eventHandler=imscmpending)
imscmEvent.addEvent('handleMessage.*: \"(.*)\", mCurPendingProcessMsgId = (.*)' , module_ImsCM, eventType = eventType.EDGE, eventHandler=imscmpending)

#no need to add clearLoopMsgQueue
#no need to add ImsServiceListenerEx, all release action will be recorded.

#add regstate report
#ImsConnectionManagerService: [onVoLteServiceStateChanged], currentImsFeature = "VoWifi", cpRegState = "VOLTE INACTIVE"
imscmEvent.addEvent('currentImsFeature = \"(.*)\".*,.*cpRegState = \"(.*)\"' , module_ImsCM, eventType = eventType.EDGE, eventHandler=cmregstat, groupnum=2)

#add rssi
# ImsConnectionManagerEEPolicy: loopAudioCallQosForWifiPreferred: rssi = -86, rsrp = -103
imscmEvent.addEvent('rssi = (.*), rsrp = (.*)' , module_ImsCM, eventType = eventType.EDGE, eventHandler=hosignal, groupnum=2)
#add audio qos
imscmEvent.addEvent('loss = (.*), jitter = (.*), rtt = (.*)' , module_ImsCM, eventType = eventType.EDGE, eventHandler=audioqos, groupnum=3)
#add video qos
imscmEvent.addEvent('audioLoss = (.*), audioJitter = (.*), audioRtt = (.*)' , module_ImsCM, eventType = eventType.EDGE, eventHandler=audioqosinvideo, groupnum=3)
imscmEvent.addEvent('videoLoss = (.*), videoJitter = (.*), videoRtt = (.*)' , module_ImsCM, eventType = eventType.EDGE, eventHandler=videoqosinvideo, groupnum=3)
##audio/video qos and threshhold, vowifi call
imscmEvent.addEvent('loop(\w+)CallQos.*: Vowifi handover to Volte' , module_ImsCM, eventType = eventType.EDGE, eventHandler=qos2volte)


##audio/video rssi threshhold, volte call
imscmEvent.addEvent('loop(\w+)CallThreshold.*: Volte handover to (\w+)' , module_ImsCM, eventType = eventType.EDGE, eventHandler=callthreshholdho, groupnum=2)


##idle , reged than handover
imscmEvent.addEvent('loopProcessIdleThreshold.*: Volte switch to (\w+)' , module_ImsCM, eventType = eventType.EDGE, eventHandler=idlethreshholdho)

##idle non-reg attach
imscmEvent.addEvent('(loopProcessIdleThreshold.*: Auto attach Vowifi)' , module_ImsCM, eventType = eventType.EDGE, eventHandler=idleautovowifi)

#TOOD: add new log
#ImsConnectionManagerDefaultPolicy: loopIdleThresholdForCellularPreferred: Vowifi switch to Volte !!!!!
#loopIdleThresholdForWifiPreferred: Volte switch to Vowifi
imscmEvent.addEvent('loopIdleThreshold.*: Volte switch to (\w+)' , module_ImsCM, eventType = eventType.EDGE, eventHandler=idlethreshholdho)
imscmEvent.addEvent('loopIdleThreshold.*: Vowifi switch to (\w+)' , module_ImsCM, eventType = eventType.EDGE, eventHandler=idlethreshholdho)
##imscm error pattern
imscmEvent.addEvent(':.*\[(.*)\] error, mRequestId =' , module_ImsCM, eventType = eventType.EDGE, eventHandler=imscmhandlemsgerror)

#ImsConnectionManagerService: Rtp_handleMessage: "MSG_RECEIVE_NO_RTP", "Volte Call", "AUDIO CALL", isVideoPacket = false
imscmEvent.addEvent('handleMessage: \"MSG_RECEIVE_NO_RTP\", \"(.*)\", \"(.*)\", isVideoPacket = (.*)' , module_ImsCM, eventType = eventType.EDGE, eventHandler=imscmnortp2, groupnum=3)
## imscm no rtp received
imscmEvent.addEvent('handleMessage: \"MSG_RECEIVE_NO_RTP\", \"(.*)\", isVideoPacket = (.*)' , module_ImsCM, eventType = eventType.EDGE, eventHandler=imscmnortp, groupnum=2)

## imscm ping unreachable, seems no need to draw
imscmEvent.addEvent('(handleMessage: ping unreachable, must reset noAudioRtpCounter and noVideoRtpCounter)', module_ImsCM)
## ping ok, no audio/no video reach max counter
imscmEvent.addEvent('(handleMessage: .* meet max counter conditions, must reset noAudioRtpCounter and noVideoRtpCounter)', module_ImsCM)

## operation Successed
imscmEvent.addEvent('operationSuccessed: id = .*, type = "(.*)"', module_ImsCM, eventType = eventType.EDGE, eventHandler=imscmopsuccessed)

##error msg
###operation failed
#VoWifiRegisterManager report reg state
#VoWifiSecurityManager report s2b error code

imscmEvent.addEvent('operationFailed: id = .*, type = "(.*)", failed reason = (.*)', module_ImsCM, eventType = eventType.EDGE, eventHandler=imscmopfailed)
#code refatored
imscmEvent.addEvent('operationFailed: id = .*, failed reason = (.*), type = "(.*)"', module_ImsCM, eventType = eventType.EDGE, eventHandler=imscmopfailed2)

### switch vowifi error, not useful
'''
imscmEvent.addEvent('(switchOrHandoverVowifi: Device isn\'t in LTE environment)', module_ImsCM)
imscmEvent.addEvent('(switchOrHandoverVowifi: primary USIM card is disabled)', module_ImsCM)
imscmEvent.addEvent('(switchOrHandoverVowifi: error call mode and return this method, mCallMode =.*)', module_ImsCM)
imscmEvent.addEvent('(switchOrHandoverVowifi: invalid vowifi rssi)', module_ImsCM)
'''

### some ho exception
imscmEvent.addEvent('(Waiting for Volte registered.*Volte call end)', module_ImsCM, eventType = eventType.EDGE, eventHandler=imswaitvoltereg)
imscmEvent.addEvent('(Volte is registered, don\'t)', module_ImsCM, eventType = eventType.EDGE, eventHandler=imsrepeatvolte)
imscmEvent.addEvent('(Vowifi is registered, don\'t)', module_ImsCM, eventType = eventType.EDGE, eventHandler=imsrepeatvowifi)

#
##msg pending
# ImsConnectionManagerService: handleMessageHandoverToVowifi: mIsPendingProcess
#D:\code\log\bug_log\vit_log\2016_10_25\modem_log-0650-vowifiregisterfail-2



#------------------------------------------------------------------------------------

#phone imsservice logic
##vowifi/volte icon
phoneEvent.addEvent("updateImsFeatures->volteEnable:(.*) wifiEnable:(.*)", module_Ims, eventType=eventType.EDGE, eventHandler=geticon,groupnum=2)
##ims reg addr
phoneEvent.addEvent("setIMSRegAddress addr = (.*)", module_Ims, eventType=eventType.EDGE, eventHandler=setimsregaddr)
#get ims reg addr
phoneEvent.addEvent("getIMSRegAddress mImsRegAddress =(.*)", module_Ims, eventType=eventType.EDGE, eventHandler=getimsregaddr)
#get pcscf addr
phoneEvent.addEvent("getImsPcscfAddress mImsPscfAddress =(.*)", module_Ims, eventType=eventType.EDGE, eventHandler=getpcscfregaddr)

## start vowifi/volte call
phoneEvent.addEvent("createCallSession-> start(.*)", module_Ims, eventType=eventType.EDGE, eventHandler=startcall, color = "blue")

#some status event
phoneEvent.addEvent("EVENT_WIFI_ATTACH_FAILED-> mFeatureSwitchRequest:.* mAttachVowifiSuccess:.*", module_Ims, eventType=eventType.EDGE, eventHandler=telepdgfail)

phoneEvent.addEvent("EVENT_WIFI_ATTACH_SUCCESSED-> mFeatureSwitchRequest:(.*) mIsCalling:.*" , module_Ims, eventType=eventType.EDGE, eventHandler=telepdgsuccess)

phoneEvent.addEvent("ACTION_NOTIFY_VOWIFI_UNAVAILABLE->.* mIsCPImsPdnActived:(\w+)" , module_Ims, eventType=eventType.EDGE, eventHandler=telvowifiunavail)



phoneEvent.addEvent("Needn't switch to type (\d+) as it already registed", module_Ims, eventType=eventType.EDGE, eventHandler=switcherror)
#Adapter Part
##VoWifiSecurityManager

###update data router
##update datarouter
phoneEvent.addEvent('VoWifiCallManager: Update the call state to data router. state: (.*)', module_Adapter, eventType = eventType.EDGE, eventHandler=drstatus)
###s2b start
phoneEvent.addEvent("(Start the s2b attach.)",module_Adapter, eventType = eventType.EDGE)
###deattach
#phoneEvent.addEvent("(Try to de-attach, is handover:.*)", module_Phone)
###force stop
#phoneEvent.addEvent("(Force stop the s2b.)", module_Phone)
###s2b success
#phoneEvent.addEvent("(S2b attach success.)", module_Phone)
###s2b failed
#phoneEvent.addEvent("(S2b attach failed, errorCode:.*)", module_Phone)
###s2b state change
#phoneEvent.addEvent("(S2b attach progress state changed to.*)", module_Phone)
###s2b stop
#phoneEvent.addEvent("(S2b attach stopped, errorCode: .*)", module_Phone)
#------------------------------------------------------------------------------------
##VoWifiRegisterManager
###prepare login
phoneEvent.addEvent("(Prepare the info before login), subId is:.*", module_Adapter, eventType=eventType.EDGE)
###try to login
#phoneEvent.addEvent("(Try to login to the ims, current register state: .*)", module_Phone)
###Login info: ip, p-cscf
phoneEvent.addEvent("Login with the local ip: (.*), pcscf ip: (.*)", module_Adapter, eventType=eventType.EDGE, eventHandler=loginstatus, groupnum=2)
###logout
phoneEvent.addEvent("Try to logout from the ims, current register state: (.*)", module_Adapter, eventType=eventType.EDGE, eventHandler=logoutstatus)
###Re-register, do this in service
#phoneEvent.addEvent("(Re-register, with the type:.*)", module_Phone)
###force stop, no need to track
#phoneEvent.addEvent("(Stop current register process. registerState:.*)", module_Phone)

### security callback, this is old callback
phoneEvent.addEvent("Get the security callback:.*({\"security_json_action\":.*)", module_Adapter, eventType=eventType.EDGE, eventHandler=olds2bstatus)
phoneEvent.addEvent("Get the security callback:.*({.*})", module_Adapter, eventType=eventType.EDGE, eventHandler=news2bstatus)
### register callback
#in 4.4, json order is not the same as 6.0/7.0
#phoneEvent.addEvent("Get the register state changed callback: {\"event_code\":.*,\"event_name\":\"(.*)\",\"state_code\":(.*)}" , module_Adapter, eventType=eventType.EDGE, eventHandler=regstatus, groupnum=2)
phoneEvent.addEvent("Get the register state changed callback:.*({.*})" , module_Adapter, eventType=eventType.EDGE, eventHandler=regstatus)

###call related event
#phoneEvent.addEvent("(Handle the event.*for the call.*)", module_Phone)


###mute success, not come here
#phoneEvent.addEvent("Mutes\((.*)\)the mic for the active call", module_Phone, eventType=eventType.EDGE, eventHandler=mutestatus)
###mute failed, not come here
#phoneEvent.addEvent("(Native set mute failed)", module_Phone, eventType=eventType.EDGE, eventHandler=defaultfailed)



###start call, #important key words
phoneEvent.addEvent("Initiates an ims call with (.*)", module_Adapter, eventType=eventType.EDGE, eventHandler=makecallstatus)
###start failed
phoneEvent.addEvent("(Native start the call failed)", module_Adapter, eventType=eventType.EDGE, eventHandler=defaultfailed)

#FIXME: reg state is wrong.
phoneEvent.addEvent("ImsCallSessionImpl.*(Start the call failed. Check the callee or profile)", module_Adapter, eventType=eventType.EDGE, eventHandler=regstatewrongcallfail)


###one click start conf call
phoneEvent.addEvent("Initiates an ims conference call with participants: (.*)", module_Adapter, eventType=eventType.EDGE, eventHandler=oneclickconf)
###one click start failed
phoneEvent.addEvent("(Start the conference failed)", module_Adapter, eventType=eventType.EDGE, eventHandler=defaultfailed)

###accept
phoneEvent.addEvent("Accept an incoming call with call type is (.*)", module_Adapter, eventType=eventType.EDGE, eventHandler=acceptcall)
### lemon async send answer msg, so always right.
#phoneEvent.addEvent("(Native accept the incoming call failed)", module_Phone, eventType=eventType.EDGE, eventHandler=defaultfailed)

#seems Notify the event: {"event_code":105,"event_name":"call_terminate","id":3,"state_code":335}
#will conver most cases.
###reject
#phoneEvent.addEvent("Reject an incoming call as the reason is (.*)", module_Phone, eventType=eventType.EDGE, eventHandler=rejectcall)
#phoneEvent.addEvent("(Native reject the incoming call failed)", module_Phone, eventType=eventType.EDGE, eventHandler=defaultfailed)

###terminate
#phoneEvent.addEvent("Terminate a call as the reason is (.*)", module_Phone, eventType=eventType.EDGE, eventHandler=termcall)
#term failed will not come here, lemon async
#phoneEvent.addEvent("(Native terminate a call failed)", module_Phone, eventType=eventType.EDGE, eventHandler=defaultfailed)

###hold
phoneEvent.addEvent("Hold a call with the media profile: (.*)", module_Adapter, eventType=eventType.EDGE, eventHandler=holdcall)
#hold will not fail, lemon async
#phoneEvent.addEvent("(Native hold the call failed)", module_Phone, eventType=eventType.EDGE, eventHandler=defaultfailed)

###resume
phoneEvent.addEvent("Continues a call with the media profile: (.*)", module_Adapter, eventType=eventType.EDGE, eventHandler=resumecall)
#resume will not fail, lemon async
#phoneEvent.addEvent("(Native resume the call failed)", module_Phone, eventType=eventType.EDGE, eventHandler=defaultfailed)

###merge
phoneEvent.addEvent("(Merge the active & hold call)", module_Adapter, eventType=eventType.EDGE)

###update, seems not called
#phoneEvent.addEvent("(Update the current call's type to .*)", module_Phone)


###remove conf participants
phoneEvent.addEvent("Remove the participants: (.*)", module_Adapter, eventType=eventType.EDGE, eventHandler=removepart)
###send dtmf, #, * may also in
phoneEvent.addEvent("sendDtmf(\w)", module_Adapter,  eventType=eventType.EDGE, eventHandler=dtmf)
###start dtmf
phoneEvent.addEvent("startDtmf(\w)", module_Adapter,  eventType=eventType.EDGE, eventHandler=dtmf)
###send ussd
phoneEvent.addEvent("Send an USSD message: (.*)", module_Adapter, eventType=eventType.EDGE, eventHandler=ussd)

###start camera
phoneEvent.addEvent("ImsCallSessionImpl: Try to start the camera: (\w+) for the call: (\w+)", module_Adapter, eventType=eventType.EDGE, eventHandler=startcamera, groupnum=2)
#start failed
phoneEvent.addEvent("(Failed to start the camera as.*)",  module_Adapter, eventType=eventType.EDGE, color="red")

###stop camera
phoneEvent.addEvent("Try to stop the camera for the call: (\w+)", module_Adapter, eventType=eventType.EDGE, eventHandler=stopcamera)
#error handling
phoneEvent.addEvent("(Failed to stop the camera.)", module_Adapter, eventType=eventType.EDGE, color="red")

###start local render
phoneEvent.addEvent("Try to start the local render for the call: (\w+)", module_Adapter, eventType=eventType.EDGE, eventHandler=startlocalrender)
phoneEvent.addEvent("(Failed to start the local render.)", module_Adapter, eventType=eventType.EDGE, color="red")

###stop local render
phoneEvent.addEvent("Try to stop the local render for the call: (\w+)", module_Adapter, eventType=eventType.EDGE, eventHandler=stoplocalrender)
phoneEvent.addEvent("(Failed to stop the local render.)", module_Adapter, eventType=eventType.EDGE, color="red")

###start remote render
phoneEvent.addEvent("Try to start the remote render for the call: (\w+)", module_Adapter, eventType=eventType.EDGE, eventHandler=startremoterender)
phoneEvent.addEvent("(Failed to start the remote render.)", module_Adapter, eventType=eventType.EDGE, color="red")

### stop remote render
phoneEvent.addEvent("Try to stop the remote render for the call: (\w+)", module_Adapter, eventType=eventType.EDGE, eventHandler=stopremoterender)
phoneEvent.addEvent("(Failed to stop the remote render.)", module_Adapter, eventType=eventType.EDGE, color="red")

### start capture
phoneEvent.addEvent("Try to start capture for the call: (\w+), cameraId: (\w+), videoQuality index: (\w+)", module_Adapter,eventType=eventType.EDGE, eventHandler=startcapture, groupnum=3 )
phoneEvent.addEvent("(Failed to start capture.)", module_Adapter, eventType=eventType.EDGE, color="red")

### stop capture
phoneEvent.addEvent("Try to stop capture for the call: (\w+)", module_Adapter, eventType=eventType.EDGE, eventHandler=stopcapture )
phoneEvent.addEvent("(Failed to stop capture.)", module_Adapter, eventType=eventType.EDGE, color="red")

###start video trans
phoneEvent.addEvent("Try to start the video transmission for the call: (\w+)", module_Adapter, eventType=eventType.EDGE, eventHandler=startvideo)

phoneEvent.addEvent("Failed to start the video transmission for the call: (\w+)", module_Adapter, eventType=eventType.EDGE, eventHandler=startvideofailed)

### stop video trans
phoneEvent.addEvent("Try to stop the video transmission for the call: (\w+)", module_Adapter, eventType=eventType.EDGE, eventHandler=stopvideo)
phoneEvent.addEvent("Failed to stop the video transmission for the call: (\w+)", module_Adapter, eventType=eventType.EDGE, eventHandler=stopvideofailed)

###local rotate
phoneEvent.addEvent("Try to rotate local render for the call: (\w)", module_Adapter, eventType=eventType.EDGE, eventHandler=rotatelocalrender)
phoneEvent.addEvent("Failed to rotate local render for the call: (\w+)", module_Adapter, eventType=eventType.EDGE, eventHandler=rotatelocalrenderfailed)

### remote rotate
phoneEvent.addEvent("Try to rotate remote render for the call: (\w)", module_Adapter, eventType=eventType.EDGE, eventHandler=rotateremoterender)
phoneEvent.addEvent("Failed to rotate remote render for the call: (\w+)", module_Adapter, eventType=eventType.EDGE, eventHandler=rotateremoterenderfailed)

###modify request
phoneEvent.addEvent("Try to send the modify request, isVideo: (\w+)", module_Adapter, eventType=eventType.EDGE, eventHandler=modifyrequest)

phoneEvent.addEvent("(Failed to send the modify request) for the call", module_Adapter, eventType=eventType.EDGE, color="red", eventHandler=modifyrequestfailed)
###TODO: set pause image, not common function
phoneEvent.addEvent("Set the pause image to.*", module_Adapter)
###invite conf call
phoneEvent.addEvent("Try to invite this call(.*)to the conference call(.*)", module_Adapter, eventType=eventType.EDGE, eventHandler=invite2conf)

phoneEvent.addEvent("The handler get the message: (\d+)", module_Adapter, eventType=eventType.EDGE, eventHandler=teleaction, display=False)

#add SRVCC events
phoneEvent.addEvent("(Handle the SRVCC success as register logout now)", module_Adapter, eventType=eventType.EDGE, eventHandler=srvcclogout)
phoneEvent.addEvent("(handle the SRVCC start event)", module_Adapter, eventType=eventType.EDGE)
phoneEvent.addEvent("(handle the SRVCC success event)", module_Adapter, eventType=eventType.EDGE)
phoneEvent.addEvent("(handle the SRVCC failed/cancel event)", module_Adapter, eventType=eventType.EDGE, color="red")
phoneEvent.addEvent("(Try to release the call)", module_Adapter, eventType=eventType.EDGE, color="blue")
#some error in adapter
phoneEvent.addEvent("(Failed to update the data router state, please check)", module_Adapter,eventType=eventType.EDGE, eventHandler=adddrerror )


#some exception
phoneEvent.addEvent("(and server response 504. state code:)", module_Adapter,eventType=eventType.EDGE, eventHandler=subs504)

###create conf call
#TODO: Try to create the conference call

#0 VOLTE; 1 VOWIFI; 2 END Call,  value can be string/number
#need to do here
#phoneEvent.addEvent("(Update the call state to data router. state: .*)", module_Phone)
#------------------------------------------------------------------------------------
#Service part
#Security Service
serviceEvent.addEvent("Start the attach process as type: (.*), subId: .*, imsi: (.*), hplmn: (.*), vplmn: (.*)" , module_Service, eventType=eventType.EDGE, eventHandler=s2binfo, groupnum=4)
serviceEvent.addEvent("(Can not get the net id), start attach process failed.", module_Service,eventType=eventType.EDGE, color='red')
##RegisterService
#aka response
serviceEvent.addEvent("Get the challenge response: TAG = (.*),.*", module_Service, eventType=eventType.EDGE, eventHandler=akastatus)

#re-register
serviceEvent.addEvent("Try to start the re-register process with the type: (.*), info: (.*)", module_Service, eventType=eventType.EDGE, eventHandler=reregstatus, groupnum=2)

#"Try to reset the sip stack."
serviceEvent.addEvent("(Try to reset the sip stack)", module_Service, eventType=eventType.EDGE, color="blue")

#important callback event
#call_rtcp_changed should be ignored.
serviceEvent.addEvent("Notify the event: (.*)", module_Service, eventType=eventType.EDGE, eventHandler=servicecallback)

#reg status code comes here
#only care about the adapter's log
#serviceEvent.addEvent("(RegisterService.*Get the register state changed callback.*)", module_Service)
#for status_update, we use service
serviceEvent.addEvent("Get the register state changed callback, register state: (\w+), code:.*", module_Service, eventType=eventType.EDGE, eventHandler=regupdate)

#------------------------------------------------------------------------------------
#lemon part
##reinvite ack not received
serviceEvent.addEvent("(ACK to reinvite with no offer does not received when call.*)", module_Service)

#sms logs

serviceEvent.addEvent("Send the sms over wifi: smscPDU\[.*\] pdu\[.*\] retry\[(.*)\] messageRef\[.*\] serial\[.*\] text\[(.*)\]", module_Service, eventType=eventType.EDGE, eventHandler=sendsms, groupnum = 2)

serviceEvent.addEvent("Native send vowifi SMS, rpMessageRef: (.*), id: (.*)", module_Service, eventType=eventType.EDGE, eventHandler=smspair, groupnum =2)
serviceEvent.addEvent("Get the native callback, message send ok: id = (.*), type = (.*)", module_Service, eventType=eventType.EDGE, eventHandler=sendsmsok, groupnum =2)
serviceEvent.addEvent("SmsService: Message send ok, get the rpMessageRef: (.*)", module_Service, eventType=eventType.EDGE, eventHandler=sendsmsok2)

serviceEvent.addEvent("SmsService: Get the .* callback, received message: id = (.*)", module_Service, eventType=eventType.EDGE, eventHandler=recvsms)
serviceEvent.addEvent("SmsService: Received message, get the rpMessageRef: (.*)", module_Service, eventType=eventType.EDGE, eventHandler=recvsms2)

serviceEvent.addEvent("Get the native callback, message send failed: id = (.*), type = (.*), stateCode = (.*)", module_Service, eventType=eventType.EDGE, eventHandler=sendsmsfailed, groupnum = 3)
serviceEvent.addEvent("Handle the timeout message, rpMessageRef: (.*)", module_Service, eventType=eventType.EDGE, eventHandler=smstimeout)
serviceEvent.addEvent("Send SMS ack for rpMessageRef: (.*)", module_Service, eventType=eventType.EDGE, eventHandler=smsack)

#Media At cmd, default is not displayed
serviceEvent.addEvent("CPVoiceAgent: AT> AT\+SPRTPMEDIASET=(.*)", module_Service, eventType=eventType.EDGE, eventHandler=cpmediaset, display=False)

#nonce error
serviceEvent.addEvent("(Can not get data from the nonce as it is null)", module_Service, eventType=eventType.EDGE, eventHandler=nonceerror)
serviceEvent.addEvent("(Failed to get the challenge response.)", module_Service, eventType=eventType.EDGE, eventHandler=akaerror)
#some lemon keywords
#conn, sess<.*>，　notify conn event
#FIXME:　conn termed by user is not reported to user
#EN_MTFE_CONN_STAT_TERMED not reported
#EN_RSE_EVNT_SESS_TERMING  is not used in Mtc_SprocOnCallEvnt
#conf, conf<.*>, notify conf event



### MTC_EBASE_S2B , MTC_EBASE_REG

#security part
securityEvent.addEvent("SecurityS2bBinder.*(Failed to exec the ping cmd)", module_Security, eventType=eventType.EDGE, color="red")
securityEvent.addEvent("SecurityS2bBinder.*Mtc_S2bStart (no wifi network) get", module_Security, eventType=eventType.EDGE, color="red")
securityEvent.addEvent("SecurityS2bBinder.*Mtc_S2bStart (netid is error)", module_Security, eventType=eventType.EDGE, color="red")
securityEvent.addEvent("SecurityS2bBinder.*(phoneId = -1)", module_Security, eventType=eventType.EDGE, color="red")

#strange ping algo for others...
securityEvent.addEvent("SecurityS2bBinder.*pingCount = (\d) this time (ping .* success)", module_Security, eventType=eventType.EDGE, eventHandler=pingmsg, groupnum=2)
#strange ping algo for reliance
securityEvent.addEvent("SecurityS2bBinder.*this time (ping.*success)", module_Security, eventType=eventType.EDGE, color="blue")
securityEvent.addEvent("SecurityS2bBinder.*(\d+ times of pings fail), notify fail", module_Security, eventType=eventType.EDGE, color="red", eventHandler=pingfail)
securityEvent.addEvent("SecurityS2bBinder.*(s2b Start fail), notify fail.", module_Security, eventType=eventType.EDGE, color="red")
securityEvent.addEvent("SecurityS2bBinder.*roaming=(.*) hplmn =(.*) vplmn=(.*) static=(.*)", module_Security, eventType=eventType.EDGE, eventHandler=ikeroaming)
securityEvent.addEvent("LEMON.*(imsi is.*)", module_Security, eventType=eventType.EDGE)

#system_server part
## wifi

systemserverEvent.addEvent("(DhcpClient: Broadcasting DHCPDISCOVER)", module_systemserver, eventType=eventType.EDGE, eventHandler=dhcpdiscover)
systemserverEvent.addEvent("DhcpClient: Received packet: .* ACK: your new IP /(.*), netmask", module_systemserver, eventType=eventType.EDGE, eventHandler=dhcpack)

#wpa_supplicant part
## get ssid
wpaEvent.addEvent("wpa_supplicant: wlan0:    selected BSS (.*) ssid=\'(.*)\'", module_wpasupplicant,eventType=eventType.EDGE, eventHandler=wpaselect, groupnum=2)
wpaEvent.addEvent("(wpa_supplicant: wlan0: State: ASSOCIATED -> COMPLETED)", module_wpasupplicant,eventType=eventType.EDGE, eventHandler=wpaconn)


#imscm is inside phone process
imscmEventArray = imscmEvent.getarray()
for i, event in enumerate(imscmEventArray):
    phoneEvent.addWholeEvent(event)
