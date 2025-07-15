# CONTROL FLOW AND LOOPS

## if, else if, else

These control statements let your program make decisions:

+ if checks a condition.

+ else if checks another condition if the first one is false.

+ else runs if none of the previous conditions were true.

### Basic Syntax

```c
if (condition1) {
    // code runs if condition1 is true
}
else if (condition2) {
    // code runs if condition1 is false and condition2 is true
}
else {
    // code runs if neither condition1 nor condition2 is true
}
```

### Example in C

```c
#include <stdio.h>

int main() {
    int number = 75;

    if (number > 90) {
        printf("Grade: A\n");
    }
    else if (number > 80) {
        printf("Grade: B\n");
    }
    else if (number > 70) {
        printf("Grade: C\n");
    }
    else {
        printf("Grade: D or below\n");
    }

    return 0;
}
```

###  Output

```bash
Grade: C
```
## Switch

The switch statement is used as an alternative to multiple if-else statements when you're comparing the same variable to several constant values.

### Basic Syntax

```c
switch (expression) {
    case value1:
        // code to run if expression == value1
        break;
    case value2:
        // code to run if expression == value2
        break;
    ...
    default:
        // code to run if none of the above cases match
}
```

### Example in C

```c
#include <stdio.h>

int main() {
    int day = 3;

    switch (day) {
        case 1:
            printf("Monday\n");
            break;
        case 2:
            printf("Tuesday\n");
            break;
        case 3:
            printf("Wednesday\n");
            break;
        case 4:
            printf("Thursday\n");
            break;
        case 5:
            printf("Friday\n");
            break;
        default:
            printf("Weekend\n");
    }

    return 0;
}
```

output

```bash
wednesday
```

Another example

```c
#include <stdio.h>

// Function to check if a character is a vowel
int isVowel(char ch) {
    switch (ch) {
        case 'a':
        case 'e':
        case 'i':
        case 'o':
        case 'u':
        case 'A':
        case 'E':
        case 'I':
        case 'O':
        case 'U':
            return 1;  // It's a vowel
        default:
            return 0;  // Not a vowel
    }
}

int main() {
    char c;

    printf("Enter a character: ");
    scanf(" %c", &c);

    if (isVowel(c)) {
        printf("%c is a vowel.\n", c);
    } else {
        printf("%c is not a vowel.\n", c);
    }

    return 0;
}
```

sample run

```bash
Enter a character: E
E is a vowel.
```

## While loop

A while loop keeps executing as long as a condition is true. It's used when:

+ You don’t know ahead of time how many times you need to loop.

+ The loop may run zero or more times.

### Syntax

```
while (condition) {
    // code block to repeat
}
```

+ The loop checks the condition first.

+ If it's true, it runs the code.

+ If it's false, the loop stops.

### Example 1: Count from 1 to 5

```c
#include <stdio.h>

int main() {
    int i = 1;

    while (i <= 5) {
        printf("i = %d\n", i);
        i++;  // increase i to avoid an infinite loop
    }

    return 0;
}
```

Output:

```bash
i = 1
i = 2
i = 3
i = 4
i = 5
```

### Example 2: User Input Until Correct Password

```c
#include <stdio.h>

int main() {
    int password;

    printf("Enter the password: ");
    scanf("%d", &password);

    while (password != 1234) {
        printf("Wrong password. Try again: ");
        scanf("%d", &password);
    }

    printf("Access granted.\n");
    return 0;
}
```

### Output:

```bash
Enter the password: 111
Wrong password. Try again: 000
Wrong password. Try again: 1234
Access granted.
```

## for loop

A for loop is used when you know exactly how many times you want to run a block of code.

It’s clean and compact.

### Basic Syntax

```c
for (initialization; condition; increment) {
    // code to run each loop
}
```

+ initialization: runs once at the beginning

+ condition: checked before each iteration

+ increment: runs after each iteration

### Example 1: Count from 1 to 5

```c
#include <stdio.h>

int main() {
    for (int i = 1; i <= 5; i++) {
        printf("i = %d\n", i);
    }
    return 0;
}
```

output

```bash
i = 1
i = 2
i = 3
i = 4
i = 5
```

### Example 2: Print Even Numbers Using continue

```c
#include <stdio.h>

int main() {
    for (int i = 1; i <= 10; i++) {
        if (i % 2 != 0) {
            continue; // skip odd numbers
        }
        printf("%d is even\n", i);
    }
    return 0;
}
```

Output:

```c
2 is even
4 is even
6 is even
8 is even
10 is even
```

### Example 3: Stop When You Hit a Specific Value (Using break)

```c
#include <stdio.h>

int main() {
    for (int i = 1; i <= 10; i++) {
        if (i == 6) {
            break; // stop the loop completely
        }
        printf("%d\n", i);
    }
    return 0;
}
```

output

```bash
1
2
3
4
5
```

## Nested if

A nested if is an if statement inside another if or else block.

It lets you check multiple conditions in layers.

### Basic Syntax

```c
if (condition1) {
    // first condition is true
    if (condition2) {
        // both condition1 and condition2 are true
    }
    else {
        // condition1 is true, but condition2 is false
    }
}
else {
    // condition1 is false
}
```

### Example: Grade Classification

```c
#include <stdio.h>

int main() {
    int score;

    printf("Enter your score: ");
    scanf("%d", &score);

    if (score >= 0 && score <= 100) {
        if (score >= 90) {
            printf("Grade: A\n");
        }
        else if (score >= 80) {
            printf("Grade: B\n");
        }
        else if (score >= 70) {
            printf("Grade: C\n");
        }
        else {
            printf("Grade: D\n");
        }
    } else {
        printf("Invalid score. Must be between 0 and 100.\n");
    }

    return 0;
}
```

### Sample output

```bash
Enter your score: 85
Grade: B
```

If you enter an invalid score like -5 or 150, it gives:

```bash
Invalid score. Must be between 0 and 100.
```

## nested for and while examples

### Multiplication table

```c
#include <stdio.h>

int main() {
    for (int i = 1; i <= 5; i++) {
        for (int j = 1; j <= 10; j++) {
            printf("%d x %d = %d\t", i, j, i * j);
        }
        printf("\n");
    }

    return 0;
}
```

output

```bash
1 x 1 = 1	1 x 2 = 2	...	1 x 10 = 10
2 x 1 = 2	2 x 2 = 4	...	2 x 10 = 20
...
```



