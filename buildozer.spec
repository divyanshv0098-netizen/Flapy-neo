[app]

# (str) Title of your application
title = Flappy Neon

# (str) Package name
package.name = flappyneon

# (str) Package domain (needed for android packaging)
package.domain = org.flappy

# (list) Source files to include (let it include python files)
source.dir = .

# (list) Source files to exclude (let it empty)
source.exclude_exts = spec

# (list) List of inclusion/exclusion patterns
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 0.1

# (list) Application requirements
# Add necessary libraries here
requirements = python3,kivy

# (list) Permitted permissions
android.permissions = INTERNET

# (str) Supported orientations
orientation = portrait

# (list) List of service to declare
#services = 

#
# Android specific
#

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (string) Presplash background color
#android.presplash_color = #121212

# (list) The Android target API, default is 31
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 21

# (str) Android NDK version to use
#android.ndk = 25b

# (bool) Use AndroidX
android.androidx = True

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
