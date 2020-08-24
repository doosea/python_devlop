import time

from .celery import cel


@cel.task()
def send_msg(name):
    print("向{}发送信息.....".format(name))
    time.sleep(5)
    return "发信息完成！"
