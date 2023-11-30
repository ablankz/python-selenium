# python-selenium

## 仮想環境について
以下のコマンドでプロジェクト直下に仮想環境を作成する
``` sh
python -m venv virtual
```
以降、`pip install`などするときは以下のコマンドで仮想環境内でコマンドを実行すること。
``` sh
source ./virtual/bin/activate
```
仮想環境を抜けるには以下のコマンドを叩く。
``` sh
deactivate
```
さらに[requirements.txt](./requirements.txt)にて依存パッケージを指示しているため、新規インストールを行った場合、仮想環境内(プロジェクト直下であることを確認して)で以下のコマンドを実行する。
``` sh
pip freeze > requirements.txt
```
また、パッケージのインストールも以下のコマンドでまとめて行える。
``` sh
pip install -r requirements.txt
```
