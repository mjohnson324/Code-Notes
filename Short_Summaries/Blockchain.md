# Key Blockchain Terms
Blockchain- a distributed ledger, immutable database
Genesis Block- 1st block in a chain
Hub and Spoke- Design pattern for smart contracts

Proofs:
	Proof of Work (miner)- Guess a nonce correctly to extend the chain and gain $
	Proof of Stake (forger)- Gamble your $ for a chance to get more
	Zero-Knowledge Proof (prover)- Demonstrate knowledge of X without conveying any other information
Message Digest (blockchain)- 
Provenance- The origin/verifiability of something
	-Provenance is strong in blockchains due to immutability
Faucet- Provider of ether for test networks (check definition)

Big questions that cryptocurrency had to answer:
	1. Access control: how to handle authentication? (one answer: public key encryption)
	2. Availability and reliability: don't use servers to avoid data loss
	3. Security: avoid centralized servers to deincentivize theft
How to remove server? A gossip protocol!
	Gossip protocols are leaderless (all players equal), bootstrapped (peer to peer connections) and consistent (relay transactions)
Byzantine Fault: When an actor misbehaves by doing something arbitrary or malicious
	-Effective blockchains have BF tolerance.
Double Spend: When two actors receive the same payment
	-Timestamps are an unreliable mechanism for preventing a double spend
	-Blockchain is more effective for preventing this type of abuse
	-Stopping a double spend requires slowing down transactions, ordering them, and preventing their reorder
Blockchain Solves the Big Questions and prevents double spend by:
	1. Using sequences of puzzle solutions. Each input includes a hash from the previous block
	2. Use a choice rule to verify legitimacy (accept the blockchain fork with the most blocks)
	3. Collective processing power safeguards the blockchain from a loss of control
a. Identity (asymmetric encryption)
b. Networking (gossip protocol)
c. Consensus (proof of work, longest-chain rule, nodes re-validate each block)

-Nodes with data are connected by hash pointers
    Hash > Block (data e.g. transactions) > Blockchain
-Hashing is used for identification, not encryption
-Editing blocks is challenging because you must update all subsequent blocks for the edit to stick
-Reading data on the chain is free; writing new entries is not
-To control a chain you must own > 1/2 of its nodes (gain consensus)

Ethereum:
Smart Contract- Program on a node for handling transactions
	-Remember, contracts that are uploaded cannot be taken down
Gas (unit)- Work measurement
	-Gas unit not $; gwei Eth assigned to gas units to prioritize work
Limit- work requested over network
Price- Eth you auction up to get work done
Transaction cost = Price * Limit
	-A way of controlling network usage to prevent system overload.
	-Transaction costs determine what gets done first
	-Low gas limits lead to failures (lost Eth/failed transaction) if transactions take longer than estimated
	-High Limits could mean lost $$ 

IPFS: Interplanetary File System
A distributed file storage system
