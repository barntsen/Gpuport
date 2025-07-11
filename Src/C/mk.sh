#!/bin/sh

opt=-ffast-math
gcc -O2 $op -c ac2dmod.c
gcc -O2 $opt -c ac2d.c
gcc -O2 $opt -c diff.c
gcc -O2 $opt -c model.c
gcc -O2 $opt -c rec.c
gcc -O2 $opt -c src.c
gcc -O2 $opt -c util.c

ar cr libac2d.a ac2d.o model.o rec.o src.o util.o diff.o
gcc -o ac2dmod ac2dmod.o ac2d.o model.o rec.o src.o util.o diff.o -lm
