FROM python
RUN pip install coverage pytest parameterized
RUN mkdir /tests 
COPY ./* /tests/

CMD cd /tests && coverage run -m pytest
