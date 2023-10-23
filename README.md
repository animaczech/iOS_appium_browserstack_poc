## Setup

1. I'd recommend using [PyCharm](https://www.jetbrains.com/pycharm/) as IDE.
2. Accept invitation via this [link](https://accounts.browserstack.com/jointeam/2dfe1b7563b8ca458b8abaa1463176d8 ).
3. Follow this tutorial to install all requirements
   1. https://www.browserstack.com/docs/app-automate/appium/getting-started/python/pytest
4. Download & install [Appium inspector](https://github.com/appium/appium-inspector/releases)

Now you should have your Appium setup and also PyCharm installed.
1. run Appium server:
   1. Open Terminal -> and type:
   ```
   appium
   ```
    + _Be careful about the port what Appium is using (127.0.0.1:4723)_
    + _Make sure Port is free - if not kill the process or use any other free port e.g. 127.0.0.1:4725_

2. Set project environment same as Tutorial:
    ```bash
    python3 -m venv env
    source env/bin/activate
    pip3 install -r requirements.txt
    ```
3. Configure `conftest.py` and `browserstack.yml`
  - _conftest_ based on comments in code
  - _browserstack_ via [Tutorial Step 3.c](https://www.browserstack.com/docs/app-automate/appium/getting-started/python/pytest) and `BrowserStack_Readme.md`

## Simulator

in terminal:

```bash
cd ios
```
or
```bash
cd android
```
Make sure that `conftest.py` is settled for `Local Simulator.

for all tests run: 
```
pytest
```
## Remote

Make sure that `conftest.py` is settled for `Remote BrowserStack` (uncomment the driver for Remote Browserstack).

in terminal:
- Run the below command for Android: 
    ```
    cd android
    browserstack-sdk pytest -s test_sample.py
    ```

- Run the below command for iOS: 
    ```
    cd ios
    browserstack-sdk pytest -s test_sample.py
    ```


## Appium inspector
We're gonna use Appium Inspector to identify UI Elements in the app so you can use the IDs of elements in tests (on iOS Accessibility)

Make sure Appium Inspector is connection on the same HOST/PORT as Appium is running (e.g. 127.0.0.1:4723)

To run Appium inspector you need to specify capabilities to run simulators on Android/iOS use:

`iPhoneSimulator.json`
```json
{
    "platformName": "iOS",
    "platformVersion": "17.0",
    "deviceName": "CI iPhone 11", // Name of your iOS simulator
    "automationName": "XCUITest",
    // change the path according to your *.app (located in DerivedData when you build an App)
    "app": "PATH_TO_BS_FOLDER/showmax_main.app",
    "newCommandTimeout": 360,
    "autoAcceptAlerts": "true",
    "autoDismissAlerts": "true",
    "iosInstallPause": 1000
}
```
note: Where to find *.app file:
* DerivedData -> showmax-********* -> Build -> Products -> showmax_main.app *

`~/Library/Developer/Xcode/DerivedData/{app name}/Build/Products/{scheme}-iphonesimulator/{app name}.app`


`AndroidEmulator.json`
```json
{
  "appium:deviceName": "UI TESTS - Pixel 4 API 29", // Name of your iOS simulator
  "platformName": "android",
  "appium:automationName": "UiAutomator2",
  "appium:app": "PATH_TO_PROJECT_FOLDER/android-showmax-main/app/build/intermediates/apk/staging/debug/app-staging-debug.apk",
  "appium:allowTestPackages": "true"
}
```
