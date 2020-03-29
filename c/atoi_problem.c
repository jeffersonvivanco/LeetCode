#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>

int myAtoi(char *);

int main() {
    printf("%d", myAtoi("-91283472332"));
}

int myAtoi(char *str) {
    int i;
    long int res;
    char numStr [strlen(str) + 1];
    int numStrIndex = 0;

    int isNumber = 0;
    for (i = 0; i < strlen(str); i++) {
        char c = str[i];
        if (str[i] == ' ' && isNumber) {
            break;
        }
        if (str[i] == ' ' && isNumber == 0) {
            continue;
        }
        if (('0' > str[i]) && (str[i] > '9') && i == 0) {
            c = '0';
            break;
        }
        isNumber = 1;
        numStr[numStrIndex] = str[i];
        numStrIndex++;
    }
    numStr[numStrIndex] = '\0';
    res = atol(numStr);
    if (res > INT_MAX) res = INT_MAX;
    if (res < INT_MIN) res = INT_MIN;
    return (int)res;
}