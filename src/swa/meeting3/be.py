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
import os
# ============= local library imports  ==========================


def get_file_contents(p, root=None):
    if root is None:
        root = os.path.expanduser('~')
    pp = os.path.join(root, p)
    with open(pp, 'r') as rfile:
        return [line.strip() for line in rfile]


def get_file_contents2(name):

    root = os.path.expanduser('~')
    pp = os.path.join(root, name)
    with open(pp, 'r') as rfile:
        return rfile.readlines()

# ============= EOF =============================================
