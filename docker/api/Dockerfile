FROM python:3.10.2-slim-buster AS builder

WORKDIR /app

# Install system dependencies
RUN apt-get update \
    && apt-get -y install netcat \
    && apt-get clean

# ignore 'Running pip as the root user...' warning
ENV PIP_ROOT_USER_ACTION=ignore

# update pip
RUN pip install --upgrade pip

# install poetry
ENV POETRY_VERSION=1.5.1
RUN pip install "poetry==$POETRY_VERSION"

# copy application
COPY ["pyproject.toml", "poetry.lock", "README.md", "./"]
COPY ["src/", "src/"]

# build wheel
RUN poetry build --format wheel

FROM builder as production

# expose port
EXPOSE 80

# copy the wheel from the build stage
COPY --from=builder /app/dist/*.whl /app/

# install package
RUN pip install /app/*.whl

COPY docker/api/start-dev.sh /app/docker/api/start-dev.sh
RUN chmod +x /app/docker/api/start-dev.sh

ENTRYPOINT /app/docker/api/start-dev.sh