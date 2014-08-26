CC = gcc
CFLAGS =  -std=c99 -I. -lbcm2835
DEPS = 
OBJ = buzzer.o

%.o: %.c $(DEPS)
	$(CC) -c -o $@ $< $(CFLAGS)

buzzer: $(OBJ)
	gcc -o $@ $^ $(CFLAGS)
