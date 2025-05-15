import cryo
import polars as pl

txs = cryo.collect('transactions', blocks=['latest'], rpc ='https://eth.merkle.io')
print(txs)