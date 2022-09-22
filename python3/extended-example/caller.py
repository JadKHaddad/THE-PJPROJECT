from application import App, Account, CallerCall, SIP_HOST, SIP_PORT
import pjsua2 as pj
import logging
import time

SIP_USER = "user2"
SIP_PASSWD = "user2"
SIP_CALLED_USER = "user1"


if __name__ == "__main__":
    logging.basicConfig(
        filename="caller.log",
        filemode="w",
        format="%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s",
        datefmt="%H:%M:%S",
        level=logging.INFO,
    )

    app = App(sip_host=SIP_HOST, sip_port=SIP_PORT)
    account = Account(username=SIP_USER, password=SIP_PASSWD)

    time.sleep(3)
    call = CallerCall(account, SIP_CALLED_USER)
    call_op_prm = pj.CallOpParam()
    try:
        call.makeCall(f"sip:{SIP_CALLED_USER}@{SIP_HOST}:{SIP_PORT}", call_op_prm)
    except pj.Error as e:
        logging.error(f"Exception: {e.status} {e.reason}")
    except Exception as e:
        logging.error(f"Exception: {e}")

    app.handle_events()

    app.destroy()
