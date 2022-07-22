# -*- coding: utf-8 -*-
# Copyright 2022 Aneior Studio, SL
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from unittest import TestCase

from airflow_hop.hooks import HopHook

DEFAULT_HOST = 'localhost'
DEFAULT_PORT = 8081
DEFAULT_USERNAME = 'cluster'
DEFAULT_PASSWORD = 'cluster'
DEFAULT_LOG_LEVEL = 'Basic'
DEFAULT_HOP_CONFIGURATION = 'home/user/hop/config'
DEFAULT_PROJECT_NAME = 'default'
DEFAULT_HOP_CONFIG_FILE = f'{DEFAULT_HOP_CONFIGURATION}/hop-config.json'
DEFAULT_METASTORE_FILE = f'{DEFAULT_HOP_CONFIGURATION}/projects/' \
            f'{DEFAULT_PROJECT_NAME}/metadata.json'
DEFAULT_PROJECT_CONFIG_FILE = f'{DEFAULT_HOP_CONFIGURATION}/projects/' \
            f'{DEFAULT_PROJECT_NAME}/project-config.json'

class TestHopHook(TestCase):
    """
    Perform tests regarding Hooks
    """

    def test_client_constructor(self):
        client = HopHook.HopServerConnection(
                                    DEFAULT_HOST,
                                    DEFAULT_PORT,
                                    DEFAULT_USERNAME,
                                    DEFAULT_PASSWORD,
                                    DEFAULT_LOG_LEVEL,
                                    DEFAULT_HOP_CONFIGURATION,
                                    DEFAULT_PROJECT_NAME)
        self.assertEqual(client.host, DEFAULT_HOST)
        self.assertEqual(client.port, DEFAULT_PORT)
        self.assertEqual(client.username, DEFAULT_USERNAME)
        self.assertEqual(client.password, DEFAULT_PASSWORD)
        self.assertEqual(client.log_level, DEFAULT_LOG_LEVEL)
        self.assertEqual(client.hop_config_file, DEFAULT_HOP_CONFIG_FILE)
        self.assertEqual(client.metastore_file, DEFAULT_METASTORE_FILE)
        self.assertEqual(client.project_config_file, DEFAULT_PROJECT_CONFIG_FILE)
