from flask import Flask,jsonify
from flask_restful import  Api, Resource
import json
import until

app = Flask(__name__)
api = Api(app)

class Todo(Resource):
    def post(self):
        with open("data.json", encoding="utf-8") as f:
            data = json.load(f)
        x = json.dumps(data)
        y = json.loads(x)
        for i in range(len(y)):
            until.add_all_question(y[i])

    def get(self):
        sql = '''
        select * from answer
        '''
        row = until.get_all_answer(sql)
        data = []
        for r in row:
            data.append({
                "Number" : r[0],
                "Answer" : r[1]
            })
        return jsonify({"respon": data})

api.add_resource(Todo,"/body")
if __name__ == '__main__':
    app.run(port=8000, debug=True)