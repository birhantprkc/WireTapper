[app]

# (str) Title of your application
title = WireTapper

# (str) Package name
package.name = wiretapper

# (str) Package domain (needed for android/ios packaging)
package.domain = org.wiretapper

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,jpeg,svg,kv,atlas,html,css,js,json,db,csv,geojson,txt,env

# (list) List of directory to include (let empty to include all the files)
source.include_patterns = static/*,templates/*,uploads/*,images/*

# (list) Source files to exclude (let empty to not exclude anything)
source.exclude_exts = spec

# (list) List of directory to exclude (let empty to not exclude anything)
source.exclude_dirs = .git, .github, __pycache__, bin, .buildozer

# (str) Application versioning (method 1)
version = 1.0.0

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,flask,requests,werkzeug,jinja2,markupsafe,itsdangerous,click

# (str) Custom source folders for requirements
# Sets custom source for any requirement with recipes or site-packages
# requirement.source.kivy = ../kivy

# (list) Permissions
android.permissions = INTERNET, ACCESS_FINE_LOCATION, ACCESS_COARSE_LOCATION, BLUETOOTH, BLUETOOTH_ADMIN, BLUETOOTH_SCAN, BLUETOOTH_CONNECT, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK / AAB will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Use --private data storage (True) or --dir public storage (False)
android.private_storage = True

# (str) Android entry point
# python-for-android entry point
p4a.hook =

# (str) Bootstrap to use for android build
p4a.bootstrap = webview

# (str) Application entrypoint script
p4a.port = 8080
p4a.html_app = False

# (int) Orientation
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = false, 1 = true)
warn_on_root = 1

# (str) Path to build artifact storage, absolute or relative to spec file
# build_dir = ./.buildozer

# (str) Path to build output (i.e. .apk, .aab, .ipa) storage
# bin_dir = ./bin
