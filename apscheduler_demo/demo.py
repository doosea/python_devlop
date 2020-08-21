"""
    BlockingScheduler : 最简单的调度器模块, 调用 start 方阻塞当前进程, 后面程序无法执行
    BackgroundScheduler ： 非阻塞的后台调度器，所以程序会继续向下执行
"""

from datetime import datetime, date
import os
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler


def tick(text):
    print(text)
    print("time is %s" % datetime.now())

# 阻塞式调度器
# scheduler = BlockingScheduler()
# 非阻塞式调度器
scheduler = BackgroundScheduler()

# （1）间隔性任务
scheduler.add_job(tick, 'interval', seconds=3, start_date='2020-08-21 16:44:00', end_date='2020-08-21 16:45:30', args=["text"])
# （2）cron
# scheduler.add_job(tick, 'cron', hour=15, minute=55, args=["text"])
# （3）date
# scheduler.add_job(tick, 'date', run_date=datetime(2020, 8, 21, 15, 52, 50), args=['text'])

print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

try:
    print("BlockingScheduler 调用 start 方阻塞当前进程, 后面程序无法执行")
    scheduler.start()
    print("BackgroundScheduler , 非阻塞的后台调度器，所以程序会继续向下执行")
except (KeyboardInterrupt, SystemExit):
    scheduler.shutdown()
