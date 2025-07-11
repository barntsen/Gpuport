
from ctypes import *
import pyeps
import babin as ba


class rec :
  ''' rec is a class for creating receiver geometry from
       the variables in the configuration (mod.py) file

       Parameters :
         pyac2d   : Reference to the pyac2d eps wave
                    propagation library.    

         par      : Object with parameters set in the
                    configuration (mod.py) file.
       
       Returns    : Receiver object.
  '''

  def __init__(self,pyac2d,par):
    pyac2d.RecNew.restype=c_void_p
    # Convert from python variables to eps variables
    rxx = pyeps.Store1di(pyac2d,par.rx)  
    ryy = pyeps.Store1di(pyac2d,par.ry)  
    snp = pyeps.Store1ds(pyac2d,par.fsnp) 
    # Create receiver eps object.
    # Set argument types 
    pyac2d.RecNew.argtypes=[c_void_p,c_void_p,c_int,c_int,c_int,c_void_p]
    self.rec= pyac2d.RecNew(rxx,ryy,c_int(par.nt),c_int(par.resamp),
                            c_int(par.sresamp),snp);

  def save(self,pyac2d,par):
    ''' save records data to file.

        Parameters: 
          pyac2da :  Pointer to the eps pyac2d library.
          par     :  object with parameters set in the
                     configuration (mod.py) file.
 
          Returns :  None
    '''
    fname  = par.press   # Output file name for pressure recording
    fp=pyeps.Store1ds(pyac2d,fname)
    # Set argument types
    pyac2d.RecSave.argtypes=[c_void_p,c_void_p]
    pyac2d.RecSave(self.rec,fp)
