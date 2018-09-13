# gmp-deploy

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/f45600bd9b3c4fb99713a3fa5124199b)](https://app.codacy.com/app/brucellino/gmp-deploy?utm_source=github.com&utm_medium=referral&utm_content=SouthAfricaDigitalScience/gmp-deploy&utm_campaign=Badge_Grade_Settings)
 [![DOI](https://zenodo.org/badge/29038756.svg)](https://zenodo.org/badge/latestdoi/29038756)

The repository that contains the [GNU multiple precision arithmetic library](https://gmplib.org/) for CODE-RADE

## Dependencies

This is a base node in the CODE-RADE dependency tree and has no upstream dependencies.

## Versions

We build the following versions :

  * 6.1.0
  * 6.1.2

## Configuration


The builds are configured out-of-source with make :

```
../configure ABI=64 \
--with-gnu-ld \
--enable-static=yes \
--enable-shared=yes \
--build=x86_64 \
--host=x86_64-pc-linux-gnu \
--enable-cxx=yes \
--enable-fat \
--prefix=${SOFT_DIR}
```

See the [pipeline file](Jenkinsfile) for the pipeline definition

## Citing

Cite as : 

> Bruce Becker. (2018, August 29). SouthAfricaDigitalScience/gmp-deploy: GMP for CODE-RADE Foundation Release 4 (Version v0.2.0-fr4). Zenodo. http://doi.org/10.5281/zenodo.1405240