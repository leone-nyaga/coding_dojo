#ifndef MAIN_H
#define MAIN_H

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>

void createFile(const char *filename);
void createAndWriteFile(const char *filename, const char *text);

#endif
