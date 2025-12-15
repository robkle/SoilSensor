#!/bin/bash

set -a
echo "Enter Postgresql/timescaleDb password: "
read POSTGRES_PASSWORD
set +a

docker compose up --build