from sys import stdin

class Memoize:
   def __init__ (self, f):
      self.f = f
      self.mem = {}
   def __call__ (self, *args, **kwargs):
      if (args, str(kwargs)) in self.mem:
         return self.mem[args, str(kwargs)]
      else:
         tmp = self.f(*args, **kwargs)
         self.mem[args, str(kwargs)] = tmp
         return tmp


@Memoize
def get_max(i):
   maxv = i

   if i > 11:
      a = i/4
      if a > 11:
         a = get_max(a)
      b = i/3
      if b > 11:
         b = get_max(b)
      c = i/2
      if c > 11:
         c = get_max(c)

      t = a+b+c

      if t > i:
         return t
         
   return maxv

x = stdin.readlines()

for s in x:
   print get_max(int(s))