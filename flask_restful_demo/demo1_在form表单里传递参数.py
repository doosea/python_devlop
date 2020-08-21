from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

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


# 获取  &  更新
class Get_Modify(Resource):
    def get(self):
        return Tasks

    def post(self):
        args = parser.parse_args()
        t_id = int(max(Tasks.keys()).lstrip('t')) + 1
        t_id = 't%i' % t_id
        Tasks[t_id] = {'task': args['task']}
        return Tasks[t_id], 201


# 设置每个视图函数的访问格式
api.add_resource(Get_Modify, '/get_modify')

if __name__ == '__main__':
    app.run(debug=True)




