from setuptools import Extension, setup


try:
    from Cython.Build import cythonize

    extensions = cythonize(
        [Extension("leb128", ["leb128.pyx"])],
        force=True,
        emit_linenums=True,
    )

except ImportError:
    extensions = [
        Extension("leb128", ["leb128.c"]),
    ]


setup(
    name='cyleb128',
    ext_modules=extensions,
    version="0.1.2",
    packages=[],
    license="MIT",
    description="Fast LEB128 implementation in cython",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="http://github.com/mosquito/cyleb128",
    author="Dmitry Orlov",
    author_email="me@mosquito.su",
    provides=["leb128"],
    build_requires=["cython"],
    keywords=["python", "leb128", "cython"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Natural Language :: Russian",
        "Programming Language :: Cython",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Software Development :: Libraries",
        "Topic :: System",
        "Topic :: System :: Operating System",
    ],
    extras_require={
        "develop": ["pytest"],
    },
)
