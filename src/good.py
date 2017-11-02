# ===============================================================================
# Copyright 2017 ross
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

def print_file_contents(path):
    print 'Printing contents of {}'.format(path)
    with open(path, 'r') as rfile:
        for i,line in enumerate(rfile):
            print 'Line#={}, Value={}'.format(i, line)


if __name__ == '__main__':
    test_path = 'test_file.txt'
    print_file_contents(test_path)

# ============= EOF =============================================
