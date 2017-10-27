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


def do_hello_world():
    print 'hello world'


def approach_traffic_light(state, speed, distance, yellow_threshold=2):
    if state == 'green':
        continue_moving()
    elif state == 'red':
        apply_brakes()
    else:
        # state is yellow
        if time_to_light(distance, speed) < yellow_threshold:
            continue_moving()
        else:
            apply_brakes()


def continue_moving():
    print 'continue moving'


def apply_brakes():
    print 'apply brakes'


def time_to_light(distance, speed):
    return distance/float(speed)



if __name__ == '__main__':
    approach_traffic_light('green', 10, 10)
# ============= EOF =============================================
