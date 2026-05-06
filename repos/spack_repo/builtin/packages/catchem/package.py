# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
# ----------------------------------------------------------------------------

from spack.package import *


class Catchem(Package):
    "Configurable ATmospheric Chemistry modelling component."

    homepage = "https://github.com/ufs-community/CATChem"
    url = "https://github.com/UFS-Community/CATChem.git"

    maintainers("colin-harkins", "bbakernoaa", "zmoon")

    license("Apache-2.0", checked_by="github_user1")

    version("main", branch="main")

    depends_on("fortran")

    depends_on("hdf5")
    depends_on("netcdf-fortran")
    depends_on("mpi", when="+mpi")

    def install(self, spec, prefix):
        # FIXME: Unknown build system
        make()
        make("install")
