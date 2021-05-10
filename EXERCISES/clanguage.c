#include <stdio.h>
int main(){
    int customer_no
    float power_consumed,bill_amount;
    scanf("%d%f",&customer_no,power_consumed);
    if(power_consumed>0 && power_consumed<=200){
        bill_amount = power_consumed*0.50;
    }
    else if (power_consumed>200 && power_consumed<=400){
        bill_amount = (power_consumed-200)*0.65 + (200*0.50);
    }
    else if (power_consumed>400 && power_consumed<=600){
        bill_amount = (power_consumed-400)*0.85 + (200*0.50) + (200*0.65)
    }
    else if (power_consumed>600){
        bill_amount = (power_consumed-600)*1.00 + (200*0.50) + (200*0.65) + (200*0.85)
    }
    printf("%f",bill_amount)
}