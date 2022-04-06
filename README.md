# Search Mail Bounce

## Create .Env
```sh
cp .env-example .env
```

## Run with docker-compose
```sh
 docker-compose up -d --build
```

## Or

### Create Environment
```sh
python3 -m venv venv
```

### Activate Environment
```sh
. venv/bin/activate
```

### Install Package
```sh
pip install -r requirements.txt
```

### Run
```sh
python3 main.py
```