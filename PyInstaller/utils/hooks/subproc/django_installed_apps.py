#-----------------------------------------------------------------------------
# Copyright (c) 2005-2017, PyInstaller Development Team.
#
# Distributed under the terms of the GNU General Public License with exception
# for distributing bootloader.
#
# The full license is in the file COPYING.txt, distributed with this software.
#-----------------------------------------------------------------------------

import django
django.setup()

from django.conf import settings

installed_apps = []


if django.VERSION >= (1, 7):
	from django.apps import apps

	for app_config in apps.get_app_configs():
		installed_apps.append((app_config.name, app_config.path))
else:
	for app in settings.INSTALLED_APPS:
		app_module = __import__(app)
		assert len(app_module.__path__) == 1
		installed_apps.append((app, app_module.__path__[0]))

print(installed_apps)
