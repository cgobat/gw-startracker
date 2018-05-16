#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <stddef.h>
#include <stdint.h>
#include <string.h>
#include <math.h>
#include <time.h>
#include <sys/time.h>


#define NUM_TEST 100000


double  norm(int n,const double  * x, const double  * y)
{
  int i;
  double  s0,s1;
  s0 = s1 = 0;
  for (i=n>>1;i>0;i--)
    {
      s0 += x[0] * y[0];
      s1 += x[1] * y[1];
      x += 2;
      y += 2;
    }
  return sqrtf(s0+s1);
}


// Manual
double  m_norm(double  x[3])
{
  return sqrtf( (x[0] * x[0]) + (x[1] * x[1]) + (x[2] * x[2]) );
}


float timedifference_msec(struct timeval t0, struct timeval t1)
{
    return (t1.tv_sec - t0.tv_sec) * 1000.0f + (t1.tv_usec - t0.tv_usec) / 1000.0f;
}



int main(void)
{
	struct timeval t0;
	struct timeval t1;
	float elapsed;
	double res;
	int i;

	double  x[3] = { 0.12645715, -0.0821628,  -0.22324085};

	// nomr()
	gettimeofday(&t0, 0);
	printf("\n\n100000 vect norm with norm()\n");
	printf("norm(x) = %.9f \n", norm(3, x, x) );
	i = 0;
	while(i < NUM_TEST)
	{
		res = norm(3, x, x);
		i++;
	}
	gettimeofday(&t1, 0);
	elapsed = timedifference_msec(t0, t1);
	printf("T: %f ms\n", elapsed);


	// m_norm()
	gettimeofday(&t0, 0);
	printf("\n\n100000 vect norm with m_norm()\n");
	printf("m_norm(x) = %.9f \n", m_norm(x) );
	i = 0;
	while(i < NUM_TEST)
	{
		res = m_norm(x);
		i++;
	}
	gettimeofday(&t1, 0);
	elapsed = timedifference_msec(t0, t1);
	printf("T: %f ms\n", elapsed);


	return 0;
}