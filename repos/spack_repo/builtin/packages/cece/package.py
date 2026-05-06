# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
# ----------------------------------------------------------------------------

from spack.package import *


class Cece(Package):
    "CECE is a high-performance, performance-portable emissions compute 
    component for Earth System Models."

    homepage = "https://github.com/ufs-community/CECE"
    url = "https://github.com/UFS-Community/CECE.git"

    maintainers("bbakernoaa", "zmoon")

    license("Apache-2.0")

    # FIXME: Add proper versions and checksums here.
    version("main", branch="main")

    depends_on("fortran")
    depends_on("kokkos")
    
    depends_on("esmf")
    # TODO Hard-disable tests for now, since rapidcheck not in Spack
    depends_on("googletest")
    depends_on("yaml-cpp")

    def install(self, spec, prefix):
        # FIXME: Unknown build system
        make()
        make("install")
