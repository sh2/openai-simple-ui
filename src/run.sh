#!/bin/bash

exec streamlit run openai-simple-ui.py \
    --browser.gatherUsageStats=false \
    --server.baseUrlPath=/simple-openai \
    --server.address 10.0.2.100 \
    --server.port 8501
