FROM python:3.6.6-alpine

MAINTAINER "github.com/j-000"

WORKDIR /budrun

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python"]

CMD ["server.py"]
