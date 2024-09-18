FROM maven
RUN mkdir -p /tests /.m2/repository
COPY . /tests/
RUN chmod 777 /tests/
RUN chmod 777 /.m2/repository
CMD mvn -f /tests/pom.xml test -B
