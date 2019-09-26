FROM python:3
ENV PYTHONUNBUFFERED 1
RUN adduser pyuser \
  && mkdir /app \
WORKDIR /app
COPY requirements.txt /app
RUN pip install --upgrade pip \
  && pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
COPY . .
RUN chmod +x app.py \
  && chmod -R pyuser:pyuser /app
USER pyuser
EXPOSE 5000
ENTRYPOINT ["python","app.py"]
