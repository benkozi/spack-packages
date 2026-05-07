# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
# ----------------------------------------------------------------------------

from spack.package import *


class Catchem(CMakePackage):
    "Configurable ATmospheric Chemistry modelling component."

    homepage = "https://github.com/ufs-community/CATChem"
    url = "https://github.com/UFS-Community/CATChem.git"

    maintainers("colin-harkins", "bbakernoaa", "zmoon", "benkozi")

    license("Apache-2.0")

    version("main", branch="main")

    depends_on("fortran", type="build")

    depends_on("hdf5")
    depends_on("netcdf-fortran")
    depends_on("mpi")

    def cmake_args(self) -> list[str]:
        return [
            self.define("CMAKE_BUILD_TYPE", "Release"),
            self.define("MPI", True),
            self.define("OPENMP", True),
            self.define("NETCDF_ROOT", self.spec["netcdf-c"].prefix),
            self.define("HDF5_ROOT", self.spec["hdf5"].prefix),
        ]
