from re import A
from application import App, Account, SIP_HOST, SIP_PORT
import logging

SIP_USER = "user1"
SIP_PASSWD = "user1"

if __name__ == "__main__":
    logging.basicConfig(
        filename="answerer.log",
        filemode="w",
        format="%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s",
        datefmt="%H:%M:%S",
        level=logging.INFO,
    )

    app = App(sip_host=SIP_HOST, sip_port=SIP_PORT)
    account = Account(username=SIP_USER, password=SIP_PASSWD)

    app.handle_events()

    app.destroy()
