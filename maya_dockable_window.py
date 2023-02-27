from PySide2.QtWidgets import QMainWindow, QDialog
from maya import OpenMayaUI
from maya import cmds
from shiboken2 import shiboken2
from maya.app.general.mayaMixin import MayaQWidgetDockableMixin


class MayaDockableWindow(MayaQWidgetDockableMixin, QDialog):
    def __init__(self):
        self.window_name = self.__class__.__name__ + "_dockable_window"
        self.kill_ui()

        maya_window = OpenMayaUI.MQtUtil.mainWindow()
        wrap_window = shiboken2.wrapInstance(long(maya_window), QMainWindow)
        super(MayaDockableWindow, self).__init__(parent=wrap_window)

        self.setObjectName(self.window_name)

    def kill_ui(self):
        workspace_ctl = "{}WorkspaceControl".format(self.window_name)
        if cmds.workspaceControl(workspace_ctl, exists=True):
            cmds.deleteUI(workspace_ctl)

        window = OpenMayaUI.MQtUtil.findWindow(self.window_name)
        if not window:
            return
        dialog = shiboken2.wrapInstance(long(window), QDialog)
        dialog.setParent(None)
        dialog.deleteLater()
        del dialog

    def show(self):
        super(MayaDockableWindow, self).show(dockable=True)