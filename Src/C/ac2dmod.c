#include <stdio.h>                 /* Library interface                 */
#include <stdlib.h>
#include "util.h"
#include "model.h"
#include "src.h"
#include "rec.h"
#include "ac2d.h"
#include <math.h>

int main(int argc, char *argv[])
{
  float *wavelet;    // Source pulse
  float *vp;         //
  float *rho;        //
  float *Q;          //
  float f0;

  struct model *Model; // Model
  struct rec   *Rec;   // Receiver
  struct src   *Src;   // Source

  int *sx, *sy;     // Source x,y-coordinates
  int *rx, *ry;     // Receiver x,y-coordinates
  struct ac2d  *Ac2d;  // FD solver
  int Nx,Ny;       // Model dimension in x- and y-directions.
  int nt,ntr;          // No of time steps
  int resamp, sresamp; // Resampling factors for data and snapshot
  float dt, dx;        // Time sampling and space sampling intervals
  FILE * fd;           // File desriptor for source pulse              
  int i;               // Timestep no
  char  * tmp;         // Temporary workspace
  float W0;
  int Nb,Rheol;
  int Nr,rx0;
  int l;
  float si;
  float t0,t1;         // Time at start
  int stat;

  // Main modeling parameters

  t0 = Clock();
  Nx = atoi(argv[1]);
  Ny = atoi(argv[2]);
  nt = atoi(argv[3]);

  dx=5.0; // grid interval
  dt=0.0005; // Time sampling
  l=8;      // Operator length
  f0=25.0;   // Peak frequency
  W0=f0*3.14159*2.0; // Central angular frequency
  Nb = 30;             // Border for PML attenuation
  Rheol = MAXWELL;

  // Read the velocity model
  fd=fopen("vp.bin","r");
  vp= (float*)malloc(Nx*Ny*sizeof(float));
  stat=fread(vp, sizeof(float), (size_t)Nx*Ny, fd); 
  fclose(fd);

  // Read the density model
  fd=fopen("rho.bin","r");
  rho= (float*)malloc(Nx*Ny*sizeof(float));
  stat=fread(rho, sizeof(float), (size_t)Nx*Ny, fd); 
  fclose(fd);

  // Read the attenuation model
  fd=fopen("q.bin","r");
  Q= (float*)malloc(Nx*Ny*sizeof(float));
  stat=fread(Q, sizeof(float), (size_t)Nx*Ny, fd); 
  fclose(fd);

  // Read a source signature from file
  fd=fopen("src.bin","r");
  wavelet=(float*)malloc(nt*sizeof(float));
  stat=fread(wavelet, sizeof(float), (size_t)nt, fd); 
  fclose(fd);

  /* Create a source */
  sx=(int*)malloc(sizeof(int));
  sy=(int*)malloc(sizeof(int));
  sx[0]= Nx/2;
  sy[0]= Ny/2;
  Src=SrcNew(wavelet,nt,sx,sy,1);

  /* Create a model   */
  Model = ModelNew(vp,rho,Q,dx,dt,W0,Nb,Rheol,Nx,Ny); 
  si=ModelStability(Model);
  fprintf(stderr,"Stability index: ");
  fprintf(stderr,"%f\n",si);
  fflush(stderr);

  // Create a receiver
  Nr=740;
  rx=(int*)malloc(sizeof(int)*Nr);
  ry=(int*)malloc(sizeof(int)*Nr);
  rx0=0;
  for(i=0; i<Nr; i=i+1){
    rx[i] = rx0;
    ry[i] = 50;
    rx0=rx0+8;
  }
  resamp=1;   //Output receiver sampling
  sresamp=10; //Output snapshot resampling
  ntr = nt/resamp; //No of output samples per rec
  Rec= RecNew(rx,ry,ntr,resamp,sresamp,"snp.bin",Nr);

  /* Create solver    */
  Ac2d = Ac2dNew(Model);

  t1=Clock();
  /* Run solver       */
  Ac2dSolve(Ac2d, Model, Src, Rec, nt,l);

  // Save recording
  RecSave(Rec,"p.bin");

  printf("Nx : %d \n", Nx);
  printf("Ny : %d \n", Ny);
  printf("Nt : %d \n", nt);
  printf("Solver time : %f \n",Clock()-t1); 
  printf("Wall   time : %f \n",Clock()-t0); 
  fflush(stdout);

  return(OK);
}
