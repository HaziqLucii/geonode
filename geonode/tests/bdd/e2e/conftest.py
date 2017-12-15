# -*- coding: utf-8 -*-
#########################################################################
#
# Copyright (C) 2016 OSGeo
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#########################################################################

import os

import pytest
from geonode.tests.bdd import __file__ as bdd_path


# @pytest.fixture(scope='session')
# def pytestbdd_selenium_speed():
#     return 0.5

# @pytest.fixture(scope='session')
# def splinter_implicit_wait():
#     return True


@pytest.yield_fixture(scope='function', autouse=True)
def en_browser(browser):
    en_browser = browser
    en_browser.visit('http://localhost:8000/account/login')
    yield en_browser
    en_browser.quit()


@pytest.fixture
def pytestbdd_feature_base_dir():
    """Feature files base directory."""

    return os.path.join(
        os.path.dirname(bdd_path),
        'features'
    )
