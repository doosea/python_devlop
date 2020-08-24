import time

from .celery import cel


@cel.task()
def send_email(name):
    print("向{}发送邮件.....".format(name))
    time.sleep(5)
    return "发邮件完成！"


if __name__ == '__main__':
    print("xxx")