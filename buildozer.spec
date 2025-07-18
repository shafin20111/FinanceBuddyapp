# Sample content for buildozer.spec
[app]

# (str) Title of your application
title = Finance Pro

# (str) Package name
package.name = financepro

# (str) Package domain (reverse DNS style)
package.domain = org.example

# (str) Source code where your main.py is located
source.dir = .

# (str) Application versioning (method 1)
version = 0.1

# (str) Application versioning (method 2)
# version.regex = 
# version.code = 

# (list) Application requirements
requirements = python3,kivy,matplotlib

# (str) Presplash image path (optional)
# presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon file path (optional)
icon.filename = assets/icon.png

# (str) Supported orientation (portrait, landscape, all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (str) Android entry point, default is ok
# android.entrypoint = org.kivy.android.PythonActivity

# (int) Target API
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 21

# (int) Android NDK version to use
android.ndk = 25b

# (bool) Use --private data storage (True recommended)
android.private_storage = true

# (bool) Android archive with debug symbols
android.debug_symbols = true

# (str) Android permissions needed
android.permissions = INTERNET

# (str) Supported architectures
android.archs = armeabi-v7a, arm64-v8a

# (list) Garden requirements for Kivy extensions (matplotlib is a garden package)
garden_requirements = matplotlib

# (bool) Copy library instead of linking (fixes some errors)
android.copy_libs = 1
