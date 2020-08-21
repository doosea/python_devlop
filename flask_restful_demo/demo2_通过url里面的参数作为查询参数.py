from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from flasgger import Swagger


# flask config
class FlaskDevelopmentConfig(object):
    DEBUG = False
    ENV = 'development'
    # SWAGGER = {'title': '算法引擎 API', 'openapi': '3.0.2', 'uiversion': 3}
    SWAGGER = {
        "title": "dosea-flask-swagger",
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


FLASK_CONFIG = FlaskDevelopmentConfig()
app = Flask(__name__)
app.config.from_object(FLASK_CONFIG)

api = Api(app)
swagger = Swagger(app)
# swagger.init_app(app)


Tasks = {
    't1': {'task': 'eat an app'},
    't2': {'task': 'play football'},
    't3': {'task': 'watching TV'},
}


def abort_if_todo_doesnt_exist(t_id):
    if t_id not in Tasks:
        abort(404, message="Todo {} doesn't exist".format(t_id))


parser = reqparse.RequestParser()
parser.add_argument('task', type=str)


# 更新 & 删除  任务
class Updata_Delete(Resource):
    def get(self, t_id):  # 根据t_id获取对应的value
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
        abort_if_todo_doesnt_exist(t_id)
        return Tasks[t_id]

    def delete(self, t_id):  # 根据t_id删除对应的value
        """
            删除字典中的id对应的键值对--delete
         ---
         parameters:
           - in: path
             name: t_id
             description: id编号
             required: true
             schema:
               type: string
          """
        abort_if_todo_doesnt_exist(t_id)
        del Tasks[t_id]
        return 'delete success'

    def post(self, t_id):  # 判断t_id是否存在，并返回Tasks整个列表
        """
            返回字典中的所有内容--post
        ---
        tags:
            - 海淀梁朝伟
        parameters:
          - name: t_id
            in: path
            description: id编号
            required: true
            schema:
                type: string

          """
        abort_if_todo_doesnt_exist(t_id)
        return Tasks, 201

    def put(self, t_id):  # 根据t_id添加对应的value，并返回所有值
        """
            更新字典中的id对应的内容，或者添加新的key-value --put
         ---
         parameters:
           - in: path
             name: t_id
             description: id编号
             required: true
             schema:
               type: string

          """
        args = parser.parse_args()
        task = {'task': args['task']}
        Tasks[t_id] = task
        return Tasks, 201


api.add_resource(Updata_Delete, '/update_delete/<t_id>')

if __name__ == '__main__':
    app.run(debug=True)
