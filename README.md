# Pirate Bot for Ikariam
We all know how tough it can be to return every now and then to go into a pirate raid in Ikariam game.
Well, not anymore.
This bot will do it for you!
After logging into your account via the log.txt file, it will automatically navigate to the pirate building in your city.
It will then navigate to the pirate building and begin mining your points.
You can leave the bot running as long as you like since it will know when to raid again.
Additionally, it can generate your current score and append it to the CSV file for analysis.
Enjoy!!

## Installation
1. Install selenium


```bash
sudo apt-get -y install python3 python3-pip
pip install -U selenium
```
2. Install chrome driver
```bash
sudo apt update
sudo apt install google-chrome
sudo apt install chrome-driver-{your_version}
```
3. Create a driver location path varibale
```bash
export PATH=$PATH:/place/with/the/file
```
4. Create a login file 'log.txt'
```bash
touch log.txt
echo "mail@mail.com, password" > log.txt
```
5. Run pyinstaller.py
```bash
python3 pyinstaller.py
```


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[shalom2552](https://github.com/shalom2552)
