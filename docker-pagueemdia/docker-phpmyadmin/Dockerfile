FROM phpmyadmin:latest

ENV UPLOAD_LIMIT 1G

COPY config.user.inc.php /etc/phpmyadmin/config.user.inc.php

RUN echo "upload_max_filesize = ${UPLOAD_LIMIT}" > /usr/local/etc/php/conf.d/uploads.ini && \
    echo "post_max_size = ${UPLOAD_LIMIT}" >> /usr/local/etc/php/conf.d/uploads.ini && \
    echo "memory_limit = ${UPLOAD_LIMIT}" >> /usr/local/etc/php/conf.d/uploads.ini

EXPOSE 80