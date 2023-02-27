from PySide2.QtWidgets import QMainWindow, QWidget
from maya import OpenMayaUI
from shiboken2 import shiboken2


class MayaWindow(QMainWindow):
    def __init__(self):
        self.window_name = self.__class__.__name__ + "_window"
        self.kill_ui()

        maya_window = OpenMayaUI.MQtUtil.mainWindow()
        wrap_window = shiboken2.wrapInstance(long(maya_window), QMainWindow)
        super(MayaWindow, self).__init__(parent=wrap_window)

        self.setObjectName(self.window_name)

    def kill_ui(self):
        window = OpenMayaUI.MQtUtil.findWindow(self.__class__.__name__ + "_window")
        if not window:
            return

        dialog = shiboken2.wrapInstance(long(window), QMainWindow)
        dialog.setParent(None)
        dialog.deleteLater()
        del dialog

    def setLayout(self, layout):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        central_widget.setLayout(layout)
