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

    maintainers("bbakernoaa", "zmoon", "benkozi")

    license("Apache-2.0")

    version("main", branch="main")

    depends_on("fortran")
    depends_on("kokkos")
    
    depends_on("esmf")
    # TODO Hard-disable tests for now, since rapidcheck not in Spack
    depends_on("googletest")
    depends_on("yaml-cpp")

    # TODO add non-container mode
    def install(self, spec, prefix):
        # Run Docker environment script
        runfile = glob(join_path(self.stage.source_path, "setup.sh"))[0]
        runfile = which(runfile, required=True)
        runfile()
