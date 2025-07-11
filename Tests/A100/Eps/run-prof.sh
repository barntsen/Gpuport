#!/bin/sh
# mk.sh is a test script for ac2dmod

#./clean.sh

n1=$1  # Nx
n2=$2  # Ny
nt=$3  # nt
rsnp=$4

#Create wavelet
ricker -nt $nt -f0 30.0 -t0 0.100 -dt 0.0005 src.bin 

#Create vp
spike -n1 $n1 -n2 $n2 -val 2500.0 vp.bin

#Create rho 
spike -n1 $n1 -n2 $n2 -val 1000.0 rho.bin

#Create Q 
spike -n1 $n1 -n2 $n2 -val 100000.0 q.bin

#Run modelling
BIN=/home/barn/Dropbox/Projects/Gpuport/Src/Eps
export NBLOCKS=1024
export NTHREADS=1024
#$BIN/ac2dmod $n1 $n2 $nt $rsnp
nsys profile $BIN/ac2dmod $n1 $n2 $nt $rsnp

#./snp.sh

