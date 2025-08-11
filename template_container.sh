#!/bin/bash

podman run \
        --detach \
        --restart=always \
        --publish=8511:8501 \
        --env=OPENAI_API_KEY= \
        --name=openai-simple-ui \
        openai-simple-ui:20250101
