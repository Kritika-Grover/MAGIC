#!/bin/bash

docker build -t monomer-pipeline .
docker run monomer-pipeline