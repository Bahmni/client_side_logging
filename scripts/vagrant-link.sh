# This Source Code Form is subject to the terms of the Mozilla Public License,
# v. 2.0. If a copy of the MPL was not distributed with this file, You can
# obtain one at https://www.bahmni.org/license/mplv2hd.
#
# Copyright (C) OpenMRS Inc. OpenMRS is a registered trademark and the OpenMRS
# graphic logo is a trademark of OpenMRS Inc.

#!/bin/sh -x

PATH_OF_CURRENT_SCRIPT="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
source $PATH_OF_CURRENT_SCRIPT/vagrant/vagrant_functions.sh

run_in_vagrant -c "sudo rm -rf /var/www/client_side_logging"
run_in_vagrant -c "sudo rm -rf /usr/lib/python2.6/site-packages/client_side_logging"
run_in_vagrant -c "sudo ln -s /Project/client_side_logging /var/www/client_side_logging"
run_in_vagrant -c "sudo ln -s /Project/client_side_logging /usr/lib/python2.6/site-packages/client_side_logging"
run_in_vagrant -c "sudo chown -h jss:jss /var/www/client_side_logging"
run_in_vagrant -c "sudo chown -h jss:jss /usr/lib/python2.6/site-packages/client_side_logging"