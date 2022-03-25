FROM python:3.10.3-slim

RUN adduser --disabled-password --gecos "" myuser
USER myuser
WORKDIR /home/myuser

ENV PATH="/home/myuser/.local/bin:${PATH}"

RUN pip install --user --upgrade pip

COPY --chown=myuser:myuser app/requirements.txt requirements.txt
RUN pip install --user -r requirements.txt

COPY --chown=myuser:myuser ./app .

# Run the executable
CMD ["python", "./src/app.py"]