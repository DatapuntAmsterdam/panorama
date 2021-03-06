#!/bin/sh

set -e
set -u

DIR="$(dirname $0)"

dc() {
	docker-compose -p panorama -f ${DIR}/docker-compose.yml $*
}

echo "Removing any previous backups"
rm -rf ${DIR}/backups
mkdir -p ${DIR}/backups

echo "Building dockers"
dc down
dc pull
dc build

echo "Starting and migrating db"
dc up -d database
dc run importer /deploy/docker-wait.sh
dc run importer /deploy/docker-migrate.sh

echo "Print counts"
docker-compose -p panorama -f ${DIR}/docker-compose.yml exec -T database psql -U panorama -c 'select status, count(*) from panoramas_panorama group by 1'

echo "Importing data"
dc run --rm importer

echo "Print counts"
docker-compose -p panorama -f ${DIR}/docker-compose.yml exec -T database psql -U panorama -c 'select status, count(*) from panoramas_panorama group by 1'

echo "Running backups"
dc exec -T database backup-db.sh panorama

echo "Done"
