from celery_tasks.celery import cel
from celery_tasks.task01 import send_email
from datetime import datetime, timedelta

# # 方式1
# now = datetime(2020, 8, 24, 17, 36)
# utc_now = datetime.utcfromtimestamp(now.timestamp())
# result = send_email.apply_async(args=["hi, xxxxxxxxxx"], eta=utc_now)
# print(result.id)

# 方式2
now = datetime.now()
utc_now = datetime.utcfromtimestamp(now.timestamp())
td = timedelta(seconds=10)
utc_now = utc_now + td

result = send_email.apply_async(args=["hi, yasuo"], eta=utc_now)
print(result.id)
