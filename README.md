[![Build Status](https://ci.sagrid.ac.za/job/gmp-deploy/badge/icon)](https://ci.sagrid.ac.za/job/gmp-deploy/)

# gmp-deploy

The repository that contains the [GNU multiple precision arithmetic library](https://gmplib.org/) for CODE-RADE

# Dependencies

This is a base node in the CODE-RADE dependency tree and has no upstream dependencies.

# Versions

We build the following versions :

  * 6.1.2
  
# Configuration


The builds are configured out-of-source with cmake :

```
../configure ABI=64 \
--with-gnu-ld \
--enable-shared \
--prefix=${SOFT_DIR}
make -j 2
```

# Citing
