"""
App module — Child repository'ye özel uygulama kodu.

Bu dosya child repo'ya özeldir ve parent repo'da bulunmaz.
Upstream sync sırasında conflict oluşmaz çünkü parent'ta karşılığı yoktur.
"""

from core import core_function, get_version


def main():
    """Child-specific application entry point."""
    print(f"Core version: {get_version()}")
    print(core_function())
    print("Child-specific customization active!")


if __name__ == "__main__":
    main()
