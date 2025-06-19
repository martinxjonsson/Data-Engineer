from flask import Flask, request
from person_service import db_get_persons, db_get_person_by_id, db_create_person, db_update_person, db_delete_person
from attribute_service import db_get_attributes, db_get_attributes_by_id
from attribute_service import (
    db_get_attributes,
    db_get_attributes_by_id,
    db_create_attribute
)
from attribute_service import (
    db_get_attributes,
    db_get_attributes_by_id,
    db_create_attribute,
    db_update_attribute
)

from attribute_service import (
    db_get_attributes,
    db_get_attributes_by_id,
    db_create_attribute,
    db_update_attribute,
    db_delete_attribute
)

app = Flask(__name__)
app.route('/attribute', methods=['GET'])


def get_all_attributes():
    try:
        return db_get_attributes()
    except Exception as e:
        print(e)
        return {"error": str(e)}


@app.route('/attribute', methods=['POST'])
def create_attribute():
    try:
        data = request.get_json()
        attribute_name = data['attribute_name']
        attribute_description = data.get('attribute_description', '')
        attribute_value = data['attribute_value']
        person_id = data['person_id']

        return db_create_attribute(attribute_name, attribute_description, attribute_value, person_id)
    except Exception as e:
        print(e)
        return {"error": str(e)}


@app.route('/attribute/<int:id>', methods=['GET'])
def get_attributes_by_id(id):
    try:
        return db_get_attributes_by_id(id)
    except Exception as e:
        print(e)
        return {"error": str(e)}


@app.route('/attribute/<int:id>', methods=['PUT'])
def update_attribute(id):
    try:
        data = request.get_json()
        attribute_name = data.get('attribute_name')
        attribute_description = data.get('attribute_description', '')
        attribute_value = data.get('attribute_value')
        person_id = data.get('person_id')

        if not all([attribute_name, attribute_value, person_id]):
            return {"error": "Missing required fields"}

        return db_update_attribute(id, attribute_name, attribute_description, attribute_value, person_id)
    except Exception as e:
        print(e)
        return {"error": str(e)}


@app.route('/attribute/<int:id>', methods=['DELETE'])
def delete_attribute(id):
    try:
        return db_delete_attribute(id)
    except Exception as e:
        print(e)
        return {"error": str(e)}


@app.route("/", methods=["GET"])
def index():
    return {"index": True}


@app.route('/person', methods=['GET'])
def get_all_person():
    try:
        return db_get_persons()
    except Exception as e:
        print(e)
        return {"error": str(e)}


@app.route('/person/<int:id>', methods=['GET'])
def get_person_by_id(id):
    try:
        return db_get_person_by_id(id)
    except Exception as e:
        print(e)
        return {"error": str(e)}


@app.route("/person", methods=['POST'])
def create_person():
    try:
        data = request.get_json()
        username = data['name']
        age = data['age']
        student = data['student']
        db_create_person(username, age, student)
        return {"success": "created person: %s" % username}
    except Exception as e:
        print(e)
        return {"error": str(e)}


@app.route("/person/<int:id>", methods=['PUT'])
def update_person(id):
    try:
        data = request.get_json()
        username = data['name']
        age = data['age']
        student = data['student']
        db_update_person(id, username, age, student)
        return {"success": "updated person"}
    except Exception as e:
        print(e)
        return {"error": str(e)}


@app.route('/person/<int:id>', methods=['DELETE'])
def delete_person(id):
    try:
        return db_delete_person(id)
    except Exception as e:
        print(e)
        return {"error": str(e)}


@app.route('/attribute', methods=['GET'])
def get_all_attributes():
    return {"message": "Not implemented yet"}


if __name__ == "__main__":
    app.run(debug=True)
