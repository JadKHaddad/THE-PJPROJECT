import pjsua2 as pj
import time
import logging

SIP_HOST = "kamailio5.5.0-trusty"
SIP_PORT = "5060"


class Call(pj.Call):
    def __init__(self, acc, call_id=pj.PJSUA_INVALID_ID):
        pj.Call.__init__(self, acc, call_id)
        self.logger = logging.getLogger("Call")
        self.acc = acc

    def onDtmfDigit(self, prm):
        self.logger.info(f"[{self.acc.username}] DTMF Digit: {prm.digit}")

    def onInstantMessage(self, prm):
        self.logger.info(
            f"[{self.acc.username}] Instant Message: {prm.contentType} : {prm.msgBody}"
        )

    def onTypingIndication(self, prm):
        self.logger.info(f"[{self.acc.username}] Typing Indication: {prm.isTyping}")

    def onCallState(self, prm):
        info = self.getInfo()
        self.logger.info(f"[{self.acc.username}] Call State: {info.state}")


class CallerCall(Call):
    def __init__(self, acc, called_user, call_id=pj.PJSUA_INVALID_ID):
        Call.__init__(self, acc, call_id)
        self.logger = logging.getLogger("CallerCall")
        self.called_user = called_user
        self.acc = acc

    def onCallState(self, prm):
        info = self.getInfo()
        self.logger.info(f"[{self.acc.username}] Call State: {info.state}")
        if info.state == pj.PJSIP_INV_STATE_CONFIRMED:
            self.logger.info(f"[{self.acc.username}] Call Confirmed")
            dtmf_prm = pj.CallSendDtmfParam()
            dtmf_prm.method = pj.PJSUA_DTMF_METHOD_SIP_INFO
            dtmf_prm.digits = "1234"
            self.sendDtmf(dtmf_prm)
            self.logger.info(f"DTMF Sent: {dtmf_prm.digits}")

            message_prm = pj.SendInstantMessageParam()
            message_prm.content = "Hello World"
            self.sendInstantMessage(message_prm)
            self.logger.info(
                f"[{self.acc.username}] Instant Message Sent: {message_prm.content}"
            )

            typing_prm = pj.SendTypingIndicationParam()
            typing_prm.isTyping = True
            self.sendTypingIndication(typing_prm)
            self.logger.info(
                f"[{self.acc.username}] Typing Indication Sent: {typing_prm.isTyping}"
            )
            time.sleep(1)
            call_op_prm = pj.CallOpParam()
            self.hangup(call_op_prm)
            self.logger.info(f"[{self.acc.username}] Call Hangup")

        if info.state == pj.PJSIP_INV_STATE_DISCONNECTED:
            self.logger.info(f"[{self.acc.username}] Call Disconnected")
            # make a new call if disconnected
            # time.sleep(1) # sleeping here is causing an infinite loop
            # try:
            #     call_op_prm = pj.CallOpParam()
            #     self.logger.info(f"[{self.acc.username}] Calling: {self.called_user}")
            #     self.makeCall(
            #         f"sip:{self.called_user}@{SIP_HOST}:{SIP_PORT}", call_op_prm
            #     )
            # except pj.Error as e:
            #     logging.error(f"Exception: {e.status} {e.reason}")
            # except Exception as e:
            #     logging.error(f"Exception: {e}")


class Account(pj.Account):
    def __init__(self, username, password):
        pj.Account.__init__(self)
        self.logger = logging.getLogger("Account")
        self.username = username
        self.password = password

        self.acfg = pj.AccountConfig()
        self.acfg.idUri = f"sip:{self.username}@{SIP_HOST}:{SIP_PORT}"
        self.acfg.regConfig.registrarUri = f"sip:{SIP_HOST}:{SIP_PORT}"

        self.cred = pj.AuthCredInfo("digest", "*", self.username, 0, self.password)
        self.acfg.sipConfig.authCreds.append(self.cred)
        self.create(self.acfg)
        self.logger.info(f"Account Created [{self.username}]")

    def onRegState(self, prm):
        self.logger.info(f"[{self.username}] Reg State: {prm.code} {prm.reason}")

    def onIncomingCall(self, prm):
        self.logger.info(f"[{self.username}] Incoming Call")
        call = Call(self, call_id=prm.callId)
        call_prm = pj.CallOpParam()

        call_prm.statusCode = pj.PJSIP_SC_RINGING
        call.answer(call_prm)

        call_prm.statusCode = pj.PJSIP_SC_OK
        call.answer(call_prm)

        self.logger.info(f"[{self.username}] Incoming Call Answered")
        raise Exception("Answered")


class App:
    def __init__(
        self, sip_host, sip_port, run_time=30, handle_events_timeout=100
    ):
        self.logger = logging.getLogger("App")
        self.sip_host = sip_host
        self.sip_port = sip_port
        self.run_time = run_time
        self.handle_events_timeout = handle_events_timeout

        self.ep_cfg = pj.EpConfig()
        self.ep_cfg.uaConfig.threadCnt = 0  # important
        self.ep_cfg.uaConfig.mainThreadOnly = True  # important
        self.ep_cfg.uaConfig.maxCalls = 32

        self.ep = pj.Endpoint()
        self.ep.libCreate()
        self.ep.libInit(self.ep_cfg)
        self.ep.libStart()

        # Create SIP transport. Error handling sample is shown
        sipTpConfig = pj.TransportConfig()
        sipTpConfig.port = 0
        self.ep.transportCreate(pj.PJSIP_TRANSPORT_UDP, sipTpConfig)
        self.ep.audDevManager().setNullDev()  # important, set audio device to null

    # def start(self):
    #     self.logger.info("Starting")
    #     thread = Thread(target=self.handle_events)
    #     thread.daemon = True
    #     thread.start()
    #     self.logger.info("Started")

    def handle_events(self):
        timer = 0
        while timer < self.run_time:
            num_events = self.ep.libHandleEvents(self.handle_events_timeout)
            self.logger.info(f"Events: {num_events}")
            timer += 1
            time.sleep(1)

    def destroy(self):
        self.ep.libDestroy()
