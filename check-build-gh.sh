#!/bin/bash
set -eou pipefail
# Copyright 2023 Bruce Becker
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

cd "${PWD}/${NAME}-${VERSION}/build-${GITHUB_RUN_ID}"

echo $?

make install
mkdir -vp "${REPO_DIR}/libraries/${NAME}"
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
prepend-path CFLAGS            "-I$::env(GMP_DIR)/include"
prepend-path LDFLAGS           "-L$::env(GMP_DIR)/lib"
MODULE_FILE
) >"${REPO_DIR}/libraries/${NAME}/modules/${VERSION}"
ls -lht "${REPO_DIR}/libraries/${NAME}/modules/${VERSION}"
