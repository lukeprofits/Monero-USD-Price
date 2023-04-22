from setuptools import setup

setup(
    name='monero_usd_price',
    version='1.0.0',
    author="Luke Profits",
    description="Monero-USD-Price is an easy way to get the current median or average price of Monero (median is recommended over average, because it less sensitive to outliers.)",
    url="https://github.com/lukeprofits/Monero-USD-Price",
    packages=['monero_usd_price'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['requests']
)
