# Source
I have followed and been inspired by [libevm Twitter broadcast](https://x.com/i/broadcasts/1rmxPonPrkVJN). Gread insite how to make use of cryo with contracts abi and function signatures and blockchain economics.


# Scope
We want to use cryo to query data from Ethereum mainnet

# Tools
- Python
- Cryo: check CryoInstall.md guide
- Jupyter Notebook

# What do we use in cryo and how
Cryo provides methods to retreives data from the blockchain with very fast response, avoiding iterations.

# Data we query 
## Uni-V2: USDC
From the Uniswap pool we get ETH/USDC price via tokens reserves

# UNI-V3: WBTC
In uni-V3 we cannot make use of get reserve to calc prices. Uni-V3 allows LP to provie liquidity on specif price range introducing the concentrated liquidity model, this is very differtn from UNI-V1 and V2 the liquidity had to be provided on the intire price range. 
The price range can be determined via 'ticks':

- UNI_V3 WBTC: 0xCBCdF9626bC03E24f779434178A73a0B4bad62eD
- WBTC: 0x2260FAC5E5542a773Aa44fBCfeDf7C193bc2C599

We look for:
```bash 
struct Slot0{...};
slot0 = Slot0({
    sqrtPriceX96: sqrtPriceX96,
    tick: tick,
    observationIndex: 0,
    observationCardinality: cardinality,
    observationCardinalityNext: cardinalityNext,
    feeProtocol: 0,
    unlocked: true
});
```
Add block Timestamp:
- Multicall3 function: getCurrentBlockTimestamp()
- Function Signature: 0x0f28c97d


