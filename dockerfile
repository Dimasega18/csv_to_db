FROM jenkins/jenkins:jdk17
USER root
RUN mkdir app
RUN apt-get update && apt-get install -y python3 python3-sqlalchemy python3-pandas
RUN apt-get clean
USER jenkins