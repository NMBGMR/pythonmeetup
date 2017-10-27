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
# # ============= local library imports  ==========================
# letters = 'abc'
#
#
# #x=['0a','1b','2c']
#
# x=[]
#
# for sponge,cabage in enumerate(letters):
#     m = '{}{}'.format(sponge,cabage)
#     print
#     x.append(m)
#
# print sponge
# print x
#
# i='asdfadsfsadf'
#
# x2 = ['{}{}'.format(i,lll) for i,lll in enumerate(letters) ]
#
# print 'lll', lll
# print 'x2', x
#
# x=list(range(10))
#
# even = [xi for xi in x if xi%2==0]
# print even
#
# def complex_filter(xi):
#
#     return


s = 'fasdecasecsad'
ss = [(i, si) for i,si in enumerate(s)]





x='abc'

# {'a':1, 'b':1, 'c':2}


# print {xi: i for i, xi in enumerate(x) if i>1}
#
# d ={}
# for i, xi in enumerate(x):
#     if i>1:
#         d[xi]=i
# print d

# print [(i,j,z) for i in range(10) for j in range(20) for z in range(3)]

def col_stack(a,b):

    nlist = zip(a,b)

    return nlist

aa = [1,2,3]
bb = [10,20,30]

# [(1,10),
#  (2,20)
#  (3,30)]

pts = col_stack(aa, bb)
print pts
#
# print pts[0]
# print pts[1]
print zip(*pts)
print zip(pts[0], pts[1], pts[2])


# print x
# print y







# ============= EOF =============================================
