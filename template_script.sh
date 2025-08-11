#!/bin/bash

export OPENAI_API_KEY=

streamlit run src/openai-simple-ui.py \
    --browser.gatherUsageStats=false
