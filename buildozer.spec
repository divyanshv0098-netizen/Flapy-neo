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
# 锁定版本避免拉取到不兼容的新版 Kivy
requirements = python3,kivy==2.3.0

# (list) Permitted permissions
android.permissions = INTERNET

# (str) Supported orientations
orientation = portrait

# (str) Application icon
# 如果你暂时没有 512x512 的 PNG 图标，请在前面加上 # 注释掉此行
# icon.filename = %(source.dir)s/icon.png

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (int) The Android target API
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 21

# (int) Android SDK version to use
android.sdk = 33

# (str) Android NDK version to use (推荐明确指定，避免自动下载出错)
android.ndk = 25b

# (bool) Use AndroidX
android.androidx = True

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# (int) Display warning if buildozer is run as root
warn_on_root = 1
