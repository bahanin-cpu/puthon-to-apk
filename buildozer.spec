[app]

title = My First App

package.name = myfirstapp

package.domain = org.example

source.dir = .

source.include_exts = py,png,jpg,kv,atlas

version = 1.0

requirements = python3,kivy==2.3.0,arabic-reshaper==3.0.0,python-bidi==0.4.2

orientation = portrait

fullscreen = 0

android.permissions =
android.accept_sdk_license = True
android.api = 33
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21
android.archs = arm64-v8a
p4a.branch = v2024.01.21

[buildozer]

log_level = 2

warn_on_root = 1
