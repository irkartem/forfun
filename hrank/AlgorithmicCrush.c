#include <stdio.h>
int main() {
long int n;
long int test;
scanf("%ld%ld",&n,&test);

signed long int a1[n+1];
long int i;
signed long int max = 0;
for(i=1;i<=n;i++)
    a1[i]=0;

long int j;
for(i=1;i<=test;i++)
{

    long int a;
    scanf("%ld",&a);
    long int aa;
    scanf("%ld",&aa);
    long int sum;
    scanf("%ld",&sum);
    for(j=a;j<=aa;j++)
    {
        a1[j]=a1[j]+sum;
        if (a1[j] > max) max=a1[j];
    }


}
printf("%ld",max);
return 0;
}
