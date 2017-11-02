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

# ============= enthought library imports =======================
# ============= standard library imports ========================
# ============= local library imports  ==========================

print 'modB __name__={}'.format(__name__)


def util_add(a, b):
    print 'a +b ={}'.format(a + b)


def util_mult(a, b):
    print 'a * b={}'.format(a * b)



if __name__ == '__main__':
    util_add(1, 2)
    util_add(1, 20)
    util_mult(10, 2.32)
# ============= EOF =============================================
