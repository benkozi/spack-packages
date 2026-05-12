# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
# ----------------------------------------------------------------------------

from spack.package import *


class Cece(Package):
    """CECE is a high-performance, performance-portable emissions compute
    component for Earth System Models."""

    homepage = "https://github.com/ufs-community/CECE"
    git = "https://github.com/UFS-Community/CECE.git"

    maintainers("bbakernoaa", "zmoon", "benkozi")

    license("Apache-2.0")

    version("main", branch="main")

    variant("kokkos", default=True, description="Use Kokkos")
    variant("mpi", default=True, description="Activates MPI support")

    depends_on("fortran", type="build")
    depends_on("c", type="build")
    depends_on("cxx", type="build")
    
    depends_on("esmf")
    # TODO Hard-disable tests for now, since rapidcheck not in Spack
    depends_on("googletest")
    depends_on("kokkos", when="+kokkos")
    depends_on("mpi", when="+mpi")
    depends_on("yaml-cpp")

    # TODO add non-container mode
    def install(self, spec, prefix):
        # Run Docker environment script
        runfile = join_path(self.stage.source_path, "setup.sh")
        runfile = which(runfile, required=True)
        runfile()
