from flask import Blueprint
from app.controllers import vaccines_controller

bp = Blueprint("vaccinations", __name__, url_prefix="/vaccinations")

bp.get("")(vaccines_controller.read_vaccines)
bp.post("")(vaccines_controller.create_vaccine)
