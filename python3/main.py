import pjsua2 as pj
import time

SIP_DOMAIN = "kamailio5.5.0-trusty:5060"
SIP_USER = "user1"
SIP_PASSWD = "user1"

# Subclass to extend the Account and get notifications etc.
class Account(pj.Account):
  def onRegState(self, prm):
      print(f"***OnRegState: {prm.reason}")

# pjsua2 test function
def pjsua2_test():
  # Create and initialize the library
  ep_cfg = pj.EpConfig()
  ep_cfg.uaConfig.threadCnt = 0  # important
  ep_cfg.uaConfig.mainThreadOnly = True  # important
  ep = pj.Endpoint()
  ep.libCreate()
  ep.libInit(ep_cfg)

  # Create SIP transport. Error handling sample is shown
  sipTpConfig = pj.TransportConfig()
  sipTpConfig.port = 0
  ep.transportCreate(pj.PJSIP_TRANSPORT_UDP, sipTpConfig)
  # Start the library
  ep.libStart()

  acfg = pj.AccountConfig()
  acfg.idUri = f"sip:{SIP_USER}@{SIP_DOMAIN}"
  acfg.regConfig.registrarUri = f"sip:{SIP_DOMAIN}"
  cred = pj.AuthCredInfo("digest", "*", SIP_USER, 0, SIP_PASSWD)
  acfg.sipConfig.authCreds.append( cred )
  # Create the account
  acc = Account()
  acc.create(acfg)
  # Here we don't have anything else to do..
  
  timer = 0
  while timer < 10:
      ep.libHandleEvents(100)
      timer += 1
      time.sleep(1)
      
  # Destroy the library
  ep.libDestroy()

#
# main()
#
if __name__ == "__main__":
  pjsua2_test()