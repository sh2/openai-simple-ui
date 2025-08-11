#!/bin/bash

YYYYMMDD=$(date +%Y%m%d)

podman build --tag openai-simple-ui:${YYYYMMDD} .
