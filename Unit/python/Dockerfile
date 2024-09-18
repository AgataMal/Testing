FROM python
RUN pip install coverage pytest parameterized
RUN mkdir /tests 
COPY ./* /tests/
RUN chmod 777 -R /tests/

CMD cd /tests && coverage run -m pytest
