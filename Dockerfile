FROM ethereum/client-go:v1.10.1

ARG ACCOUNT_PASSWORD

COPY genesis_files/genesis_pow.json /tmp

RUN geth init /tmp/genesis_pow.json \
    && rm -f ~/.ethereum/geth/nodekey \
    && echo ${ACCOUNT_PASSWORD} > /tmp/password \
    && geth account new --password /tmp/password \
    && rm -f /tmp/password

ENTRYPOINT ["geth"]