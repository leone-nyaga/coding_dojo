# RECURSION

Recursion is a programming technique where a function calls itself repeatedly until a specific base condition is met. A function that performs such self-calling behavior is known as a recursive function, and each instance of the function calling itself is called a recursive call.

```c
#include <stdio.h>

void rec(int n) {
    
    // Base Case
    if (n == 6) return;

    printf("Recursion Level %d\n", n);
    rec(n + 1);
}

int main() {
    rec(1);
    return 0;
}
```

Output

```bash
Recursion Level 1
Recursion Level 2
Recursion Level 3
Recursion Level 4
Recursion Level 5
```


