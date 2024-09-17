FROM maven
RUN mkdir /tests 
COPY . /tests/
CMD mvn -f /tests/pom.xml test -B
