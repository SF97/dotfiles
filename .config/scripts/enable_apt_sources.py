#! /usr/bin/python3

import aptsources.sourceslist as sl
import lsb_release

codename = lsb_release.get_distro_information()['CODENAME']
sources = sl.SourcesList()

for source in sources.list:
    if source.comment.lower().find("disabled on upgrade") >= 0:
        source.dist = codename
        source.set_enabled(True)
        print(source)
sources.save()
