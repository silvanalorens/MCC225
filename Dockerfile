FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PORT=8899 \
    HF_HUB_ETAG_TIMEOUT=60 \
    HF_HUB_DOWNLOAD_TIMEOUT=120

ARG INSTALL_OPCIONAL=true
ARG TORCH_FLAVOR=cu124

WORKDIR /workspace

RUN apt-get update && apt-get install -y --no-install-recommends \
    bash \
    bash-completion \
    build-essential \
    curl \
    git \
    wget \
    tini \
    less \
    nano \
    vim \
    tree \
    procps \
    ripgrep \
    fd-find \
    fzf \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender1 \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*

COPY requirements-base.txt requirements-opcional.txt ./

RUN python -m pip install --upgrade pip setuptools wheel && \
    python -m pip install -r requirements-base.txt && \
    python -m pip install --index-url https://download.pytorch.org/whl/${TORCH_FLAVOR} \
      torch==2.4.1 torchvision==0.19.1 torchaudio==2.4.1 && \
    if [ "$INSTALL_OPCIONAL" = "true" ]; then \
      python -m pip install -r requirements-opcional.txt; \
    fi && \
    python -m pip install "httpx<0.28"

RUN python -m nltk.downloader punkt stopwords wordnet omw-1.4 averaged_perceptron_tagger && \
    python -m spacy download es_core_news_sm

RUN printf '%s\n' \
    'if [ -f /usr/share/bash-completion/bash_completion ]; then' \
    '  . /usr/share/bash-completion/bash_completion' \
    'fi' \
    '' \
    'alias ll="ls -alF"' \
    'alias la="ls -A"' \
    'alias l="ls -CF"' \
    >> /etc/bash.bashrc && \
    printf '%s\n' \
    'set completion-ignore-case on' \
    'set show-all-if-ambiguous on' \
    'set mark-symlinked-directories on' \
    >> /etc/inputrc

EXPOSE 8899

ENTRYPOINT ["/usr/bin/tini", "--"]

CMD ["sh", "-c", "jupyter lab --ip=0.0.0.0 --port=${PORT} --no-browser --allow-root --ServerApp.root_dir=/workspace"]
