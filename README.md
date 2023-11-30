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

## VSCoe拡張機能
- [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
  Pythonでプログラミングするために必要なデバッグ機能やインテリセンスに加え、「Jupyter Notebook」をVSCodeから使えるようになります。
- [indent-rainbow](https://marketplace.visualstudio.com/items?itemName=oderwat.indent-rainbow)
  ソースコードのインデントの深さを色分けして表示します。ソースコードのインデントが重要な意味を持つPythonでは重宝する機能です。
- [vscode-icons](https://marketplace.visualstudio.com/items?itemName=vscode-icons-team.vscode-icons)
  VSCode上で表示するファイルアイコンのデザインを見た目で分かりやすいデザインにします。
- [autoDocstring](https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring)
  「ドキュメンテーション文字列(docstring)」を自動入力します。
  
