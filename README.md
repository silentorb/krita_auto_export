# Krita Auto Export

Created by Christopher W. Johnson

## Background

The primary purpose of this plugin is to help synchronize texture creation between [Krita](https://krita.org) and [Blender](https://www.blender.org),
particularly in concert with the [Auto Reload](https://github.com/samytichadou/Auto_Reload_Blender_addon) Blender addon.

## Usage

[How to install Krita plugins](https://docs.krita.org/en/user_manual/python_scripting/install_custom_python_plugin.html).

This plugin has no UI.

To enable a document for auto exporting, add `autoexport` anywhere in the Document Info (preferably the Keywords section).

Once a document is configured to auto export, a neighboring PNG with the same file name will be automatically exported:
  * Every two seconds *if* the document has unsaved changes
  * When the document is saved
