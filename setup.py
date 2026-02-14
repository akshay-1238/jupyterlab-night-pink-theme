"""
Setup script for jupyterlab-night-pink-theme
"""
from pathlib import Path
from setuptools import setup

HERE = Path(__file__).parent.resolve()

# Get the package info from package.json
import json
with (HERE / "package.json").open() as f:
    package_json = json.load(f)

lab_path = (HERE / package_json["jupyterlab"]["outputDir"])

# Representative files that should exist after a successful build
ensured_targets = [
    str(lab_path / "package.json"),
    str(lab_path / "static/style.js")
]

labext_name = "jupyterlab-night-pink-theme"

data_files_spec = [
    ("share/jupyter/labextensions/%s" % labext_name, str(lab_path), "**"),
    ("share/jupyter/labextensions/%s" % labext_name, str(HERE), "install.json"),
]

long_description = (HERE / "README.md").read_text()

setup_args = dict(
    name=package_json["name"],
    version=package_json["version"],
    url=package_json["homepage"],
    author=package_json["author"]["name"],
    author_email=package_json["author"]["email"],
    description=package_json["description"],
    license=package_json["license"],
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=[],
    install_requires=[
        "jupyterlab>=4.0.0,<5",
    ],
    zip_safe=False,
    include_package_data=True,
    python_requires=">=3.8",
    platforms="Linux, Mac OS X, Windows",
    keywords=["Jupyter", "JupyterLab", "JupyterLab4"],
    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Framework :: Jupyter",
        "Framework :: Jupyter :: JupyterLab",
        "Framework :: Jupyter :: JupyterLab :: 4",
        "Framework :: Jupyter :: JupyterLab :: Extensions",
        "Framework :: Jupyter :: JupyterLab :: Extensions :: Prebuilt",
    ],
)

try:
    from jupyter_packaging import wrap_installers, npm_builder, get_data_files
    
    post_develop = npm_builder(
        build_cmd="install:extension", source_dir="src", build_dir=lab_path
    )
    setup_args["cmdclass"] = wrap_installers(post_develop=post_develop, ensured_targets=ensured_targets)
    setup_args["data_files"] = get_data_files(data_files_spec)
except ImportError:
    pass

if __name__ == "__main__":
    setup(**setup_args)
