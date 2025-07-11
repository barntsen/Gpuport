''' pyeps is a python function library for storing numpy arrays in memory 

    Functions: Store2df allocates memory and copies 2D numpy array into memory 
               Store1df allocates memory and copies 1D numpy array into memory
               Store1di allocates memory and copies 1D integer arr into memory
               Store1ds allocates memory and copies 1D integer char array into memory
'''

import numpy as np
from ctypes import *

def Store2df(pyeps,arr):
  ''' Store2df allocates memory and copies 2D numpy arr into memory
  
      Parameters:
        pyeps   : Shared library containg c-functions
        arr     : 2D numpy array
  '''

  # Set the return type of the memory allocator
  pyeps.PyepsCre2df.restype=c_void_p
  nx = arr.shape[0]
  ny = arr.shape[1]
  out = pyeps.PyepsCre2df(ny,nx) 

  # Set the argument types of Set2df
  pyeps.PyepsSet2df.argtypes=[c_void_p,c_int,c_int,c_float]
  for i in range(0,nx):
    for j in range(0,ny):
      fval=c_float(float(arr[i,j]))
      pyeps.PyepsSet2df(out,j,i,fval)

  return(out)

def Store1df(pyeps,arr):
  ''' Store1df allocates memory and copies 1D numpy arr into memory
  
      Parameters:
        pyeps   : Shared library containg c-functions
        arr     : 1D numpy array
  '''

  # Set return type of allocator
  pyeps.PyepsCre1df.restype=c_void_p
  nx = arr.shape[0]
  out = pyeps.PyepsCre1df(nx) 
  pyeps.PyepsSet1df.argtypes=[c_void_p,c_int,c_float]
  for i in range(0,nx):
      fval=c_float(float(arr[i]))
      pyeps.PyepsSet1df(out,i,fval)

  return(out)

def Store1di(pyeps,arr):
  ''' Store1di allocates memory and copies 1D integer arr into memory
  
      Parameters:
        pyeps   : Shared library containg c-functions
        arr     : 1D integer array
  '''
  
  # Set return type of allocator
  pyeps.PyepsCre1di.restype=c_void_p
  nx = arr.shape[0]
  out = pyeps.PyepsCre1di(c_int(nx)) 

  # Set function argument types
  pyeps.PyepsSet1di.argtypes=[c_void_p,c_int,c_int]
  for i in range(0,nx):
      ival=c_int(int(arr[i]))
      pyeps.PyepsSet1di(out,c_int(i),ival)

  return(out)

def Store1ds(pyeps,arr):
  ''' Store1ds allocates memory and copies 1D integer char array into memory
  
      Parameters:
        pyeps   : Shared library containg c-functions
        arr     : 1D char array
  '''

  # Set return type of allocator
  pyeps.PyepsCre1ds.restype=c_void_p
  nx = len(arr)
  out = pyeps.PyepsCre1ds(nx) 

  # Set argument types
  pyeps.PyepsSet1ds.argtypes=[c_void_p,c_int,c_wchar]
  for i in range(0,nx):
    c = c_wchar(arr[i])
    pyeps.PyepsSet1ds(out,i,c)
  
  return(out)
