# This Source Code Form is subject to the terms of the Mozilla Public License,
# v. 2.0. If a copy of the MPL was not distributed with this file, You can
# obtain one at https://www.bahmni.org/license/mplv2hd.
#
# Copyright (C) OpenMRS Inc. OpenMRS is a registered trademark and the OpenMRS
# graphic logo is a trademark of OpenMRS Inc.

import logging
import logging.config
import logging.handlers
import os
import yaml


class RotatingLogger:
    def __init__(self, config_file, logger_name):
        config_dict = self.get_config(config_file)
        self.log = logging.getLogger(logger_name)
        handler = logging.handlers.RotatingFileHandler(filename=config_dict["filename"],
                                                       maxBytes=config_dict["maxBytes"],
                                                       backupCount=config_dict["backupCount"])
        formatter = logging.Formatter(fmt=config_dict["format"])
        handler.setFormatter(formatter)
        handler.setLevel(logging.ERROR)
        self.log.addHandler(handler)

    def get_config(self, config_file_path):
        config_file = open(os.path.dirname(__file__) + "/" + config_file_path, 'r')
        config_dict = yaml.load(config_file)
        config_file.close()
        return config_dict