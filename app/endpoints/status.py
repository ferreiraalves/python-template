#!/usr/bin/env python
# -*- coding: utf-8 -*

import logging

from flask import Blueprint, jsonify

logging.basicConfig(level=logging.INFO)
_logger = logging.getLogger(__name__)

blueprint = Blueprint('status', __name__)


@blueprint.route('/status', methods=['GET', 'OPTIONS'])
def get_status():
    return '', 200


