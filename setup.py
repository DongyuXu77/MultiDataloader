from setuptools import setup, find_packages

setup(
    name = "MultiDataloader",
    version = "0.0.1",
    author = "Dongyu Xu",
    author_email = "xudongyu@bupt.edu.cn",
    description = "a toy package to test diff dataloader performance",
    packages = find_packages(
        exclude = ['*.md', 'test/*']
    )
)
