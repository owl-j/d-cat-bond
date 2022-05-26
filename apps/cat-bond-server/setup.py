from setuptools import find_packages, setup

PACKAGE_DIR = "src"

setup(
    name="cat-bond-server",
    packages=find_packages(where="src"),
    package_dir={"": PACKAGE_DIR},
    install_requires=[
        "gunicorn",
        "numpy",
        "flask",
        "flask-cors",
        "flask-socketio",
        "flask-jwt-extended",
        "flask-restful",
        "loguru",
        "PyJWT[crypto]",
        "requests",
        "bcrypt",
        "python-dotenv",
        "mysql-connector-python",
    ],
    extras_require={"dev": ["pytest", "tox", "black", "isort"]},
)
