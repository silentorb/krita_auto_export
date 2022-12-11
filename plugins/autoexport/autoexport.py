from krita import *
from .doc_cache import *


def get_active_doc():
    return Krita.instance().activeDocument()


def log(text):
    f = open("e:/deleteme.txt", "a")
    f.write(text + "\n")
    f.close()


def export_image(doc):
    if doc and doc.modified():
        file_props = InfoObject()
        file_props.setProperty("alpha", False)
        file_props.setProperty("compression", 6)  # 0-9
        file_props.setProperty("indexed", False)
        output_path = doc.fileName().replace('.kra', '.png')
        previous_batch_mode = doc.batchmode()
        doc.setBatchmode(True)
        doc.exportImage(output_path, file_props)
        doc.setBatchmode(previous_batch_mode)
        log(output_path)


def on_image_saved(filename):
    doc = get_active_doc()
    if doc and refresh_doc_cache(doc):
        export_image(doc)


def onTick():
    doc = get_active_doc()
    if doc and update_doc_cache(doc) and doc.modified():
        export_image(doc)


class AutoExport(Extension):

    def __init__(self, parent):
        super().__init__(parent)

    def setup(self):
        notifier = Krita.instance().notifier()
        notifier.setActive(True)
        notifier.imageSaved.connect(on_image_saved)
        seconds = 1000
        timer = QtCore.QTimer(self)
        timer.timeout.connect(onTick)
        timer.start(2 * seconds)


    def createActions(self, window):
        pass


Krita.instance().addExtension(AutoExport(Krita.instance()))
