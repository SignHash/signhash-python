from typing import NamedTuple


class Signer(NamedTuple):
    verified: bool
    domain: str
    public_key: str


def fetch_signers(stream):
    return [Signer(
        verified=True,
        domain='signhash.com',
        public_key='test-public-key',
    )]
