#!/bin/bash
# Use OpenSSL to read PEM file
openssl rsa \
  `# Do not re-print the contents of the file` \
  -noout \
  `# Set the input format to PEM` \
  -inform PEM \
  `# Select the input file` \
  -in privacy_enhanced_mail.pem \
  `# Display private key info, e.g. private exponent, modulus, etc.` \
  -text | \
  `# Extract private key` \
  grep -A18 private | \
  `# Do some cleanup` \
  tail -n18 | \
  tr -d '\n    ' | \
  tr -d ':' | \
  `# Change into a format we can use 'python -c' with (basically, just replace HEX with 'print(0xHEX)')` \
  sed 's/.*/print(0x&)/' | \
  `# Run that code as python (i.e. print out the converted bigint)` \
  xargs python3 -c