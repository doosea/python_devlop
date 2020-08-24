##  celery 异步任务

参考文献： 
- [使用 Redis](http://docs.jinkan.org/docs/celery/getting-started/brokers/redis.html#redis-caveats)
- [Celery 初步](http://docs.jinkan.org/docs/celery/getting-started/first-steps-with-celery.html#first-steps)
- [python celery 使用](https://blog.csdn.net/qq_37049050/article/details/82260151)
- [牛哄哄的celery](https://www.cnblogs.com/pyedu/p/12461819.html)

Celery是一个异步任务的调度工具。Celery 是 Distributed Task Queue，分布式任务队列，
分布式决定了可以有多个 worker 的存在，队列表示其是异步操作，即存在一个产生任务提出需求的工头，和一群等着被分配工作的码农。

首先解释几个概念
1. `Borkers`: 中间人， 任务队列本身
2. `Result Stores / backend` : 结果存储
3. `Workers`:  Celery 中的工作者，类似与生产/消费模型中的消费者，其从队列中取出任务并执行

### 使用redis 
- 设置中间件的地址, 格式为： ` redis://:password@hostname:port/db_number`
    -  `BROKER_URL = 'redis://localhost:6379/0'` 
- 设置 Redis 中存储任务的状态和返回值
    -  `CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'`
    
    
### Celery 初步
1. celery 实例
    ```python
       from celery import Celery
       
       broker = "redis://localhost:6379/0"
       backend = "redis://localhost:6379/1"
       
       cel = Celery("celery_dosea",
                    backend=backend,
                    broker=broker,
                    # 包含以下两个任务文件，去相应的py文件中找任务，对多个任务做分类
                    include=['celery_demo.celery_tasks.task01',
                             'celery_demo.celery_tasks.task02']
                    )
       
       # 时区
       cel.conf.timezone = "Asia/Shanghai"
       # 是否使用URTC
       cel.conf.enable_utc = False
    ```
   
   `Celery` 参数： 
    - 第一个参数是当前模块的名称， 必须
    - 中间人关键字参数，消息中间件的url
    
2. 异步任务文件命令行执行
    - `celery -A [task_name] worker --loglevel=info --pool threads`
    - `celery -A [task_name] worker --loglevel=info -P eventlet`
    -  其中： `task_name` 为 `py` 文件的name, `eventlet` 开启协程， `threads` 开启线程