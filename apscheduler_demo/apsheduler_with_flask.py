from apscheduler.schedulers.background import BackgroundScheduler
import datetime, time
from flask import Flask
from flask_restful import Api, request, abort, Resource, reqparse
from flasgger import Swagger


class FlaskConf(object):
    '''
        自定义的flask 配置类， 配合app.config.from_object(flaskConf)使用
    '''
    DEBUG = False
    ENV = 'development'
    SWAGGER = {
        # 'openapi': '3.0.2',
        "title": "'算法引擎 API",
        "description": "海淀两朝伟的Flask-Swagger",
        "termsOfService": "https://github.com/doosea",
        "contact": {
            "name": "dosea",
            "url": "https://github.com/doosea",
            "email": "doosea@163.com"
        },
        "license": {
            "name": "Apache 2.0",
            "url": "https://www.apache.org/licenses/LICENSE-2.0.html"
        },
        "version": "1.0.1"
    }


class MyAPI(Resource):
    '''
        定义flask restful 风格的接口， 可以实现get,post,put,delete
        每个方法下面，可以自定义flasgger 生成swagger 的文档注释，基于openApi 3.0.2
    '''

    def get(self, id):
        """
           获取字典中的id对应的内容--get
        ---
        parameters:
           - in: path
             name: t_id
             description: id编号
             required: true
             schema:
               type: string

         """
        return id

    def post(self, id):
        return id


def abort_if_todo_doesnt_exist(id):
    '''
        参数检查校验， 不存在中断抛异常
    :param id:
    :return:
    '''
    if id not in [1, 2, 3]:
        abort(404, message="Todo {} doesn't exist".format(id))


def my_job(id="my_job"):
    print(id, "-->", datetime.datetime.now())


flaskConf = FlaskConf()
app = Flask(__name__)
app.config.from_object(flaskConf)
swagger = Swagger(app)
api = Api(app)

# 参数校验
parser = reqparse.RequestParser()
parser.add_argument('task', type=str)

# 添加路由
api.add_resource(MyAPI, '/myApi/<id>')


scheduler = BackgroundScheduler()
scheduler.add_job(my_job, args=["job_interval"], id="job_interval", trigger='interval', seconds=5,
                  start_date="2020-08-21 16:55:00", end_date="2020-08-21 17:58:00")
scheduler.add_job(my_job, args=["job_date"], id="job_date", trigger='date', run_date="2020-08-21 17:01:00")
scheduler.add_job(my_job, args=['job_once_now'], id='job_once_now')

if __name__ == '__main__':
    try:
        scheduler.start()
        print("BackgroundScheduler , 非阻塞的后台调度器，所以程序会继续向下执行")
        app.run()
    except SystemExit:
        print('exit')
        scheduler.shutdown()





