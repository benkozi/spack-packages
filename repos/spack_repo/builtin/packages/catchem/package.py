# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
# ----------------------------------------------------------------------------

from spack.package import *


class Catchem(CMakePackage):
    """Configurable ATmospheric Chemistry modelling component."""

    homepage = "https://github.com/ufs-community/CATChem"
    git = "https://github.com/UFS-Community/CATChem.git"

    maintainers("colin-harkins", "bbakernoaa", "zmoon", "benkozi")

    license("Apache-2.0")

    version("develop", branch="develop")
    version("gcafs", branch="feature/gcafs",
            git="https://github.com/lwcugb/CATChem.git")
    version("main", branch="main")

    variant("mpi", default=True, description="Activates MPI support")
    variant("nuopc", default=False, description="Activates NUOPC mode")
        
    depends_on("fortran", type="build")

    depends_on("hdf5")
    depends_on("netcdf-fortran")
    depends_on("mpi", when="+mpi")
    depends_on("esmf", whem="+nuopc")

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        spec = self.spec
        env.set("CC", spec["mpi"].mpicc)
        env.set("CXX", spec["mpi"].mpicxx)
        env.set("FC", spec["mpi"].mpifc)
        env.set("CMAKE_C_COMPILER", spec["mpi"].mpicc)
        env.set("CMAKE_CXX_COMPILER", spec["mpi"].mpicxx)
        env.set("CMAKE_Fortran_COMPILER", spec["mpi"].mpifc)
        env.set("CMAKE_Platform", "linux.intel")

    def cmake_args(self) -> list[str]:
        args = [
            self.define("CMAKE_BUILD_TYPE", "Release"),
            self.define("MPI", True),
            self.define("OPENMP", True),
            self.define("NETCDF_ROOT", self.spec["netcdf-c"].prefix),
            self.define("HDF5_ROOT", self.spec["hdf5"].prefix),
        ]
        if self.spec.satisfies("+nuopc"):
            args += [
                self.define("CATCHEM_BUILD_NUOPC", True),
                self.define("CATCHEM_TRACE_NUOPC", True),
                self.define("CATCHEM_BUILD_TESTING", True),
            ]
        return args

    @run_before("cmake")
    def add_submodules(self):
        git = which("git")
        git("submodule", "update", "--init", "--recursive")
