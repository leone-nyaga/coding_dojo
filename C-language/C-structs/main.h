#ifndef MAIN_H
#define MAIN_H

#include <stdio.h>
#include <string.h>

/**
 * struct Student - Information about the student
 * @name: name of student
 * @age: age of student
 * @major: major of student
 */
struct Student
{
	char name[50];
	int age;
	char major[50];
};

/**
 * struct Heroes - Information about heroes
 * @name: name of hero
 * @age: age of hero
 * @homeground: where the hero operates
 */
typedef struct Heroes
{
	char name[50];
	int age;
	char homeground[50];
} supes;

/**
 * struct dog - holds information about dogs
 * @name: name of the dog
 * @age: age of the dog
 * @owner: owner of the dog
 */
struct dog
{
	char *name;
	float age;
	char *owner;
};

/**
 * struct Alien - information on aliens
 * @name: name of alien
 * @strength: strength of alien
 * @planet: origin of alien
 */

typedef struct Alien
{
	char *name;
	int strength;
	char *planet;
} alien;

#endif
