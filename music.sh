#!/bin/bash

echo "2-Zelda_and_Chill or 1-hack or 0-norm?"
read inp
if [[ "$inp" == "0" ]]; then
  open https://www.youtube.com/watch?v=TXm9C7UCWT4
elif [[ "$inp" == "1" ]]
then
  open https://www.youtube.com/watch?v=Z6dIdJX4ens
elif [[ "$inp" == "2" ]]
then
  open https://www.youtube.com/watch?v=oCaOSz13h_o
fi
