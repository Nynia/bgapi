from flask import Blueprint
api = Blueprint('api', __name__)

from . import low_value,order_times_limit, cp_info, charge_point, focused_product_info, focused_sp_info