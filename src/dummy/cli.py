import json
import os
from pathlib import Path
from pprint import pformat

from pygments import highlight
from pygments.formatters.terminal256 import Terminal256Formatter
from pygments.lexers.data import JsonLexer, YamlLexer
from pygments.lexers.python import Python3Lexer


def pcformat(obj, lang="python", style="material"):
    """Pretty format with color"""

    if lang in ("python", "py"):
        code = pformat(obj, indent=2)
        lexer_cls = Python3Lexer
    elif lang == "json":
        code = json.dumps(obj, indent=2, sort_keys=True)
        lexer_cls = JsonLexer
    elif lang in ("yaml", "yml"):
        code = yaml.safe_dump(obj)
        lexer_cls = YamlLexer
    else:
        raise ValueError(format)
    return highlight(code, lexer_cls(ensurenl=False), Terminal256Formatter(style=style))


def cli_main():
    with Path("c:/temp/dummy_vars.json").open("wt") as fout:
        print(
            json.dumps(sorted(dict(os.environ.items())), indent=2, sort_keys=True),
            file=fout,
        )
    print("HELLO!!!")
    print(pcformat([1, 2, "three", 4]))
    print("Bye!")
