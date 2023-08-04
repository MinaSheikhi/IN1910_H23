FROM ubuntu:focal

RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y \
    bison \
    ccache \
    cmake \
    curl \
    flex \
    ninja-build \
    g++ \
    gfortran \
    git \
    libpng-dev \
    pkg-config \
    software-properties-common \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN apt-get update \
    && add-apt-repository ppa:deadsnakes \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y \
    python3.10-dev \
    python3.10-venv \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set up a virtual environment
ENV PATH=/venv/bin:$PATH
RUN python3.10 -m venv /venv

RUN python -m pip install --no-cache-dir --upgrade pip \
    seaborn \
    sphinx \
    matplotlib \
    numpy \
    numba \
    scipy \
    line_profiler \
    pybind11 \
    cmake \
    jupyter \
    jupyter-book \
    sphinx_inline_tabs \
    black \
    flake8 \
    cython \
    pre-commit \
    ffmpeg \
    dask \
    pytest \
    pytest-cov \
    pandas \
    plotly
