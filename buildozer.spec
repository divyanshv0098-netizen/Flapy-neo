[app]
title = Flappy Neon
package.name = flappyneon
package.domain = org.flappy
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy==2.3.1,cython==0.29.36
android.archs = arm64-v8a
orientation = portrait
fullscreen = 1
android.api = 33
android.minapi = 21
android.androidx = True

[buildozer]
log_level = 2
warn_on_root = 1
