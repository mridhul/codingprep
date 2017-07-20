#!/bin/bash

read word
first=${word[@]:0:1}
rem=${word[@]:1}

echo $rem$first"ay"