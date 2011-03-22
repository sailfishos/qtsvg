FORMS     = forms/window.ui
HEADERS   = displaywidget.h \
            window.h
RESOURCES = svggenerator.qrc
SOURCES   = displaywidget.cpp \
            main.cpp \
            window.cpp

QT += svg

INCLUDEPATH += $$PWD

# install
target.path = $$[QT_INSTALL_EXAMPLES]/qtsvg/painting/svggenerator
sources.files = $$SOURCES $$HEADERS $$RESOURCES $$FORMS svggenerator.pro
sources.path = $$[QT_INSTALL_EXAMPLES]/qtsvg/painting/svggenerator
INSTALLS += target sources

symbian {
    TARGET.UID3 = 0xA000CF68
    CONFIG += qt_example
}