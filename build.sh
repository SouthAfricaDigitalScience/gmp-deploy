#!/bin/bash -e
SOURCE_FILE=$NAME-$VERSION.tar.gz

module load ci

mkdir -p $WORKSPACE
mkdir -p $SRC_DIR
mkdir -p $SOFT_DIR


if [[ ! -e $SRC_DIR/$SOURCE_FILE ]] ; then
  mkdir -p $SRC_DIR
  wget http://mirror.ufs.ac.za/gnu/gnu/gmp/$SOURCE_FILE -O $SRC_DIR/$SOURCE_FILE
else
   tar -xvzf $SRC_DIR/$SOURCE_FILE -C $WORKSPACE
fi
cd $WORKSPACE/$NAME-$VERSION
./configure --prefix $SOFT_DIR
make -j 8
