#-----------------------------------------------------------------------------
# Copyright (c) 2014-2017, PyInstaller Development Team.
#
# Distributed under the terms of the GNU General Public License with exception
# for distributing bootloader.
#
# The full license is in the file COPYING.txt, distributed with this software.
#-----------------------------------------------------------------------------


# Include rest_framework_json_api submodules
from PyInstaller.utils.hooks import collect_submodules
hiddenimports = collect_submodules('rest_framework_json_api')
