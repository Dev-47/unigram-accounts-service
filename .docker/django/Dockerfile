FROM python:3.8-slim as base

RUN adduser --disabled-password --disabled-login unigram_accounts
USER unigram_accounts

WORKDIR /home/unigram_accounts/app

ENV PATH="/home/unigram_accounts/.local/bin:${PATH}"

COPY --chown=unigram_accounts:unigram_accounts requirements.txt requirements.txt

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install --user -r requirements.txt

COPY --chown=unigram_accounts:unigram_accounts . /home/unigram_accounts/app/
