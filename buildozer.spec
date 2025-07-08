[app]

title = LlamadasControl
package.name = llamadascontrol
package.domain = org.test
source.dir = .
source.include_exts = py,kv,png,jpg,atlas
version = 0.1
requirements = python3,kivy
orientation = portrait
fullscreen = 0

android.permissions = ANSWER_PHONE_CALLS, READ_PHONE_STATE
android.api = 31
android.minapi = 21
android.sdk_path = /home/kali/.buildozer/android/platform/android-sdk
android.ndk_path = /home/kali/.buildozer/android/platform/android-ndk-r25b
android.accept_sdk_license = True
android.ndk_api = 21
android.archs = arm64-v8a, armeabi-v7a
android.copy_libs = 1

[buildozer]
log_level = 2
warn_on_root = 1
