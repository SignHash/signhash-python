import io
import pytest

from signhash import fetch_signers


@pytest.fixture
def public_key():
    return 'test-public-key'


def test_binary_signer_is_fetched(public_key):
    stream = io.StringIO('test content')

    signers = fetch_signers(stream)

    assert len(signers) > 0

    signer = signers[0]

    assert signer.verified is True
    assert signer.public_key == public_key
    assert signer.domain == 'signhash.com'
