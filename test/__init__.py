def test_vars():
    """Returns env var names to update in testing.

    These values are updated with values prefixed as `TEST_`.
    See .env.sample.
    """
    return [
        'DOMAIN',
    ]
