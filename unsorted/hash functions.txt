Hash Function- A function that can map data of any size onto data of a fixed size. Hash functions are:
1. Deterministic- The same input always results in the same output (useful for identification)
2. Uniform- All outputs are equally likely
3. One-Way- You cannot predict the input from the output
4. Comprehensive- Incorporates all available data
5. Continuity- outputs are non-similar

Hash Collision- when different inputs to a hash function produce the same hash
Cryptographic hashing minimizes collisions
90% of users use the 1000 most common passwords
Rainbow Table- Table of hashing functions and digests of common passwords
Salting- When random bits are added to a password prior to hashing. Repeated salting makes it more difficult to decrypt a password
