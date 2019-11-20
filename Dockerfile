ARG BASE_IMAGE
FROM ${BASE_IMAGE}

CMD env FLASK_APP=app FLASK_ENV=development flask run