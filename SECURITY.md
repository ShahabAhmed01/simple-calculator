# Security Policy

## Supported versions

This project does not have a tagged release yet. Security fixes are applied to
the `main` branch. Once releases exist, this section will list the supported
versions.

## Reporting a vulnerability

Please report security issues privately through GitHub:

**https://github.com/ShahabAhmed01/simple-calculator/security/advisories/new**

If private vulnerability reporting is unavailable, open a minimal public issue
asking the maintainer for a private channel. Do not include exploit details,
credentials, or other sensitive information in a public issue.

Useful reports include:

- A description of the issue and its impact
- Steps to reproduce it
- The affected file or function
- A minimal proof of concept, if safe to share privately
- The Python version and operating system
- Any suggested fix

## Scope

Simple Calculator is a local desktop application. It does not use the network,
store credentials, or write user data to disk. Areas of interest include:

- Code execution or sandbox escape through the expression evaluator
- Denial of service through crafted expressions or resource exhaustion
- Unsafe handling of user input in the GUI or CLI
- Vulnerabilities in development or CI tooling

Out of scope: attacks that require access to the user's machine or account,
social engineering, and vulnerabilities in third-party software that the
project does not control.

## Response

Reports are reviewed on a best-effort basis. There is no guaranteed response
time or service-level agreement. Please allow time for a fix and coordinate
disclosure before publishing details.

## Safe configuration

The calculator has no API keys, accounts, or environment variables. Do not add
credentials to issues, pull requests, screenshots, or logs. If you believe a
credential has been committed, report it privately so it can be removed from
the current tree and rotated by its owner.
