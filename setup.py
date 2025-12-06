from setuptools import setup

APP_NAME = "pytube"
app = "download_3.py"
VERSION = "12.1.0"

OPTIONS = {
    'argv_emulation': True,  # Enables command-line-style args in GUI apps
}

setup(
    app=[app],                      # Your main Python script
    name=APP_NAME,                  # Name of your app
    version=VERSION,               # Optional: useful for packaging
    options={"py2app": OPTIONS},    # Options specific to py2app
    setup_requires=['py2app'],      # Ensures py2app is installed before setup runs
)