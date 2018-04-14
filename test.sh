#!/bin/bash

# Questo script esegue un test di peformance usando lo strumento 
# Apache Benchmark (ab)

ab -n 1000 -c 30 http://127.0.0.1:5000/doc0000000

