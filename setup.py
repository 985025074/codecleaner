import setuptools 
setuptools.setup(
    name="codecleaner",
    version="0.0.1",
    packages=["codecleaner"],  # 显式指定包名
    entry_points={
        "console_scripts": [
            "codecleaner=codecleaner.main:main",
        ]
    },
)
