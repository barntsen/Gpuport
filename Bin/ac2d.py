from ctypes import *

import pyeps
import babin as ba
import pyeps


class ac2d :
  ''' ac2d is a  class for solving the acoustic 
      wave equation.  
     
     Parameters: 
       pyac2d  : Reference to the pyac2d wave propagation
                 library.

     Returns   : ac2d object.

  '''


  def __init__(self,pyac2d,model):
    # Set return type
    pyac2d.Ac2dNew.restype=c_void_p

    #Create fd solver
    m = model.model
    pyac2d.Ac2dNew.argtypes=[c_void_p]
    self.ac2d = pyac2d.Ac2dNew(m)
  
  def solve(self, pyac2d,model,src,rec,par) :
    ''' solve computes the solution for the acoustic 
        wave equation.

        Parameters : 
          pyac2d   : Reference to the pyac2d eps library.
          model    : model object.
          src      : src object.
          rec      : rec object.
          par      : parameter object set by the configuartion file.

    '''
    # Run the pyac2d solver.
    m=model.model
    # Set argument types
    pyac2d.Ac2dSolve.argtypes=[c_void_p,c_void_p,c_void_p,c_void_p,c_int,c_int]
    pyac2d.Ac2dSolve(self.ac2d,m,src.src,rec.rec,c_int(par.nt),c_int(par.l))

