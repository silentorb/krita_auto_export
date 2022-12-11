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

## Technical Notes

### Frequency Performance

Currently there does not appear to be any practical means using the Krita API to determine whether a file was modified since the last plugin tick.

Because of that, once a document is configured to auto export and has unsaved changes, it will be repeatedly exported regardless of user interaction.

The document state could be diffed but that would be computationally expensive (primarily for the bitmaps).

This plugin could hijack the modified value of the document but the simple implementation of that would break the normal Krita modified functionality,
and more elaborate approaches that attempted to juggle the modified state would be hacky, brittle and could lead to bizarre fringe cases.  

Ideally the Krita API would provide a modified timestamp and not just a modified boolean value.  Maybe that already exists or could eventually be added.
