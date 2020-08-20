def info():
    about = """
    This subpackage implements predefined PDES on graphs.

    Ref:
    https://elmoatazbill.users.greyc.fr/pub.html
    """
    print(about)

__all__ = [
        'pdeanisodiff',
        'pdeisodiff',
        'pdeinflapdiff',
        'pdemorphdilation',
        'pdemorpherosion',
        'info',
]
