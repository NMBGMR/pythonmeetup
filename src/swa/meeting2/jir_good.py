# ===============================================================================
# Copyright 2016 ross
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ===============================================================================

# ============= standard library imports ========================
# ============= local library imports  ==========================


class Vehicle:
    _current_fuel_volume = 0
    _current_weight = 0
    _max_load = 0

    def __init__(self, color, capacity, fuel_type='diesel', fuel_capacity=12, max_load=1000):
        self._color = color
        self._capacity = capacity
        self._fuel_type = fuel_type
        self._fuel_capacity = fuel_capacity

        self._max_load = max_load

    def move(self, speed, heading):
        self._set_speed(speed)
        self._turn_steering_wheel(heading)

    def add_fuel(self, fuel_vol):

        override = True
        if not self._check_capacity(fuel_vol):
            override = self._issue_warning()

        if not self._check_weight(fuel_vol):
            override = self._issue_warning()

        if override:
            self._add_fuel(fuel_vol)

    def add_weight(self, m):
        self._current_weight = 0

    def _set_speed(self, speed):
        pass

    def _turn_steering_wheel(self, heading):
        pass

    def _check_capacity(self, v):
        return self._current_fuel + v > self._fuel_capacity

    def _check_weight(self, v):
        pass


class Car(Vehicle):
    def _set_speed(self, speed):
        pass

    def _turn_steering_wheel(self, heading):
        pass


class Boat(Vehicle):
    def _set_speed(self, speed):
        pass

    def _turn_steering_wheel(self, heading):
        pass


class Plane(Vehicle):
    def move(self, speed, heading, attitude):
        pass
# ============= EOF =============================================
