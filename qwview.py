#!/usr/bin/python
import sys
import os
from PyQt5 import QtGui, QtQml, QtWebEngine
from OpenGL import GL  #Linux workaround.  See: http://goo.gl/s0SkFl
from docopt import docopt

__doc__ = """{f}

Usage:
    {f} [-i] [-p <profile_name>] <URL>
    {f} -h | --help

Options:
    -i --incognito               Enable off the record mode.
    -p --profile <profile_name>  Use profile (storage) name.
    -h --help                    Show this help and exit.
""".format(f=__file__)

otr_mode = False
pfname = "Default"

args = docopt(__doc__)
if args['--incognito']:
    otr_mode = True
if args['--profile']:
    pfname = args['--profile']

app = QtGui.QGuiApplication(["QtWebViewer"])
app.setWindowIcon(QtGui.QIcon(":/browser"))
engine = QtQml.QQmlApplicationEngine()
cx = engine.rootContext()
cx.setContextProperty("myUrl", args["<URL>"])
cx.setContextProperty("isOffTheRecord", otr_mode)
cx.setContextProperty("viewStorageName", pfname)
engine.load("{home}/lib/qwview.qml".format(home=os.environ["HOME"]))
app.exec_()
