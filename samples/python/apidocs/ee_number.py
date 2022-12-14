# Copyright 2022 The Google Earth Engine Community Authors
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

# [START earthengine__apidocs__ee_number]
import math

print(ee.Number(0).getInfo())  # 0
print(ee.Number(1).getInfo())  # 1
print(ee.Number(0.0).getInfo())  # 0
print(ee.Number(1.0).getInfo())  # 1
print(ee.Number(-1.0).getInfo())  # -1
print(ee.Number(math.pi).getInfo())  # 3.141592653589793
print(ee.Number(1.2e-35).getInfo())  # 1.2e-35
print(ee.Number(3.4e10).getInfo())  # 34000000000
# [END earthengine__apidocs__ee_number]
