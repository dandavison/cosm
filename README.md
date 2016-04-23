Example `docopt` app with subcommand and bash tab completion.

```
$ python setup.py develop
$ . completion/bash/docopt-example
$ docopt-example subcommand_with  # <TAB>
subcommand_with_argument     subcommand_without_argument
$  docopt-example subcommand_with_argument  # <TAB>
thing1  thing2  thing3
```

Code taken from `docker-compose` and `docker`.
