#!/bin/sh
# mk.sh is a test script for PyAc2d. 

./clean.sh


Nx=8192 Ny=8192 nt=1501 rsnp=0
./run-prof.sh $Nx $Ny $nt $rsnp > log-prof.txt
