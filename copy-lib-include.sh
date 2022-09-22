#!/bin/bash
mkdir -p ./lib
cp -R ./pjproject/pjsip/lib/*             ./lib
cp -R ./pjproject/pjlib/lib/*             ./lib
cp -R ./pjproject/pjlib-util/lib/*        ./lib
cp -R ./pjproject/pjmedia/lib/*           ./lib
cp -R ./pjproject/pjnath/lib/*            ./lib
cp -R ./pjproject/third_party/lib/*       ./lib

mkdir -p ./include
cp -R ./pjproject/pjsip/include/*         ./include
cp -R ./pjproject/pjlib/include/*         ./include
cp -R ./pjproject/pjlib-util/include/*    ./include
cp -R ./pjproject/pjmedia/include/*       ./include
cp -R ./pjproject/pjnath/include/*        ./include

#chmod u+x ./copy-lib-include.sh