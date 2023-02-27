from maya import cmds

class UndoStack:

    def __init__(self, name="actionName"):
        self.name = name;

    def __enter__(self):
        cmds.undoInfo(chunkName=self.name, openChunk=True)

    def __exit__(self, typ, val, tb):
        cmds.undoInfo(chunkName=self.name, closeChunk=True)