#!/bin/bash

API_KEY=
SECRET_KEY=
EMQX_DASHBOARD_BASE_URL=http://localhost:18083

# Create authenticator
curl -X POST -u ${API_KEY}:${SECRET_KEY} \
     -H 'Content-Type: application/json' \
     ${EMQX_DASHBOARD_BASE_URL}/api/v5/authentication \
     --data '{
               "mechanism":"password_based",
               "backend":"built_in_database",
               "password_hash_algorithm":{
                 "name":"sha256",
                 "salt_position":"suffix"
               },
               "user_id_type":"username"
             }'

# Import users into authenticator
curl -X POST -u ${API_KEY}:${SECRET_KEY} \
     -H 'Content-Type: application/json' \
     ${EMQX_DASHBOARD_BASE_URL}/api/v5/authentication/password_based:built_in_database/import_users?type=plain \
     --data '[
               {
                 "is_superuser": true,
                 "password": "admin",
                 "user_id": "admin"
               },
               {
                 "is_superuser": false,
                 "password": "user1",
                 "user_id": "user1"
               },
               {
                 "is_superuser": false,
                 "password": "user2",
                 "user_id": "user2"
               }
             ]'

# Create a new authorization source
curl -X POST -u ${API_KEY}:${SECRET_KEY} \
     -H 'Content-Type: application/json' \
     ${EMQX_DASHBOARD_BASE_URL}/api/v5/authorization/sources \
     --data '{
               "type": "built_in_database",
               "enable": true
             }'

# Create the list of rules for All Users
curl -X POST -u ${API_KEY}:${SECRET_KEY} \
     -H 'Content-Type: application/json' \
     ${EMQX_DASHBOARD_BASE_URL}/api/v5/authorization/sources/built_in_database/rules/all \
     --data '{
               "rules": [
                 {
                   "action": "subscribe",
                   "topic": "user/${client_id}",
                   "permission": "allow"
                 },
                 {
                   "action": "subscribe",
                   "topic": "user/${username}",
                   "permission": "allow"
                 },
                 {
                   "action": "subscribe",
                   "topic": "#",
                   "permission": "deny"
                 }
               ]
             }'
