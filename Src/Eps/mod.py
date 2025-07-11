import numpy as np

#Set all modeling parameters
pi      = 3.14159
nx      = 251       # No of grdipoints in x-direction
ny      = 251       # No of gridpoints in y-direction
dx      = 5.0       # Grid interval
dt      = 0.0005;   # Time sampling interval
nt      = 1501      # No of time steps
t0      = 0.1       # Pulse delay
f0      = 25.0      # Dominant frequency 
w0      = 2.0*pi*f0 # Dominant angular frequency
resamp  = 1         # Resampling factor (relative to no of timesteps ) for data
sresamp = 10        # Resampling factor for snapshots
nb      = 35        # No of PML boundary points
l       = 6         # Length of differentiator
fvp     = "vp.bin"  # Vp file name
frho    = "rho.bin" # Rho file name
fqp     = "qp.bin"   # Q file name
fqp     = "qr.bin"   # Q file name
fsrc    = "src.bin" # Wavelet file name
fsnp    = "snp.bin" # Snapshot file name
press   = "p.bin"   # Pressure recording file name
#Q-models
MAXWELL = 1         # Maxwell rheology
SLS     = 2         # Standard linear solid rheology
rheol   = MAXWELL

#Source position
sx       = np.zeros(1)
sy       = np.zeros(1)
sx[0]    = nx/2     # source x-coordinate
sy[0]    = ny/2     # source y-coordinate

#Receiver positions
nr = 250            # Number of receivers
rx=np.zeros((nr))
ry=np.zeros((nr))
for i in range(0,nr):   
  rx[i] = i         # Source x-coordinate
  ry[i] = 50        # Source y-coordinate
