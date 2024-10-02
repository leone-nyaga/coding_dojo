#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/**
 * struct Student - Information about a student
 * @name: name of student
 * @age: age of student
 * @grade: grade of student
 */
struct Student
{
	char name[50];
	int age;
	float grade;
};

void printStudent(struct Student student);
