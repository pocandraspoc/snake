import collections


class ReturnValue(object):
  def __init__(self, y0, y1, y2):
     self.y0 = y0
     self.y1 = y1
     self.y2 = y2

def g(x):
  y0 = x + 1
  y1 = x * 3
  y2 = y0 ** y1
  return ReturnValue(y0, y1, y2)

print(g(2).y1)