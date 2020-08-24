from celery.result import AsyncResult
from celery_tasks.celery import cel

# 根据id  获取redis 中的结果
async_result = AsyncResult(id="00c692e2-e95b-4649-b0d2-93e02660665c", app=cel)

if async_result.successful():
    result = async_result.get()
    print(result)
elif async_result.failed():
    print("执行失败！")
elif async_result.status == "PENDING":
    print("任务等待中被执行")
elif async_result.status == "RETRY":
    print("任务异常正在重试")
elif async_result.status == "STARTED":
    print("任务已经开始执行")
