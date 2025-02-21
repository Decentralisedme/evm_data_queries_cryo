'''
Simple Manual Pool Pring calcualtion
''' 

# UNI-V2: USDC

usdc_bal = 21790133153119           # tok_0
eth_bal = 7802798107670332036790    # tok_1
usdc_dec=6
eth_dec=18

# Get the eth/USDC Price 
# 1 ETH = x USDC

def tok_0_tok_1_price_UniV2(tok_0_bal, tok_1_bal):
    tok1_tok0_quote = tok_0_bal / tok_1_bal * 1e12
    return tok1_tok0_quote 

def tok_1_tok_0_price_UniV2(tok_1_bal, tok_0_bal):
    tok0_tok1_quote = tok_1_bal / tok_0_bal / 1e12
    return tok0_tok1_quote

price_tok0_tok1 = tok_0_tok_1_price_UniV2(usdc_bal,eth_bal)
print(f"ETH/USDC: {price_tok0_tok1}")
price_tok1_tok0 = tok_1_tok_0_price_UniV2(eth_bal,usdc_bal)
print(f"USDC/ETH: {price_tok1_tok0}")

# UNI-V3: USDC