from celery import Celery
from datetime import timedelta

broker = "redis://localhost:6379/0"
backend = "redis://localhost:6379/1"

cel = Celery("celery_dosea",
             backend=backend,
             broker=broker,
             # 包含以下两个任务文件，去相应的py文件中找任务，对多个任务做分类
             include=['celery_tasks.task01',
                      'celery_tasks.task02']
             )

# 时区
cel.conf.timezone = "Asia/Shanghai"
# 是否使用URTC
cel.conf.enable_utc = False
cel.conf.beat_schedule = {
    # 名字随意命名
    'add-every-10-seconds': {
        # 执行tasks1下的test_celery函数
        'task': 'celery_tasks.task01.send_email',
        # 每隔2秒执行一次
        # 'schedule': 1.0,
        # 'schedule': crontab(minute="*/1"),
        'schedule': timedelta(seconds=6),
        # 传递参数
        'args': ('张三',)
    },

    # 'add-every-12-seconds': {
    #     'task': 'celery_tasks.task01.send_email',
    #     每年4月11号，8点42分执行
    #     'schedule': crontab(minute=42, hour=8, day_of_month=11, month_of_year=4),
    #     'args': ('张三',)
    # },
}