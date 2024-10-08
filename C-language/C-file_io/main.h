#ifndef MAIN_H
#define MAIN_H

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>

int main(void);
void createFile(const char *filename);
void createAndWriteFile(const char *filename, const char *text);
void appendToFile(const char *filename, const char *text);
void readFile(const char *filename);

#endif
