# Authentication Strategies

Credential Stuffing: Using the same password across different websites
Phishing: Fooling people into giving their information with phony fronts

Usability and security are in conflict

## Authentication Factors

1. Knowledge (passwords, etc.)
2. Possession (cell phones, etc.)
3. Inherence (fingerprints, etc.)

A debit card is an example of TFA (pin is knowledge, card is possession)

## Types

1. SMS - better than nothing
   - Easy to use but insecure
2. Soft Token - time-based one-time passwords
   - Usable offline, an open standard and symmetric keys but requires an app, and the secret key must be kept safe
3. Push Authentication - device notifications
   - Asymmetric key cryptography and denial is easy, but is it too simple?
4. Webauthn
   - Safe, open and phishing-resistant, but how do you manage cost and availability?