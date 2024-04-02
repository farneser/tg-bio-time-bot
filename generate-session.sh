#!/bin/bash

if [ -f "./env" ]; then
  echo '"env" file found!'
  source "./env"
else
  echo 'Enter "API_ID"'
  read API_ID
  export API_ID=$API_ID
  echo "API_ID=$API_ID" > "./env"

  echo 'Enter "API_HASH"'
  read API_HASH
  export API_HASH=$API_HASH
  echo "API_HASH=$API_HASH" >> "./env"
fi

export API_ID=$API_ID
export API_HASH=$API_HASH

echo "Downloading dependencies"

python3 -m venv venv

. venv/bin/activate

pip install --no-cache-dir -r ./requirements.txt

python3 bot.py --session

echo 'Session created. Run "docker-compose up --build" to start bot'
unset API_ID
unset API_HASH
