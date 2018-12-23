#!/bin/bash

. ../envs/bottlebank/bin/activate

trap 'kill -2 $(jobs -p)' INT TERM EXIT

gcloud beta emulators datastore start --no-legacy --data-dir=_data --project bottlebank --host-port "127.0.0.1:8585" &

$(gcloud beta emulators datastore env-init --data-dir=_data)

python
