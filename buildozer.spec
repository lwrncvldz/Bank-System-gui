[app]

# (str) Title of your application
title = Professional Bank System

# (str) Package name
package.name = bankapp

# (str) Package domain (needed for android/ios)
package.domain = org.bankapp

# (str) Application version
version = 1.0

# (source.dir) Source code where the main.py lives
source.dir = .

# (list) Source files to include (empty to include all files)
source.include_exts = py,png,jpg,kv,atlas,json

# (list) Permissions
android.permissions = INTERNET

# (str) Android minSDK and maxSDK
android.minsdkversion = 21
android.maxsdkversion = 32

# (str) Android NDK version to use
android.ndk = 25b

# (str) Android SDK version to use
android.sdk = 32

# (str) Supported orientation (landscape, portrait, or sensor)
orientation = portrait

# (bool) Fullscreen (0 = no, 1 = yes)
fullscreen = 0

# (str) Presplash of the application
# presplash.filename = %(source.dir)s/data/presplash.png

# (bool) Copy library instead of making a libpymodules.so
android.copy_libs = 1

# (str) Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.archs = arm64-v8a,armeabi-v7a

# (int) Android version code (internal integer)
android.version_code = 1

# (str) Android entry point class
android.entrypoint = org.kivy.android.PythonActivity

# (bool) Enable Android auto backup feature (API >=23)
android.allow_backup = True

# (list) Gradle dependencies (Java/Kotlin)
android.gradle_dependencies = 

# (list) Java classes to add to the android app package
android.add_src = 

# (list) Gradle repositories
android.add_gradle_repositories = 

# (int) Overrides automatic log level
log_level = 2

# (int) Display warning (+1 section displayed at each error)
warn_on_root = 1

# (str) Path to build output (APK) storage
# bin_dir = ./bin

[buildozer]

# (int) Log level (0 = errors only, 1 = info, 2 = debug)
log_level = 2

# (int) Display warnings and extra info to stdout
warn_on_root = 1