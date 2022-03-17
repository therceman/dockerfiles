# Leos 3.1.2

### Prerequisites

1) Linux System (Tested on Ubuntu 18.04.6 LTS)
2) Docker
3) Docker Compose

### Install & Run

```shell
make clean_run
```

**Note:** Wait until you will see msg `[INFO] Started Jetty Server` to start usage.

**Note:** P.S. You can cancel log session after this msg (CTRL+C)

### Usage

Open the browser and navigate to the LEOS web interface available at the following URL:

    http://localhost:8080/leos-pilot/ui

LEOS is pre-configured with these demo users:

    +-----------+-------+----------+--------+
    | NAME      | LOGIN | PASSWORD |ROLE    |
    +-----------+-------+----------+--------+
    | Demo User | demo  | demo     |Normal  |
    +-----------+-------+----------+--------+
    | John Doe  | john  | demo     |Normal  |
    +-----------+-------+----------+--------+
    | Jane Doe  | jane  | demo     |Support |
    +-----------+-------+----------+--------+
    | S Leo     | leos  | demo     |Support |
    +-----------+-------+----------+--------+

### Connect to container

```shell
make bash
```

### Logs

Show annotate service logs
```shell
make annotate_logs
```

Show user-repository service logs
```shell
make user-repository_logs
```

Show repository service logs
```shell
make repository_logs
```

Show leos service logs
```shell
make leos_logs
```

Show akn4euutil service logs
```shell
make akn4euutil_logs
```