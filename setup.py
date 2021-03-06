import setuptools
import re

with open("README.md", "r") as fh:
    long_description = fh.read()


def load_reqs(filename):
    with open(filename) as reqs_file:
        return [
            re.sub('==', '>=', line) for line in reqs_file.readlines()
            if not re.match('\s*#', line)
        ]


requirements = load_reqs('requirements.txt')

setuptools.setup(
    name="sw4iot-cli",
    version="0.0.1",
    author="SOFTWAY4IoT",
    author_email="softway4iot@gmail.com",
    description="Etcd of SOFTWAY4IoT",
    license="Apache Software License",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sw4iot/sw4iot-cli",
    install_requires=requirements,
    packages=[
        'sw4iot_cli'
    ],
    package_dir={
        'sw4iot_cli': 'sw4iot_cli'
    },
    keywords='sw4iot-etcd',
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: Apache Software License',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        "Operating System :: OS Independent",
        'Programming Language :: Python :: 2.7',
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
    ]
)
