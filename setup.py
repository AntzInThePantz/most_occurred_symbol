import os

from setuptools import setup

VERSION = "1"

CLASSIFIERS = [
    "Programming Language :: Python",
]

requires = [
    'psutil',
]

TESTS_REQUIRE = [
    "nose",
    "nose-cov",
]

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, "README.md")).read()
CHANGES = open(os.path.join(here, "CHANGES.txt")).read()

if __name__ == "__main__":
    setup(
        name='most_occurred_symbol',
        install_requires=requires,
        version=VERSION,
        tests_require=TESTS_REQUIRE,
        description="Most occured Symbols library and scripts.",
        long_description=README + "\n\n" +  CHANGES,
        classifiers=CLASSIFIERS,
        author="Andreas Rösch",
        author_email="roesch_andreas@gmx.net",
        entry_points = {
            "console_scripts": [
                "find-most-occurred-letter = most_occurred_symbol.__init__:main",
            ],
        }
    )
