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


