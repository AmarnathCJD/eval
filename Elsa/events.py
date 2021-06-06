from Elsa import ubot, ybot
import glob
import inspect
import logging
import re
import sys
from pathlib import Path

from telethon import events 

def Ebot(**args):
    pattern = args.get("pattern", None)
    r_pattern = r"^[/?!.]"
    if pattern is not None and not pattern.startswith("(?i)"):
        args["pattern"] = "(?i)" + pattern
    args["pattern"] = pattern.replace("^/", r_pattern, 1)
    stack = inspect.stack()
    previous_stack_frame = stack[1]
    file_test = Path(previous_stack_frame.filename)
    file_test = file_test.stem.replace(".py", "")
    reg = re.compile("(.*)")
    def decorator(func):
        ubot.add_event_handler(func, events.NewMessage(**args))
        return func

    return decorator

def load_module(shortname):
    if shortname.startswith("__"):
        pass
    elif shortname.endswith("_"):
        import importlib

        import Elsa.events  # pylint:disable=E0602

        path = Path(f"Elsa/modules/{shortname}.py")
        name = "Elsa.modules.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        print("Successfully imported " + shortname)
    else:
        import importlib

        import Elsa.events  # pylint:disable=E0602

        path = Path(f"Elsa/modules/{shortname}.py")
        name = "Elsa.modules.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        mod.Cbot = Cbot
        mod.tbot = tbot
        mod.logger = logging.getLogger(shortname)
        spec.loader.exec_module(mod)
        sys.modules["Elsa.modules." + shortname] = mod
        print("Successfully imported " + shortname)


path = "Elsa/modules/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        load_module(shortname.replace(".py", ""))
