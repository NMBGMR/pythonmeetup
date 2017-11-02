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
def mydecorator(f):
    def wrapper(*args, **kw):
        print 'MyDecorator addition ------- args={}, kw={}'.format(args, kw)
        return f(*args, **kw)

    return wrapper


class MyNumber(object):
    nominal = 0
    error = 0

    def __add__(self, other):
        self.nominal = self.nominal+other
        return self.nominal

    def __sub__(self, other):
        self.nominal= self.nominal-other
        return self.nominal

    def transpose(self):
        pass

    @mydecorator
    def T(self, a, b,c):
        print 'a={},b={}, c={}'.format(a,b,c)
        print 'asdfasdf'

    @mydecorator
    def foo(self, f, g):
        print 'foo'
    # T = property(T)

def main():
    a = MyNumber()
    # a.nominal = 12

    a.T(1, 20, 300)
    a.foo(34, 10)

if __name__ == '__main__':
    main()





# ============= EOF =============================================
