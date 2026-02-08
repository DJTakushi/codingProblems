#!/bin/sh
mkdir -p build && cp /catch2-utils/tests_runner.o build && make -s && ./build/tests_runner "$1"
