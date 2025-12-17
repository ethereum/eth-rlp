Release Notes
=============

.. towncrier release notes start

eth-rlp v3.0.0-beta.1 (2025-12-17)
----------------------------------

Breaking Changes
~~~~~~~~~~~~~~~~

- Drop support for Python 3.8 and 3.9 (`#27 <https://github.com/ethereum/eth-rlp/issues/27>`__)


Features
~~~~~~~~

- Add support for pyrlp v5 and Python 3.14 (`#27 <https://github.com/ethereum/eth-rlp/issues/27>`__)


eth-rlp v2.2.0 (2025-02-04)
---------------------------

Features
~~~~~~~~

- Merge template, adding ``py313`` support and replacing ``bumpversion`` with ``bump-my-version``. (`#26 <https://github.com/ethereum/eth-rlp/issues/26>`__)


Internal Changes - for eth-rlp Contributors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Merge template, fixing docs CI, add nightly CI runs (`#24 <https://github.com/ethereum/eth-rlp/issues/24>`__)


eth-rlp v2.1.0 (2024-03-19)
---------------------------

Internal Changes - for eth-rlp Contributors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Bump to ``hexbytes>=1.2.0`` and add ``blocklint`` to linting (`#22 <https://github.com/ethereum/eth-rlp/issues/22>`__)


eth-rlp v2.0.0 (2024-03-04)
---------------------------

Breaking Changes
~~~~~~~~~~~~~~~~

- Bump ``hexbytes`` dependency to ``>=1.0.0`` (`#21 <https://github.com/ethereum/eth-rlp/issues/21>`__)


Features
~~~~~~~~

- Add Python 3.12 support (`#18 <https://github.com/ethereum/eth-rlp/issues/18>`__)


Internal Changes - for eth-rlp Contributors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Add windows-wheel CI job for py312, set both py311 and py312 to use latest patch version (`#20 <https://github.com/ethereum/eth-rlp/issues/20>`__)
- Add ``py.typed`` file, move misplaced newsfragment, correct py version pins for ``typing-extensions`` (`#21 <https://github.com/ethereum/eth-rlp/issues/21>`__)


eth-rlp v1.0.1 (2024-01-25)
---------------------------

Bugfixes
~~~~~~~~

- Add the missing ``typing_extensions`` module requirement for Python <= 3.11 (`#19 <https://github.com/ethereum/eth-rlp/issues/19>`__)


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
