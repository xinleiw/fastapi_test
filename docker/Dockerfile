FROM hub.infervision.com/vendor/python:3.7.4-slim-stretch

WORKDIR /app

RUN sed -i s@/deb.debian.org/@/mirrors.tuna.tsinghua.edu.cn/@g /etc/apt/sources.list  && \
    sed -i s@/security.debian.org/@/mirrors.tuna.tsinghua.edu.cn/@g /etc/apt/sources.list

RUN pip install --upgrade pip -i https://mirrors.aliyun.com/pypi/simple/
RUN pip install poetry -i https://mirrors.aliyun.com/pypi/simple/

COPY poetry.lock pyproject.toml ./

RUN poetry config virtualenvs.create false && \
    poetry install --no-dev --no-interaction --no-ansi && \
    rm -rf /root/.cache/pip/ && \
    rm -rf poetry.lock pyproject.toml

COPY ./ ./

EXPOSE 9100

CMD ["uvicorn", "--host", "0.0.0.0", "--port", "9100", "main:app"]

