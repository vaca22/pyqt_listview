```angular2html
pip install pyinstaller
pyinstaller -F -w main.py
pip install pyinstaller==5.13.2
pip freeze > requirements.txt
git add .\requirements.txt -f

pip install -r requirements.txt

pyinstaller -F -w main.py --onefile --icon=output.ico --name="订单导出助手v2.3.1"
pyinstaller -F -w main.py --onefile --icon=output.ico --name="订单导出助手v2.3"

pyinstaller -F -w --add-data 'loading.gif;.' main.py --onefile --icon=output.ico --name="订单导出助手v2.4" --key wsmslgh
```