#!/bin/sh
# Run tests of the ac2d library

./clean.sh

nt=1501 
resamp=0 
sresamp=0
nthreads=256
arch=cuda

Nx=256 Ny=256  nblocks=512 
./run.sh $Nx $Ny $nt $resamp $sresamp $nblocks $nthreads $arch > log-$arch.txt 

Nx=512 Ny=512 nblocks=2048 
./run.sh $Nx $Ny $nt $resamp $sresamp $nblocks $nthreads $arch >> log-$arch.txt

Nx=1024 Ny=1024 nblocks=8192
./run.sh $Nx $Ny $nt $resamp $sresamp $nblocks $nthreads $arch >> log-$arch.txt

Nx=2048 Ny=2048 nblocks=32768
./run.sh $Nx $Ny $nt $resamp $sresamp $nblocks $nthreads $arch >> log-$arch.txt

Nx=4096 Ny=4096 nblocks=131072
./run.sh $Nx $Ny $nt $resamp $sresamp $nblocks $nthreads $arch >> log-$arch.txt

Nx=8192 Ny=8192 nblocks=524288
./run.sh $Nx $Ny $nt $resamp $sresamp $nblocks $nthreads $arch >> log-$arch.txt
exit

Nx=16384 Ny=16384 nblocks=2097152
./run.sh $Nx $Ny $nt $resamp $sresamp $nblocks $nthreads $arch >> log-$arch.txt
