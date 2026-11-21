#!/usr/bin/env python3
"""news-image-20261120 v3 — entrypoint (stdlib only).

Copies the built front page (entry.png, beside this file) to
$MAKEFUN_OUTPUT_DIR (default /output) as entry.png. Deterministic:
the same bytes every run. Verifies the copied file matches the
source byte for byte before exiting.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SRC, dst)
    with open(SRC, "rb") as f:
        src_bytes = f.read()
    if len(src_bytes) > 1048576:
        print("error: entry.png exceeds 1 MiB", file=sys.stderr)
        return 1
    with open(dst, "rb") as f:
        dst_bytes = f.read()
    if src_bytes != dst_bytes:
        print("error: copied entry.png does not match source", file=sys.stderr)
        return 1
    print(f"wrote {dst} ({len(dst_bytes)} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
