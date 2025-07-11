#!/bin/sh
opt="--compiler-options -ffast-math -x cu -use_fast_math "
#arch=sm_80
arch=native

nvcc -O2  $opt -c ac2dmod.cpp
nvcc -O2  $opt -c ac2d.cpp
nvcc -O2  $opt -c diff.cpp
nvcc -O2  $opt -c model.cpp
nvcc -O2  $opt -c -g rec.cpp
nvcc -O2  $opt -c src.cpp
nvcc -O2  $opt -c util.cpp
nvcc -O2  $opt -c gpu.cpp

ar cr libac2d.a ac2d.o diff.o model.o rec.o src.o util.o gpu.o

#Debugging
nvcc -arch=$arch -O2 --compiler-options -O2 -use_fast_math \
     -o ac2dmod ac2dmod.o ac2d.o model.o rec.o src.o util.o diff.o gpu.o -lcudart 
