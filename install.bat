timeout /t 20
echo Installing required Python packages...
pip install flask flask_login flask-sqlalchemy paho-mqtt

echo Cloning the GitHub repository...
git clone https://github.com/clre20/Earthquake-power-system-2024-Topics.git

echo Installation and download complete!
pause
