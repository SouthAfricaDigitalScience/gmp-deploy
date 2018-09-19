#!/bin/bash -e
# Copyright 2016 C.S.I.R. Meraka Institute
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

. /etc/profile.d/modules.sh
module avail
module add ci
SOURCE_FILE=${NAME}-${VERSION}.tar.bz2
whoami
echo "REPO_DIR is $REPO_DIR"
echo "SRC_DIR is $SRC_DIR"
echo "WORKSPACE is $WORKSPACE"
echo "SOFT_DIR is $SOFT_DIR"

tar xjf  "${SRC_DIR}/${SOURCE_FILE}" -C "${WORKSPACE}" --skip-old-files
mkdir -vp "${WORKSPACE}/${NAME}-${VERSION}/build-${BUILD_NUMBER}"
cd "${WORKSPACE}/${NAME}-${VERSION}/build-${BUILD_NUMBER}"
../configure ABI=64 \
--with-gnu-ld \
--enable-static=yes \
--enable-shared=yes \
--build=x86_64 \
--host=x86_64-pc-linux-gnu \
--enable-cxx=yes \
--enable-fat \
--prefix="${SOFT_DIR}"
make -j2
