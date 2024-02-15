
# File Manipulator

`FileManipulator.py`は、ファイルの内容を逆転、コピー、複製、および文字列の置換を行うコマンドラインツールです。

## 機能

このスクリプトは以下の機能を提供します：

- **逆転**：ファイルの内容を逆にして新しいファイルに保存します。
- **コピー**：ファイルのコピーを作成し、指定したパスに保存します。
- **複製**：ファイルの内容を指定回数だけ複製し、元のファイルに上書き保存します。
- **文字列の置換**：ファイル内の特定の文字列を新しい文字列に置き換えます。

## 使い方

### 1. ファイルの内容を逆にする（reverse）

```
python FileManipulator.py reverse input.txt output.txt
```

### 2. ファイルのコピーを作成する（copy）

```
python FileManipulator.py copy original.txt copy.txt
```

### 3. ファイルの内容を複製する（duplicate-contents）

```
python FileManipulator.py duplicate-contents file.txt 3
```

### 4. ファイル内の文字列を置換する（replace-string）

```
python FileManipulator.py replace-string file.txt oldString newString
```

## 注意事項

- 実行する前に、対象となるファイルが存在することを確認してください。
- 出力ファイルは、コマンド実行により作成または上書きされますので、ご注意ください。
- パスにスペースが含まれる場合は、パスを引用符で囲んでください。