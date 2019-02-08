#include <stdio.h>
#include <math.h>

int main()
{
    int low1, high1, i, temp1, temp2, remainder, n = 0, result = 0;

    scanf("%d%d", &low1, &high1);

    for(i = low1 + 1; i < high1; ++i)
    {
        temp2 = i;
        temp1 = i;

      
        while (temp1 != 0)
        {
            temp1 /= 10;
            ++n;
        }

        while (temp2 != 0)
        {
            remainder = temp2 % 10;
            result += pow(remainder, n);
            temp2 /= 10;
        }

       
        if (result == i) {
            printf("%d", i);
        }

      
        n = 0;
        result = 0;

    }
    return 0;
}
