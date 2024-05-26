# Compiler
CC = clang

# Compiler Flags
CFLAGS = -fsanitize=address,undefined -Wall -g -fno-omit-frame-pointer

# Output Executable
TARGET = main

# Source Files
SRCS = main.c 

# Object Files (derived from source files)
OBJS = $(SRCS:.c=.o)

# Default Rule
all: $(TARGET)

# Rule to link the object files to create the executable
$(TARGET): $(OBJS)
	$(CC) $(CFLAGS) $(OBJS) -o $(TARGET)

# Rule to compile each source file into an object file
%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

# Rule to clean the build files
clean:
	rm -f $(OBJS) $(TARGET)

# .PHONY to avoid conflicts with files named 'clean' or 'all'
.PHONY: clean all