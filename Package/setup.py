from setuptools import setup,find_packages

setup(
        ### 包与作者信息
        name = 'dashare',
        version = '0.1',
        author = 'shihua',
        author_email = "hua.shi@meritech-data.com",
        python_requires = ">=3.9.12",
        license = "MIT",

        ### 源码与依赖
        packages = find_packages(),
        include_package_data = True,
        description = 'DaShare is a dataapi python sdk with client and service',
        # install_requires = ['click','fastapi','pandas','rich','PyJWT'],

        ### 包接入点，命令行索引
        entry_points = {
            'console_scripts': [
                'dasharectl = dashare.cli:dashare'
            ]
        }      
)