import setuptools

setuptools.setup(
    name="streamlit_d3_line",
    version="0.2.0",
    author="Fanilo ANDRIANASOLO",
    author_email="andfanilo@gmail.com",
    description="Testing D3 in React hooks in Streamlit",
    long_description="",
    long_description_content_type="text/plain",
    url="https://github.com/vr-clarissa/streamlit-d3-demo",
    packages=setuptools.find_packages(where="./streamlit-d3-line"),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.6",
    install_requires=[
        "streamlit >= 0.63",
    ],
)
