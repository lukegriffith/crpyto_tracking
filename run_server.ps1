

$env:FLASK_APP = (Get-ChildItem -Path $PSScriptRoot\main_api.py).FullName
flask run

