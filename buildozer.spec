[app]
title = Dam
package.name = dam
package.domain = org.dam
source.dir = .
source.include_exts = py,png,jpg,kv,mp4,ttf
version = 1.0.0
requirements = python3,kivy==2.1.0,kivymd,plyer,requests,android
orientation = portrait
fullscreen = 1
android.permissions = INTERNET,ACCESS_NETWORK_STATE,WRITE_EXTERNAL_STORAGE
android.api = 30
android.ndk = 23b
android.arch = armeabi-v7a

[buildozer]
log_level = 2