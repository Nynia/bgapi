from flask import Blueprint
api = Blueprint('api', __name__)

from app.api.ismp import charge_point, cp_info, product_info
from app.api import focused_sp_info, focused_product_info, low_value
