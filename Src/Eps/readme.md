#  Ac2d - 2D Acoustic Finite-Difference simulation of seismic waves

This directory contains the source files for the Ac2d simulation library.
The library is written in a small Domain Specific Language (DSL)
and converted to either standard c, CUDA or c with OpenMP pragma's
using a source-to-source translator (transpiler). 
The transpiler is named eps and found in a separate github repo: 
[Eps](https://github.com/barntsen/Eps.git)

## List of source files
- mk.sh   : Script for compiling the source code
- clean.sh: Clean script
- ac2d.i  : Solver interface
- ac2d.e  : Solver methods
- diff.i  : Differentiator interface
- diff.e  : Differentiator methods
- model.i : Model interface
- model.e : Model methods
- rec.i   : Receiver interface
- rec.e   : Receiver methods
- src.i   : Source interface
- src.e   : Source methods
- ac2dmod.e : Example code to for using the library



