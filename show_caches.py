#!/usr/bin/env python3

import pip
from distutils.version import LooseVersion

# https://stackoverflow.com/questions/34578168/where-is-pip-cache-folder


def show_caches():
    if LooseVersion(pip.__version__) < LooseVersion("10"):
        # older pip version
        from pip.utils.appdirs import user_cache_dir
    else:
        # newer pip version
        from pip._internal.utils.appdirs import user_cache_dir

    pip_cache_dir = user_cache_dir("pip")
    print(f"pip cache dir: {pip_cache_dir}")
    wheel_cache_dir = user_cache_dir("wheel")
    print(f"wheel cache dir: {wheel_cache_dir}")


if __name__ == "__main__":
    show_caches()
