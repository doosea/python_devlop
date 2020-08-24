from celery import Celery

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
