from gettext import find
import re
e = "WARNING: The script jsonschema is installed in '/home/u_1000270/.local/bin' which is not on PATH."
if re.search('which is not on PATH', e) is None:
    print(123)
else:
    path = e[e.find("'") + 1:]
    path = path[:path.find("'")]
    if path is None:
        print(path)