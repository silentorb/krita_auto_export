from krita import *

cached_doc = ''
should_auto_export_doc = False

def reset_doc_cache():
    global cached_doc, should_auto_export_doc
    cached_doc = ''
    should_auto_export_doc = False


def refresh_doc_cache(doc):
    global cached_doc, should_auto_export_doc
    if doc:
        cached_doc = doc.fileName()
        should_auto_export_doc = 'autoexport' in doc.documentInfo()
    else:
        reset_doc_cache()

    return should_auto_export_doc


def update_doc_cache(doc):
    global cached_doc, should_auto_export_doc
    if doc:
        filename = doc.fileName()
        if filename != cached_doc:
            cached_doc = filename
            should_auto_export_doc = 'autoexport' in doc.documentInfo()
    else:
        reset_doc_cache()

    return should_auto_export_doc
