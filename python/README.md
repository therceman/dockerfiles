# Python 3.10.3

Configured for Datasketch (https://github.com/ekzhu/datasketch)

### Setup

```shell
make python_build_and_run
```

### Test

Test default endpoint
```shell
curl localhost:8888 
```

Test datasketch endpoint
```shell
curl -X POST localhost:8888/test
```

### Logs

```shell
make python_log
```