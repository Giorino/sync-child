"""
Core module — Parent repository'nin temel işlevleri.

Bu dosya tüm child repository'lere sync edilecek core kodu temsil eder.
Child repo'lar bu kodu upstream olarak alır ve kendi özelleştirmelerini üzerine ekler.
"""


def get_version():
    """Return the current core version."""
    return "1.0.0"


def core_function():
    """Example core functionality shared across all child repos."""
    return "Hello from parent core!"

def new_feature():
    """A brand new feature from parent."""
    return "new feature v2"
