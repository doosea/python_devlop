# Python定时任务框架apscheduler

- [Python定时任务框架apscheduler](https://blog.csdn.net/somezz/article/details/83104368)
- [APScheduler官方文档翻译](https://www.jianshu.com/p/4f5305e220f0)

## 基本概念介绍（APScheduler 四大组件）
- `触发器（triggers）`： 触发器包含调度逻辑，描述一个任务何时被触发，按日期或按时间间隔或按 cronjob 表达式三种方式触发。每个作业都有它自己的触发器，除了初始配置之外，触发器是完全无状态的。
- `作业存储器（job stores）`： 作业存储器指定了作业被存放的位置，默认情况下作业保存在内存，也可将作业保存在各种数据库中，当作业被存放在数据库中时，它会被序列化，当被重新加载时会反序列化。作业存储器充当保存、加载、更新和查找作业的中间商。在调度器之间不能共享作业存储。
- `执行器（executors）`: 执行器是将指定的作业（调用函数）提交到线程池或进程池中运行，当任务完成时，执行器通知调度器触发相应的事件。
- `调度器（schedulers）`: 任务调度器，属于控制角色，通过它配置作业存储器、执行器和触发器，添加、修改和删除任务。调度器协调触发器、作业存储器、执行器的运行，通常只有一个调度程序运行在应用程序中，开发人员通常不需要直接处理作业存储器、执行器或触发器，配置作业存储器和执行器是通过调度器来完成的。

### 触发器
   用于设定触发任务的条件。
   - `date` : 日期：触发任务运行的具体日期
   - `interval` : 间隔：触发任务运行的时间间隔 
   - `cron`  : 周期：触发任务运行的周期
  
1. date 触发 demo  
    ```python
        from datetime import date, datetime
        from apscheduler.schedulers.blocking import BlockingScheduler
        
        sched = BlockingScheduler()
        
        def my_job(text):
            print(text)
        
        # 在2009年11月6日执行
        sched.add_job(my_job, 'date', run_date=date(2009, 11, 6), args=['text'])
        # 在2009年11月6日 16:30:05执行
        sched.add_job(my_job, 'date', run_date=datetime(2009, 11, 6, 16, 30, 5), args=['text'])
        # 文本类型
        sched.add_job(my_job, 'date', run_date='2009-11-06 16:30:05', args=['text'])
        sched.start() 
    ```

2. interval 触发demo
    ```python
       from datetime import datetime
       from apscheduler.schedulers.blocking import BlockingScheduler
       
       def job_function():
           print("Hello World")
       
       sched = BlockingScheduler()
       
       # 每2小时触发
       sched.add_job(job_function, 'interval', hours=2)
       
       # 你可以框定周期开始时间start_date和结束时间end_date
       # 周期触发的时间范围在2010-10-10 9:30 至 2014-06-15 11:00
       sched.add_job(job_function, 'interval', hours=2, start_date='2010-10-10 09:30:00', end_date='2014-06-15 11:00:00')
       sched.start()
       
    ```
   
3. cron 强大的类crontab 表达式 

 详情参考  [APScheduler官方文档翻译](https://www.jianshu.com/p/4f5305e220f0)


### 任务存储器
   一个任务储存器不要共享给多个调度器，否则会导致状态混乱

###  调度器
根据开发需求选择相应的组件，下面是不同的调度器组件：
- `BlockingScheduler`: 适用于调度程序是进程中唯一运行的进程，调用start函数会阻塞当前线程，不能立即返回。
- `BackgroundScheduler`: 适用于调度程序在应用程序的后台运行，调用start后主线程不会阻塞。
- `AsyncIOScheduler`: 适用于使用了asyncio模块的应用程序。
- `GeventScheduler`: 适用于使用gevent模块的应用程序。
- `TwistedScheduler`: 适用于构建Twisted的应用程序。
- `QtScheduler`: 适用于构建Qt的应用程序。

