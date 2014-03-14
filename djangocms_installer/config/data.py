# -*- coding: utf-8 -*-
import six

CONFIGURABLE_OPTIONS = ['--db', '--cms-version', '--django-version', '--i18n',
                        '--reversion', '--languages', '--timezone', '--use-tz',
                        '--permissions', '--bootstrap', '--starting-page']

DJANGOCMS_DEVELOP = '-e git+https://github.com/divio/django-cms@develop#egg=django-cms'
DJANGOCMS_RC = 'https://github.com/divio/django-cms/archive/3.0c1.zip'
DJANGOCMS_BETA = 'https://github.com/divio/django-cms/archive/3.0.0.beta3.zip'
DJANGOCMS_LATEST = '2.4'

DJANGO_DEVELOP = 'https://github.com/django/django/archive/master.zip'
DJANGO_LATEST = '1.5'  # this is not true, but it's the most recent version
                       # compatible with all the CMS versions

DEFAULT_REQUIREMENTS = """
django-classy-tags>=0.3.4.1
south>=0.7.2
html5lib
Pillow>=2
django-sekizai>=0.7
djangocms-file
djangocms-flash
djangocms-googlemap
djangocms-inherit
djangocms-link
djangocms-picture
djangocms-teaser
djangocms-video
"""

DJANGOCMS_2_REQUIREMENTS = """
django-mptt>=0.5.1,<0.5.3
"""

DJANGOCMS_3_REQUIREMENTS = """
django-mptt>=0.6
djangocms-text-ckeditor>=2.0.5
djangocms-admin-style
git+https://github.com/divio/djangocms-column.git#egg=djangocms-column
git+https://github.com/divio/djangocms-style.git#egg=djangocms-style
"""

DJANGO_16_REVERSION = "django-reversion>=1.8"
DJANGO_15_REVERSION = "django-reversion>=1.7,<1.8"
DJANGO_14_REVERSION = "django-reversion<1.7"

FILER_REQUIREMENTS_CMS3 = """
easy_thumbnails
https://github.com/stefanfoulis/django-filer/archive/develop.zip
https://github.com/stefanfoulis/cmsplugin-filer/archive/develop.zip
"""
FILER_REQUIREMENTS_CMS2 = """
easy_thumbnails
django-filer
cmsplugin_filer
"""

PLUGIN_LIST_TEXT = """
djangocms_installer will install and configure the following plugins:
 * djangocms-text-ckeditor (Text plugin)
 * djangocms-file (File plugin)
 * djangocms-flash (Flash plugin)
 * djangocms-googlemap (GoogleMap plugin)
 * djangocms-inherit (Inherit plugin)
 * djangocms-link (Link plugin)
 * djangocms-picture (Picture plugin)
 * djangocms-teaser (Teaser plugin)
 * djangocms-video (Video plugin)
 * djangocms_style (Style plugin)
 * djangocms_column (Style plugin)
                     
It will optionally install cmsplugin-filer plugins (if requested during
configuration):
 * cmsplugin_filer_file (File plugin, replaces cms.plugins.file)
 * cmsplugin_filer_folder (Folder plugin)
 * cmsplugin_filer_image (Image plugin, replaces cms.plugins.picture)
 * cmsplugin_filer_link (Link plugin, replaces cms.plugins.link)
 * cmsplugin_filer_teaser (Teaser plugin, replaces cms.plugins.teaser)
 * cmsplugin_filer_video (Video plugin, replaces cms.plugins.video)
"""

DRIVERS = {
    'django.db.backends.postgresql_psycopg2': 'psycopg2',
    'django.db.backends.postgresql_postgis': 'postgis',
    'django.db.backends.mysql': 'MySQL-python',
    'django.db.backends.sqlite3': '',
}

DEFAULT_PROJECT_HEADER = """# -*- coding: utf-8 -*-
import os
gettext = lambda s: s
PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
"""

STATIC_FILES = """
STATIC_ROOT = os.path.join(PROJECT_PATH, 'static_collected')
STATICFILES_DIRS = (
    os.path.join(PROJECT_PATH, 'static'),
)

"""
