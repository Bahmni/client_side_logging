# This Source Code Form is subject to the terms of the Mozilla Public License,
# v. 2.0. If a copy of the MPL was not distributed with this file, You can
# obtain one at https://www.bahmni.org/license/mplv2hd.
#
# Copyright (C) OpenMRS Inc. OpenMRS is a registered trademark and the OpenMRS
# graphic logo is a trademark of OpenMRS Inc.

from flask import Flask, request, make_response
from RotatingLogger import RotatingLogger


LOGGER_NAME = "client_side"

CONFIG_FILE = "logging.yml"

app = Flask(__name__)

logger = RotatingLogger(CONFIG_FILE, LOGGER_NAME)


def format_log(request):
    return "Client IP : %s, Post Data : %s" % (str(request.remote_addr), request.data)


@app.route("/", methods=["POST"])
def client_side_logging():
    log_data = format_log(request)
    logger.log.error(log_data)
    return make_response(request.data, 201)


if __name__ == "__main__":
    app.run()