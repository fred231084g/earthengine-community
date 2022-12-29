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

# [START earthengine__apidocs__ee_array_erfc]
import altair as alt
import pandas as pd

print(ee.Array([-6]).erfc().getInfo())  # [2]
print(ee.Array([0]).erfc().getInfo())  # [1]
print(ee.Array([28]).erfc().getInfo())  # [0]

start = -3
end = 3
points = ee.Array(ee.List.sequence(start, end, None, 50))
values = points.erfc()

df = pd.DataFrame({'x': points.getInfo(), 'erfc(x)': values.getInfo()})

# Plot erfc() defined above.
alt.Chart(df).mark_line().encode(
    x=alt.X('x', axis=alt.Axis(values=[start, 0, end])),
    y=alt.Y('erfc(x)', axis=alt.Axis(values=[0, 1, 2]))
)
# [END earthengine__apidocs__ee_array_erfc]
