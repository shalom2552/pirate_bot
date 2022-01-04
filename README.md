# Pirate Bot
Pirate bot to mine your pirates points automatically

## Installation
1. install selenium


```bash
pip install -U selenium
```
2. install chrome driver
```bash
sudo apt update
sudo apt install google-chrom
sudo apt install chrome-driver-{your_version}
```
3. make a driver location varibale
```bash
export PATH=$PATH:/place/with/the/file
```
4. make a login file 'log.txt'
```bash
touch log.txt
echo "mail@mail.com, password" > lof.txt
```
5. run pyinstaller.py
```bash
python3 pyinstaller.py
```

## Description
We all know how tough it can be to return every now and then to go into a pirate raid.
Well, not anymore.
This bot will do it for you!
After logging into your account via the log.txt file, it will automatically navigate to the pirate building in your city.
It will then navigate to the pirate building and begin mining your points.
You can leave the bot running as long as you like since it will know when to raid again.
Enjoy!!

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[shalom2552](https://github.com/shalom2552)
