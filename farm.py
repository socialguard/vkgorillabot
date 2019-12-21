import requests
import vk_api
import time
import random

random.seed(time.ctime())
vk_session = vk_api.VkApi(token='f65d946a2884628a0f241cc7965626e353b6ae67f04412768b73ffea8136019959f2b33efb47499083a9a')


def remove(value, deletechars):
    for c in deletechars:
        value = value.replace(c,'')
    return value;


from vk_api.longpoll import VkLongPoll, VkEventType
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()
L=""
caseop=0

while 2<3:

    if caseop<10:
        
        time.sleep(4)
        caseop=caseop+1
        vk.messages.send(
            chat_id=91,
            message='кейс открыть 1',
            random_id=random.randint(2,20000000),
        )
        print("opened cases: "+str(caseop)+" , no captcha")
    else:
        caseop=caseop-10
        print("sleeping for no captcha")
        time.sleep(random.randint(6,14))