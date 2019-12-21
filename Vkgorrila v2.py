import requests
import vk_api
import time
import random

myapi=input("Enter your vkapi token: ")
celid=input("Enter chat id: ")
random.seed(time.ctime())
vk_session = vk_api.VkApi(token=myapi)
vk_sessional= vk_api.VkApi(token='8d83315f76e7ad9173ba7c1ba6e652ff10e9ff72823ae3b3e108bfdfefec6b2c1bf630d3bc4410f684805')



def remove(value, deletechars):
    for c in deletechars:
        value = value.replace(c,'')
    return value;


from vk_api.longpoll import VkLongPoll, VkEventType
longpoll = VkLongPoll(vk_session)
longpollal = VkLongPoll(vk_sessional)
vk = vk_session.get_api()
vkal = vk_sessional.get_api()
L=""
caseop=0

while 2<3:

    if caseop<10:
        try:
            time.sleep(5)
            caseop=caseop+1
            vk.messages.send(
                chat_id=celid,
                message='кейс открыть 1',
                random_id=random.randint(2,20000000),
            )
            print("opened cases: "+str(caseop)+" , no captcha")
        except vk_api.exceptions.Captcha:
            vkal.messages.send(
                chat_id=5,
                message='ОЛО БЛЯТЬ У КОГО ТО ПРОБЛЕМЫ С КАПЧЕЙ!',
                random_id=random.randint(2,20000000),
            )
            print("Oooops, you need to write captcha!")
            input("Press enter when you enter captcha on your device:")
    else:
        caseop=caseop-10
        print("sleeping for no captcha, and selling rating...")
        vk.messages.send(
            chat_id=celid,
            message='продать рейтинг',
            random_id=random.randint(2,20000000),
        )
        time.sleep(random.randint(6,16))