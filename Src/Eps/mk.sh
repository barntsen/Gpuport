#!/bin/sh
# mk is a script for compiling the py2acd ac2d code

if test -z $1 ; then 
  echo " usage: mk.sh arg "
  echo "        arg is one of c, cuda, omp or hip"
  exit
fi

#Set compiler

echo "** Compiling all code with " $1

if  test $1 = c ; then
  cc=ec
  ld=el
elif  test $1 = omp ; then
  cc=ec
  ld=el
  f=-f
  omp=-fopenmp
elif test $1 = cuda ; then 
  cc=ecc 
  ld=elc
elif test $1 = hip ; then 
  cc=ech
  ld=elh
else
    echo "argument is one of eps, cuda, omp or hip"
    exit
fi

echo "Compiling with" $cc

lib=libac2d
# Compile eps code
$cc  $f -d -O   src.e
$cc  $f -d -O   diff.e
$cc  $f -d -O   model.e
$cc  $f -d -O   rec.e
$cc  $f -d -O   ac2d.e
$cc  $f -d -O   ac2dmod.e

ar rcs $lib.a ac2d.o diff.o model.o src.o rec.o
$ld $omp -o ac2dmod$1 ac2dmod.o ac2d.o diff.o model.o src.o rec.o

