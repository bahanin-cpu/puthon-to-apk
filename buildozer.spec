[app]

title = My First App

package.name = myfirstapp

package.domain = org.example

source.dir = .

source.include_exts = py,png,jpg,kv,atlas

version = 1.0

requirements = python3==3.11.5,hostpython3==3.11.5,kivy==2.3.0

orientation = portrait

fullscreen = 0

android.permissions =
android.accept_sdk_license = True
android.api = 33
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21
android.archs = arm64-v8a

[buildozer]

log_level = 2

warn_on_root = 1
