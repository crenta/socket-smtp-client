# SMTP Mail Client

A lightweight Python implementation of an SMTP client that sends emails using raw socket programming with TLS/SSL encryption.

## Overview

This project demonstrates a low-level understanding of email protocols by implementing an SMTP client from scratch using Python's `socket` library. The client establishes a secure connection with an SMTP server, authenticates using the AUTH LOGIN method, and sends emails following the SMTP protocol specifications.

## Features

- **Raw Socket Implementation**: Direct TCP connection to SMTP servers without high-level libraries
- **TLS/SSL Encryption**: Implements STARTTLS for secure communication
- **SMTP Authentication**: Base64-encoded authentication using AUTH LOGIN
- **RFC Compliant**: Follows SMTP protocol standards (RFC 5321, RFC 3207)
- **Full SMTP Transaction**: Demonstrates complete email sending workflow

## Technical Implementation

The client implements the following SMTP commands in sequence:

1. **EHLO** - Extended hello to identify client to server
2. **STARTTLS** - Upgrade connection to TLS encryption
3. **AUTH LOGIN** - Authenticate with Base64-encoded credentials
4. **MAIL FROM** - Specify sender email address
5. **RCPT TO** - Specify recipient email address
6. **DATA** - Send email headers and message body
7. **QUIT** - Close the connection

## Requirements

- Python 3.x
- Standard library modules: `socket`, `ssl`, `base64`

## Configuration

Update the following variables in the script:

```python
email = "your-email@example.com"
email_bytes = b"your-email@example.com"
password = b"your-app-password"
target_email = "recipient@example.com"
mailserver = ("smtp.server.com", 587)
```

**Note**: Use app-specific passwords for services like Yahoo, Gmail, etc., not your regular account password.

## Usage

Run the script:

```bash
python smtp_client.py
```

The client will output the server responses at each step of the SMTP transaction.

## Learning Outcomes

This project demonstrates:

- Understanding of network protocols and socket programming
- Knowledge of secure communication using TLS/SSL
- Implementation of authentication mechanisms
- Practical application of RFC specifications
- Email infrastructure and SMTP workflow

## References

- [RFC 3207 - SMTP Service Extension for Secure SMTP over TLS](https://datatracker.ietf.org/doc/html/rfc3207)
- [RFC 5321 - Simple Mail Transfer Protocol](https://datatracker.ietf.org/doc/html/rfc5321)
- [Python SSL Module Documentation](https://docs.python.org/3/library/ssl.html)

## Security Note

This is an educational project. In production environments, use established libraries like `smtplib` and never hardcode credentials in source code. Always use environment variables or secure credential management systems.

## License

This project is available for educational purposes.
