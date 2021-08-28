systemctl stop elguardia.service
cd ~/elguardiabot
git pull --rebase
systemctl start elguardia.service --no-block
