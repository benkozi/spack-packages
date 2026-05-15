# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
# ----------------------------------------------------------------------------

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Cece(CMakePackage):
    """CECE is a high-performance, performance-portable emissions compute
    component for Earth System Models."""

    homepage = "https://github.com/ufs-community/CECE"
    git = "https://github.com/UFS-Community/CECE.git"

    maintainers("bbakernoaa", "zmoon", "benkozi")

    license("Apache-2.0")

    version("main", branch="main")

    variant("mpi", default=True, description="Activates MPI support")
    variant("gpu", default=False, description="Activates GPU support")

    depends_on("fortran", type="build")
    depends_on("c", type="build")
    
    depends_on("esmf")
    depends_on("googletest")
    depends_on("kokkos")
    depends_on("mpi", when="+mpi")
    depends_on("netcdf-c")
    depends_on("netcdf-fortran")
    depends_on("yaml-cpp")

    # TODO Hard-disable tests for now, since rapidcheck not in Spack
    patch("cece_rapidcheck.patch")

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        spec = self.spec
        env.set("CC", spec["mpi"].mpicc)
        env.set("CXX", spec["mpi"].mpicxx)
        env.set("FC", spec["mpi"].mpifc)
        env.set("CMAKE_C_COMPILER", spec["mpi"].mpicc)
        env.set("CMAKE_CXX_COMPILER", spec["mpi"].mpicxx)
        env.set("CMAKE_Fortran_COMPILER", spec["mpi"].mpifc)

    # Must build manually for Spack
    def cmake_args(self):
        args = [
            self.define("CMAKE_BUILD_TYPE", "Release"),
            self.define("NETCDF_ROOT", self.spec["netcdf-c"].prefix),
            self.define("Kokkos_ROOT", self.spec["kokkos"].prefix),
        ]
        if self.spec.satisfies("+mpi"):
            args += [
                self.define("Kokkos_ENABLE_OPENMP", True),
                self.define("Kokkos_ENABLE_SERIAL", True),
            ]
        if self.spec.satisfies("+gpu"):
            args += [
                self.define("Kokkos_ENABLE_CUDA", True),
                self.define("Kokkos_ARCH_AMPERE80", True),
            ]
        return args
