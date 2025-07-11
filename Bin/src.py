from ctypes import *
import pyeps  
import babin as ba 

class src :
  ''' src is a class for reading a source wavelet 
       and creating the source geometry 

       Parameters:
         pyac2d : Pointer to the pyac2d module 
         par    : Object containing modelling parameters
                  set in the configuration (mod.py) file.

       Returns  : Source object
  
       The pyac2d module is implemented in eps
       and contains all essential wave propagation methods.
  '''

  def __init__(self,pyac2d,par):
    # Set return type 
    pyac2d.SrcNew.restype=c_void_p
    # Read the source time function
    fin = ba.bin(par.fsrc)  
    data=fin.read((par.nt,))
    
    # Convert python variables to eps variables
    sxx = pyeps.Store1di(pyac2d,par.sx)
    syy = pyeps.Store1di(pyac2d,par.sy)
    wavelet = pyeps.Store1df(pyac2d,data)

    #Create source eps object
    # Set argument types
    pyac2d.SrcNew.argtypes=[c_void_p,c_void_p,c_void_p]
    self.src=pyac2d.SrcNew(wavelet,sxx,syy) 
