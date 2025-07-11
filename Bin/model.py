from ctypes import *
import pyeps
import babin as ba
import pyeps


class model :
  ''' model creates a model suitable for the pyac2d library 
      solver.

     Parameters: 
       pyac2d  : Reference to the pyac2d wave propagation
                 library.

     Returns   : model object.       

  '''

  def __init__(self,pyac2d,par):
    #Get the velocity model
    fin = ba.bin(par.fvp)
    data=fin.read((par.ny,par.nx))
    #Convert 2d numpy float array to eps
    vp=pyeps.Store2df(pyac2d,data);

    #Get the density model
    fin = ba.bin(par.frho)
    data=fin.read((par.ny,par.nx))
    #Convert 2d numpy float array to eps
    rho=pyeps.Store2df(pyac2d,data);

    #Get the Qp model
    fin = ba.bin(par.fqp)
    data=fin.read((par.ny,par.nx))
    #Convert 2d numpy float array to eps
    qp=pyeps.Store2df(pyac2d,data);

    #Get the Qr model                                                          
    fin = ba.bin(par.fqr)
    data=fin.read((par.ny,par.nx))
    #Convert 2d numpy float array to eps
    qr=pyeps.Store2df(pyac2d,data);

    #Create a new model
    # Set argument types
    pyac2d.ModelNew.argtypes=  [c_void_p,c_void_p,c_void_p,
                                c_void_p,c_float,c_float,c_float,c_int,c_int]
    pyac2d.ModelNew.restype=c_void_p

    self.model=pyac2d.ModelNew (vp,rho,qp,qr,c_float(par.dx),c_float(par.dt),
                                c_float(par.w0),c_int(par.nb),c_int(par.rheol))
