FROM ubuntu:22.04

LABEL maintainer="earth87human@gmail.com"

# Let the container know that there is no tty
ENV DEBIAN_FRONTEND noninteractive

# Locales
ENV LANG C.UTF-8

# Set time zone
RUN apt-get update && apt-get install -y tzdata
ENV TZ Asia/Taipei
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Install system dependencies
RUN apt-get update && apt-get install -yq --no-install-recommends \
    curl \
    unzip \
    zip \
    software-properties-common \
    php8.1-bcmath \
    php8.1-cli \
    php8.1-curl \
    php8.1-fpm \
    php8.1-gd \
    php8.1-gmp \
    php8.1-intl \
    php8.1-mbstring \
    php8.1-mysql \
    php8.1-opcache \
    php8.1-readline \
    php8.1-soap \
    php8.1-xml \
    php8.1-zip \
    php8.1-imagick \
    php8.1-redis \
    nginx

# Install Composer
RUN curl -o /tmp/composer-setup.php https://getcomposer.org/installer \
  && curl -o /tmp/composer-setup.sig https://composer.github.io/installer.sig \
  && php -r "if (hash('SHA384', file_get_contents('/tmp/composer-setup.php')) !== trim(file_get_contents('/tmp/composer-setup.sig'))) { unlink('/tmp/composer-setup.php'); echo 'Invalid installer' . PHP_EOL; exit(1); }" \
  && php /tmp/composer-setup.php --no-ansi --install-dir=/usr/local/bin --filename=composer --version=2.6.5 \
  && rm -rf /tmp/*

# Cleanup
RUN apt-get autoremove --purge -y \
        software-properties-common \
    && apt-get -y clean \
    && rm -rf /var/lib/apt/lists/* /var/tmp/*

CMD service php8.1-fpm start && nginx -g 'daemon off;'
