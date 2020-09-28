SHELL = /bin/bash -o pipefail
TEST_NUMBERS = 1 2 3 4 8 16 32 64 128 256 512 1024 2048 4096 8192 16384 32768 65536 131072 262144 524288

.PHONY: clean test $(TEST_NUMBERS)

lfsr: lfsr.c
	gcc lfsr.c -o lfsr

clean:
	rm lfsr

test: $(foreach i,$(TEST_NUMBERS),test_$i)
	echo "All tests passed!"

test_%: lfsr
	./lfsr $* | sort -nu | wc -l | sed "s/ //g" > /tmp/test_$*.output
	echo "$*" | diff /tmp/test_$*.output -
