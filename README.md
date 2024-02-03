# WhichSystem
Identify Operating System Using TTL Value And Ping

# Set up
First clone the repository.
```
git clone https://github.com/Sh4dowX404Unknown/WhichSystem.git
```
Next we can configure it in two ways:
## Automated set up
Enter the cloned folder and run the automated-setup.sh
```
cd WhichSystem
bash automated-setup.sh
```
To use the script, as it is located in the local path /usr/local/bin you just have to use the following command:
```
whichsystem.py <ip_address>
```

## Manual set up
Enter the cloned folder and give execution permissions to the file 
```
cd WhichSystem
sudo chmod +x whichsystem.py
```
Now you could use the script like this:
```
python3 whichsystem.py <ip_address>
```
If you want to set the script to the local path, do the following:
```
sudo mv whichsystem.py /usr/local/bin
sudo chmod +x /usr/local/bin/whichsystem.py
```
To use the script, do the same as in the automated set up section
```
whichsystem.py <ip_address>
```
