FROM public.ecr.aws/docker/library/python:3.12-slim

WORKDIR /app
COPY pyproject.toml README.md LICENSE ./
COPY web ./web
COPY agent ./agent
COPY fixtures ./fixtures
COPY deploy ./deploy
RUN pip install --no-cache-dir .

EXPOSE 8080
CMD ["python", "-m", "deploy.runtime"]
