# Sample content for README-Termux.txt
FinancePro Kivy App - Termux Build Instructions

1. Extract the FinancePro_Kivy.zip

2. Make sure you have Termux updated and install required packages:

    pkg update
    pkg upgrade
    pkg install python git
    pip install --upgrade pip
    pip install buildozer

3. Install additional dependencies:

    pkg install clang make libffi-dev openssl-dev

4. Initialize buildozer in the project folder (where buildozer.spec is):

    buildozer init

5. Build the APK (this will download Android SDK/NDK):

    buildozer -v android debug

6. If you get errors about missing zlib or others, try:

    pkg install zlib
    pkg install zlib-dev  # may not exist in Termux; try alternatives or skip

7. After successful build, the APK will be in:

    bin/financepro-0.1-debug.apk

8. Install the APK on your device:

    pm install -r bin/financepro-0.1-debug.apk

9. Run the app from your launcher.

---

Notes:
- Currency switcher works with local JSON config.
- No pie charts for easier build.
- UI is minimal but functional.
- Edit currency.json to add currencies.
