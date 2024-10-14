FROM jenkins/jenkins:jdk17
USER root
RUN apt-get update && apt-get install -y python3 python3-sqlalchemy python3-pandas python3-psycopg2
RUN apt-get clean
USER jenkins