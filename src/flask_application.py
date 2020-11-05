from flask import Flask, jsonify, request
import crud_ops
import filters

app = Flask(__name__)

@app.route(rule='/', methods=['GET'])
def home():
    return "<h1>This is the Home page</h1>"

@app.route(rule='/records', methods=['GET'])
def get_all_records():
    records = crud_ops.get_all_records()
    return jsonify(records), 200

@app.route(rule='/records/filter', methods=['GET'])
def get_filtered_records():
    id_ = request.args.get('id', default=None)
    name = request.args.get('name', default=None)
    age = int(request.args.get('age', default=-1))
    fav_sport = request.args.get('fav_sport', default=None)
    min_age = int(request.args.get('min_age', default=-1))
    max_age = int(request.args.get('max_age', default=-1))
    records = filters.get_filtered_records(id_=id_,
                                           name=name,
                                           age=None if age == -1 else age,
                                           fav_sport=fav_sport,
                                           min_age=None if min_age == -1 else min_age,
                                           max_age=None if max_age == -1 else max_age)
    return jsonify(records), 200

@app.route(rule='/record', methods=['GET'])
def get_record():
    id_ = request.args['id']
    dict_record = crud_ops.get_record(id_=id_)
    return jsonify(dict_record), 200

@app.route(rule='/record/update', methods=['GET', 'POST'])
def update_record():
    id_ = request.args['id']
    name = request.args.get('name', default=None)
    age = int(request.args.get('age', default=-1))
    if age == -1:
        age = None
    fav_sport = request.args.get('fav_sport', default=None)
    crud_ops.update_record(id_=id_, name=name, age=age, fav_sport=fav_sport)
    response = {"message": "Record was updated successfully", "status_code": 200}
    return jsonify(response), 200

@app.route(rule='/record/add', methods=['GET', 'POST'])
def add_record():
    name = request.args['name']
    age = request.args['age']
    fav_sport = request.args['fav_sport']
    crud_ops.add_record(name=name, age=age, fav_sport=fav_sport)
    response = {"message": "Record was added successfully", "status_code": 201}
    return jsonify(response), 201

@app.route(rule='/record/delete', methods=['GET'])
def delete_record():
    id_ = request.args['id']
    crud_ops.delete_record(id_=id_)
    response = {"message": "Record was deleted successfully", "status_code": 200}
    return jsonify(response), 200

if __name__ == "__main__":
    app.run(debug=True)