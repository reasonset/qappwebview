# qappwebview

View web page or HTML local document with Qt/QML (QQmlApplicationEngine/QtWebEngineView.) Forked from (my own) autoscrolling text.

# Synopsys

* For unix platform.
* Install with `install.zsh` script.
* do `qwview.py address`

# Requires

* Python3
* Qt5
* PyQt5
* Python OpenGL
* Qt5 Controls 2

# Options

|option|description|
|-------|----------------------|
|`-i`|Enable off the record mode.|
|`-p <profile>`|Use profile name `<profile>` instead of `"Default"`.|

# Comment.

"Unsurf" in [autoscrolling text](https://github.com/reasonset/autoscrolling-text) changed QMLApplication to Qt Application with QtWebEngine, and to be not able to open local file without URL.

So this script was come for singly browsing use.
