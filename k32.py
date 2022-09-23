from stanfordkarel import *


class ktools:
  def m(self): 
   """Shorthand for move"""
   move() 

  def tl(self):
   """Turn Left"""
   turn_left()
 
  def tr(self):
    """Turn right"""
    self.tl()
    self.tl()
    self.tl()

  def ta(self):
       """Turn Around"""
       self.tl()
       self.tl()
    
  def pick(self):
    """Pick Beeper"""
    pick_beeper()

  
  def put(self):
    """Put beeper"""
    put_beeper()

  def put2(self):
    """Put 2 beepers in a line"""
    self.put()
    self.m()
    self.put()

  def put5(self):
    """Put 5 beepers in a line"""
    self.put2()
    self.m()
    self.put2()
    self.m()
    self.put()

def main():
    """ Karel code goes here! """
    kt = ktools()
    kt.tl()
    kt.m()
    kt.m()
    kt.m()
    kt.m()
    kt.tr()
    kt.m()
    kt.put()
    pass
    

if __name__ == "__main__":
    run_karel_program()