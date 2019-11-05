import QtQuick 2.9
import QtQuick.Window 2.0
import QtQuick.Controls 2.2
import QtQuick.Layouts 1.3
import QtWebEngine 1.9

Window {
    id: root
    width: 1024
    height: 750
    visible: true
    WebEngineView {
        id: webview
        anchors.fill: parent
        url: myUrl
        profile {
            offTheRecord: isOffTheRecord
            storageName: viewStorageName
        }
        onLoadingChanged: {
            switch (loadRequest.status) {
            case WebEngineLoadRequest.LoadStartedStatus:
                loadProgressBar.visible = true
                break

            default:
                loadProgressBar.visible = false
                break
            }
        }
        onLoadProgressChanged: loadProgressBar.value = loadProgress
    }
    ProgressBar {
        id: loadProgressBar
        width: root.width
        from: 0
        to: 100
        value: 0
        visible: false
    }
}
