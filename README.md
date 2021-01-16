# common-passwords

With `commonpass.py` you can quickly generate a relatively short wordlist of common (weak) passwords for a target organisation and service. By default, about 300 passwords are returned based on common patterns (for example `<company><year>!`).

## Usage

```
> python3 commonpass.py -h

usage: commonpass.py [-h] [--min-length MIN_LENGTH] [--lang LANG] organisation service

Generate common weak passwords.

positional arguments:
  organisation          Organisation name
  service               Service name

optional arguments:
  -h, --help            show this help message and exit
  --min-length MIN_LENGTH
                        Minimum password length
  --lang LANG           Language code, "de" or "en"
```

## Example

```
> python3 commonpass.py acme email
acme
acme!
acme!!
acme2.0
acme123
acme123!
acme2020
acme2020!
acme2020!!
...
Email4Acme
Email4Acme!
Email4Acme!!
Email4Acme2.0
Email4Acme123
Email4Acme123!
...
Winter2020
Winter2020!
Winter2020!!
Winter2021
Winter2021!
Winter2021!!
```

## Installation

You only need Python 3. No additional dependencies necessary.

## For non-security people

If this tool generates any password that you are using on any real service, please consider your password very weak and change it immediately :-)

## Disclaimer

The tool is a helper script for password audits. Please use the generated wordlists only for authorized security assessments or learning challenges (like CTFs). Please do not use this tool for any illegal purposes.
