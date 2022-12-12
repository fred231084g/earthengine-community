# Copyright 2021 The Google Earth Engine Community Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START earthengine__apidocs__ee_number_erf]
print('Error function of -10:', ee.Number(-10).erf().getInfo())  # -1
# -0.001128378
print('Error function of -0.001:', ee.Number(-0.001).erf().getInfo())
print('Error function of 0:', ee.Number(0).erf().getInfo())  # 0
# 0.001128378
print('Error function of 0.001:', ee.Number(0.001).erf().getInfo())
print('Error function of 10:', ee.Number(10).erf().getInfo())  # 1
# [END earthengine__apidocs__ee_number_erf]
