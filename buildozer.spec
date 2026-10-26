[app]

# (str) Title of your application
title = Flappy Neon

# (str) Package name
package.name = flappyneon

# (str) Package domain (needed for android packaging)
package.domain = org.flappy

# (list) Source files to include
source.dir = .

# (list) Source files to exclude
source.exclude_exts = spec

# (list) List of inclusion/exclusion patterns
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 0.1

# (list) Application requirements
requirements = python3,kivy

# (list) Permitted permissions
android.permissions = INTERNET

# (str) Supported orientations
orientation = portrait

#
# Android specific
#

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (int) The Android target API
android.api = 31

# (int) Minimum API your APK will support
android.minapi = 21

# (int) Android SDK version to use
android.sdk = 31

# (bool) Use AndroidX
android.androidx = True

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# (int) Display warning if buildozer is run as root
warn_on_root = 1
