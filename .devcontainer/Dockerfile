FROM mcr.microsoft.com/devcontainers/base:2.1.8-debian13

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-sphinx

# sphinx needs is not in apt-get, so we install it with pip.
# Debian prevents installing pip packages in the system pip,
# so we need to use --break-system-packages to install it in the system python.
# sphinx needs is an established package and hopefully we won't break anything this way.
RUN pip3 install --break-system-packages sphinx-needs
