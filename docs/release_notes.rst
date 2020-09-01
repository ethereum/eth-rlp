Release Notes
=============

.. towncrier release notes start

eth-rlp v0.2.0 (2020-09-01)
---------------------------

Features
~~~~~~~~

- Add support for pyrlp v2.0.0-alpha.1 (as long as you don't use pypy) (`#8 <https://github.com/ethereum/eth-rlp/issues/8>`__)


Deprecations and Removals
~~~~~~~~~~~~~~~~~~~~~~~~~

- Dropped py3.5 support (`#7 <https://github.com/ethereum/eth-rlp/issues/7>`__)


Miscellaneous changes
~~~~~~~~~~~~~~~~~~~~~

- Merge updates from the project template (`#7 <https://github.com/ethereum/eth-rlp/issues/7>`__)


v0.1.2
--------------

Released April 25, 2018

- Add :meth:`~eth_rlp.main.HashableRLP.as_dict` as a shim for joint v0/v1 compatibility

v0.1.1
--------------

Released April 25, 2018

- Add support for rlp version 1 (but still backwards-compatible with v0)

v0.1.0
--------------

Released Mar 1, 2018

- Marked stable
- Upgraded eth-utils and hexbytes to stable versions
- Add pypy3 support

v0.1.0-alpha.2
--------------

Released Jan 30, 2018

- First working version
- Some docs
- New basic tests, that pass

v0.1.0-alpha.1
--------------

- Launched repository, claimed names for pip, RTD, github, etc
