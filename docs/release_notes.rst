Release Notes
=============

.. towncrier release notes start

eth-rlp v1.0.0 (2023-12-06)
---------------------------

Breaking Changes
~~~~~~~~~~~~~~~~

- Drop python 3.7 support (`#16 <https://github.com/ethereum/eth-rlp/issues/16>`__)


Features
~~~~~~~~

- Add python 3.11 support (`#16 <https://github.com/ethereum/eth-rlp/issues/16>`__)


Internal Changes - for eth-rlp Contributors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Merge updates from template, including use ``pre-commit`` for linting, and changing the name of the ``master`` branch to ``main`` (`#16 <https://github.com/ethereum/eth-rlp/issues/16>`__)


eth-rlp v0.3.0 (2022-01-19)
---------------------------
Eth_Rlp 0.3.0 (2022-01-19)
--------------------------

Features
~~~~~~~~

- Add support for python 3.8-3.10 (`#12 <https://github.com/ethereum/eth-rlp/issues/12>`__)
- Require eth-utils>=2.0,<3 (`#14 <https://github.com/ethereum/eth-rlp/issues/14>`__)


Deprecations and Removals
~~~~~~~~~~~~~~~~~~~~~~~~~

- Remove support for Python 3.6 (`#13 <https://github.com/ethereum/eth-rlp/issues/13>`__)


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
