dots-matrix-bot
===============

dots-matrix-bot is the interface for
`dots-bot-api <https://gitlab.com/KKlochko/dots-bot-api/>`__ to have
access to `Dots Platform Clients API <https://docs.dots.live/>`__ using
matrix.

Setup
=====

-  setup `dots-bot-api <https://gitlab.com/KKlochko/dots-bot-api/>`__,
   before continue.

-  clone this repository.

-  create ``.env``. Example:

   .. code::

      USERNAME=@example:example.com
      PASSWORD=password
      SERVER=https://example.com

-  change the ``config.toml``: `more about allowlist and blocklist
   formats <https://simple-matrix-bot-lib.readthedocs.io/en/latest/examples.html#id2>`__
   Example:

   .. code:: toml

      [simplematrixbotlib.config]
      allowlist = []
      blocklist = []
      admin_id = '@admin:example.com'

-  check that dots-bot-api is accessible, if it works then you can
   continue.

-  change base url in ``src/config/dots_bot_api_config.py``: Example:

   .. code:: python

      _base_url = "https://dotsapi.server.com"

-  run ``sudo docker-compose up -d`` in the project folder.

-  run ``sudo docker ps`` to see that ``dots_matrix_bot`` is run.

-  Now you can add bot to your chat and run commands.

Template
========

dots-matrix-bot uses
`simplematrixbotlib\ template <https://github.com/foresle/simplematrixbotlib_template>`__.

Author
======

Kostiantyn Klochko (c) 2023

License
=======

Under the GNU Affero General Public License v3.0 or later.
