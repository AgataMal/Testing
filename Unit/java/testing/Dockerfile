FROM maven
RUN mkdir /tests 
COPY . /tests/
RUN chmod 777 /tests/
CMD mvn -f /tests/pom.xml test -B
