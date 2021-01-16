import itertools
import argparse
from datetime import datetime

PREFIXES = ['', '+', '++']
SEPARATORS = ['.', '4']
SIMPLE_SUFFIXES = ['', '!', '!!']
EXTENDED_SUFFIXES = SIMPLE_SUFFIXES + ['2.0', '123', '123!']
YEAR = datetime.now().year
YEARS = ['', str(YEAR-1), str(YEAR)]
SEASONS = {
  'en': ['Spring', 'Summer', 'Autumn', 'Fall', 'Winter'],
  'de': ['Frühling', 'Fruehling', 'Sommer', 'Herbst', 'Winter']
}


def build_patterns(organisation, service, lang='en'):
    orgs = list(set(
        [organisation.title(), organisation.lower(), organisation]))
    services = list(set([service.title(), service.lower(), service]))
    lang_key = 'en' if lang not in SEASONS.keys() else lang

    return [
        [PREFIXES, orgs, YEARS, EXTENDED_SUFFIXES],
        [PREFIXES, services, SEPARATORS, orgs, EXTENDED_SUFFIXES],
        [SEASONS[lang_key], YEARS, SIMPLE_SUFFIXES]
    ]


def generate_passwords(patterns, min_length=None):
    out = []
    for pattern in patterns:
        product = list(itertools.product(*pattern))
        pattern_result = []
        for e in product:
            password = ''.join(e)
            if not min_length or len(password) >= min_length:
                pattern_result.append(password)

        out += pattern_result

    return out


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Generate common weak passwords.')
    parser.add_argument('organisation', type=str, help='Organisation name')
    parser.add_argument('service', type=str, help='Service name')
    parser.add_argument('--min-length', type=int,
                        help='Minimum password length', default=None)
    parser.add_argument('--lang', type=str,
                        help='Language code, "de" or "en"', default='en')
    args = parser.parse_args()

    patterns = build_patterns(args.organisation, args.service, args.lang)
    passwords = generate_passwords(patterns, args.min_length)
    print('\n'.join(passwords))
