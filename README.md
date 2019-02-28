# Andaluh-po

Transliterate español (spanish) gettext po files to andaluz spelling proposals. Generates po and mo files

## Table of Contents

- [Description](#description)
- [Usage](#usage)
- [Roadmap](#roadmap)
- [Support](#support)
- [Contributing](#contributing)

## Description

The **Andalusian varieties of [Spanish]** (Spanish: *andaluz*; Andalusian) are spoken in Andalusia, Ceuta, Melilla, and Gibraltar. They include perhaps the most distinct of the southern variants of peninsular Spanish, differing in many respects from northern varieties, and also from Standard Spanish. Further info: https://en.wikipedia.org/wiki/Andalusian_Spanish.

This application provides with a basic [gettext](https://www.gnu.org/software/gettext/) spanish *po files* transliteration tool, using [andaluh-py](https://github.com/andalugeeks/andaluh-py) package. Further info: https://github.com/andalugeeks/andaluh-py

**PLEASE NOTICE** andalu-po performs and automatic transliteartion from spanish to andaluz, hence all english, acronym or non spanish words will be wrongly transliterated. We encourage you to manually review all po files transliterated.

## Usage

Use from the command line with the **andaluh-po** tool:

```
$ andaluh-po -h
usage: andaluh-po [-h] [-d DEST] po

Transliterate español (spanish) gettext po files to andaluz spelling
proposals. Generates po and mo files.

positional arguments:
  po                    the original po file to transliterate

optional arguments:
  -h, --help            show this help message and exit
  -d DEST, --dest DEST  destination path of the transliterated po and mo
                        files, defaults to cwd

$ andaluh-po /tmp/language-pack-gnome-es-base-18.04+20180712/data/es/LC_MESSAGES/nautilus.po -d /tmp

$ head /tmp/nautilus.po -n 80 | tail -n 20
"Nautilus supports all the basic functions of a file manager and more. It can"
" search and manage your files and folders, both locally and on a network, "
"read and write data to and from removable media, run scripts, and launch "
"applications. It has three views: Icon Grid, Icon List, and Tree List. Its "
"functions can be extended with plugins and scripts."
msgstr ""
"Nautilû âmmite toâ lâ funçionê báçicâ de un hêttôh de arxibô y argunâ mâh. "
"Puede bûccâh y hêttionâh çû arxibô y carpetâ, tanto localê como remotâ, leêh"
" y êccribîh datô de y en dîppoçitibô êttraíblê, ehecutâh çecuençiâ de órdenê"
" y abrîh aplicaçionê. Tiene trêh bîttâ: rehiya de iconô, lîtta de iconô y "
"árbô. Çe puede ampliâh çu funçionalidá con çecuençiâ de órdenê y "
"complementô."

# #-#-#-#-#  nautilus-es.po (Nautilus)  #-#-#-#-#
# components/music/nautilus-music-view.c:198
#: data/org.gnome.Nautilus.desktop.in:3 src/nautilus-mime-actions.c:107
#: src/nautilus-properties-window.c:4602 src/nautilus-window.c:3084
msgid "Files"
msgstr "Arxibô"
``` 

## Roadmap

* Migrating to python3

## Support

Please [open an issue](https://github.com/andalugeeks/andaluh-po/issues/new) for support.

## Contributing

Please contribute using [Github Flow](https://guides.github.com/introduction/flow/). Create a branch, add commits, and open a pull request.
