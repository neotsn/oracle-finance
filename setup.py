from setuptools import setup

with open("README.md", "r", encoding="utf8") as fh:
    long_description = fh.read()

setup(
    name='the_oracle',
    version='0.1.2',
    description='🤖 Predict the stock market with AI 用AI预测股票市场',
    py_modules=['the_oracle'],
    package_dir={'': 'src'},
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/ssantoshp/Oracle',
    author="Santosh Passoubady",
    author_email="santoshpassoubady@gmail.com",
    license='MIT',
    install_requires=[
        'darts',
        'yfinance'
    ],
)
