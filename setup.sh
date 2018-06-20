#!/usr/bin/env sh

DB_DIR=.db
SETTINGS_DIR=settings
MIGRATIONS_DIR=.db/migrations

upgrade_db() {
    flask db migrate -d ${MIGRATIONS_DIR}
    flask db upgrade -d ${MIGRATIONS_DIR}
}

create_db() {
    mkdir ${DB_DIR} 2>/dev/null
    flask db init -d ${MIGRATIONS_DIR}
    upgrade_db
}

copy_settings_examples() {
    cp examples/settings/* ${SETTINGS_DIR}/
}

# Copy settings from example
if [ ! -d ${SETTINGS_DIR} ]; then
    mkdir ${SETTINGS_DIR}
    copy_settings_examples
elif [ -z "$(ls -A ${SETTINGS_DIR})" ]; then
    copy_settings_examples
fi


# Create database if it doesn't exist
if [ ! -d ${DB_DIR}/ ] || [ -z "$(ls -A ${DB_DIR})" ]; then
    create_db
else
    upgrade_db
fi

