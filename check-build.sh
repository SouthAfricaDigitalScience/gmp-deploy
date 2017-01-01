#!/bin/bash -e
. /etc/profile.d/modules.sh
module add ci
whoami
cd ${WORKSPACE}/${NAME}-${VERSION}/build-${BUILD_NUMBER}
make check

echo $?

make install
mkdir -p ${REPO_DIR}
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
setenv       GMP_DIR           /data/ci-build/$::env(SITE)/$::env(OS)/$::env(ARCH)/$NAME/$VERSION
prepend-path LD_LIBRARY_PATH   $::env(GMP_DIR)/lib
prepend-path GCC_INCLUDE_DIR   $::env(GMP_DIR)/include
prepend-path CFLAGS            "-I${GMP_DIR}/include"
prepend-path LDFLAGS           "-L${GMP_DIR}/lib"
MODULE_FILE
) > modules/$VERSION

mkdir -vp ${LIBRARIES_MODULES}/${NAME}
cp -v modules/$VERSION ${LIBRARIES_MODULES}/${NAME}
