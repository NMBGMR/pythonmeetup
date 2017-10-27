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


def task1():
    home = os.path.expanduser('~')

    p1 = os.path.join(home, 'Desktop', 'p1.txt')
    p2 = os.path.join(home, 'Desktop', 'p2.txt')

    with open(p1, 'r') as p1file:
        with open(p2, 'w') as p2file:
            p2file.write(p1file.read())


def task2():
    """
    format each column
    :return:
    """
    home = os.path.expanduser('~')
    p1 = os.path.join(home, 'Desktop', 'input.csv')
    p2 = os.path.join(home, 'Desktop', 'output.csv')

    with open(p1, 'r') as rfile:
        lines = rfile.readlines()

    with open(p2, 'w') as wfile:
        for i, li in enumerate(lines):
            li = li.strip()
            row = li.split(',')
            if i == 0:
                wfile.write(li)
            else:
                nli = '{},{},{}\n'.format(row[0], row[1], row[2])
                wfile.write(nli)

# ============= EOF =============================================
