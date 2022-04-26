from http import HTTPStatus
from flask import request, jsonify, current_app
from app.models.vaccine_model import Vaccine_model
from sqlalchemy.exc import IntegrityError
from datetime import datetime, timedelta


def create_vaccine():
    correct_keys = [
        "cpf",
        "name",
        "first_shot_date",
        "second_shot_date",
        "vaccine_name",
        "health_unit_name",
    ]

    data = request.get_json()
    if (
        "cpf" not in data
        or "name" not in data
        or "vaccine_name" not in data
        or "health_unit_name" not in data
    ):
        return {
            "error": "Missing obligatory keys",
            "obligatory keys": ["cpf", "name", "vaccine_name", "health_unit_name"],
        }, HTTPStatus.BAD_REQUEST

    if len(data["cpf"]) != 11:
        return {"error": "CPF length must be 11 digits"}, HTTPStatus.BAD_REQUEST

    for key in data:
        if type(data[key]) is not str:
            return {"error": "All keys must be strings"}, HTTPStatus.BAD_REQUEST

    for k in list(data.keys()):
        if k not in correct_keys:
            del data[k]

    data["name"] = str(data["name"]).lower()
    data["first_shot_date"] = str(datetime.now()).lower()
    data["second_shot_date"] = str(datetime.now() + timedelta(days=90)).lower()
    data["vaccine_name"] = str(data["vaccine_name"]).lower()
    data["health_unit_name"] = str(data["health_unit_name"]).lower()

    new_vaccination = Vaccine_model(**data)

    try:
        current_app.db.session.add(new_vaccination)
        current_app.db.session.commit()

    except IntegrityError:
        return {"error": "CPF already registered"}, HTTPStatus.CONFLICT

    new_vaccination = Vaccine_model.query.get(data["cpf"])
    return {
        "cpf": new_vaccination.cpf,
        "name": new_vaccination.name,
        "first_shot_date": new_vaccination.first_shot_date,
        "second_shot_date": new_vaccination.second_shot_date,
        "vaccine_name": new_vaccination.vaccine_name,
        "health_unit_name": new_vaccination.health_unit_name,
    }, HTTPStatus.CREATED

    # return jsonify(new_vaccination), HTTPStatus.CREATED


def read_vaccines():

    vaccination_list = Vaccine_model.query.all()

    serializer = [
        {
            "cpf": vaccination.cpf,
            "name": vaccination.name,
            "first_shot_date": vaccination.first_shot_date,
            "second_shot_date": vaccination.second_shot_date,
            "vaccine_name": vaccination.vaccine_name,
            "health_unit_name": vaccination.health_unit_name,
        }
        for vaccination in vaccination_list
    ]

    return {"data": serializer}, HTTPStatus.OK
