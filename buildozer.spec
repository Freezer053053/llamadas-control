[app]

title = LlamadasControl
package.name = llamadascontrol
package.domain = org.test
source.dir = .
source.include_exts = py,kv,png,jpg,atlas
version = 0.1
requirements = hostpython3,kivy
orientation = portrait
fullscreen = 0

android.permissions = ANSWER_PHONE_CALLS, READ_PHONE_STATE
android.api = 31
android.minapi = 21
android.accept_sdk_license = True
android.ndk_api = 21
android.archs = arm64-v8a, armeabi-v7a
android.copy_libs = 1

[buildozer]
build_dir = .buildozer
p4a.branch = develop
log_level = 2
warn_on_root = 1
