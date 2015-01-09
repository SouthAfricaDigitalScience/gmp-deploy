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
make check
make install DESTDIR=$WORKSPACE/build

mkdir -p $REPO_DIR
rm -rf $REPO_DIR/*
tar -cvzf $REPO_DIR/build.tar.gz -C $WORKSPACE/build apprepo

mkdir -p modules
(
cat <<MODULE_FILE
#%Module1.0
## $NAME modulefile
##
proc ModulesHelp { } {
    puts stderr "       This module does nothing but alert the user"
    puts stderr "       that the [module-info name] module is not available"
}

module-whatis   "$NAME $VERSION."
setenv       GMP_VERSION       $VERSION
setenv       GMP_DIR           /apprepo/$::env(SITE)/$::env(OS)/$::env(ARCH)/$NAME/$VERSION
prepend-path LD_LIBRARY_PATH   $::env(GMP_DIR)/lib
MODULE_FILE
) > modules/$VERSION

mkdir -p $LIBRARIES_MODULES/$NAME
cp modules/$VERSION $LIBRARIES_MODULES/$NAME
