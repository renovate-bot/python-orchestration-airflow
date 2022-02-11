# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Generated code. DO NOT EDIT!
#
# Snippet for CheckUpgrade
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-orchestration-airflow-service


# [START composer_generated_service_v1beta1_Environments_CheckUpgrade_sync]
from google.cloud.orchestration.airflow import service_v1beta1


def sample_check_upgrade():
    # Create a client
    client = service_v1beta1.EnvironmentsClient()

    # Initialize request argument(s)
    request = service_v1beta1.CheckUpgradeRequest(
    )

    # Make the request
    operation = client.check_upgrade(request=request)

    print("Waiting for operation to complete...")

    response = operation.result()

    # Handle the response
    print(response)

# [END composer_generated_service_v1beta1_Environments_CheckUpgrade_sync]