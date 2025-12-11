# CT-Engineering Beryllium

16.Sep.2025 - 17.Sep.2025

## Python String changer

The Step strings changer for Auto test feature files' steps

## Component; 構成ファイル
1. string-changer.py
2. logger.py
3. README.md
4. logs
5. config/old_string.py
6. config/new_string.py
7. config/start_path.py
8. config/list_path.py
9. config/target_list.csv

## How to Use; 使用方法
1. Input a 'file(s) name' to 'config/target_list.csv'; 文句を変える「対象ファイルの名前」を「config/target_list.csv」に入れる。
    - Example
        - scout-scan-type.feature
        - scout-detector-coverage.feature
        - axial-kv.feature
        - helical-kv.feature
        - ...
2. Input a 'diretory name in file(s)' to 'config/start_path.py'; 文句を変える対象ファイルが入ってる「フォルダの名前」を「config/start_path.py」に入れる。
    - Example
        - "../Squish-System/tests/srs/"

3. Input a 'file(s) name' to 'config/target_list.csv'; 文句を変える「対象ファイルの名前」を「config/target_list.csv」に入れる。
    - Example
        - "Scan Session using Service Generic Scan protocol in 'Service' protocol category"

4. Input a 'string(s) in file(s)' to 'config/old_string.py'; 変換前の文句（ファイルの中身に既に入ってる文句）を「config/old_string.py」に入れる。
    - Example
        - "Scan Session using Service Generic Scan protocol in 'Reference Service' protocol category"

5. execute the 'string_changer.py' script; 'string-changer.py'を実行する。
```shell
    python3 string-changer.py 
```
OR
```shell
    chmod +x string-changer.py
    starinfo-txt.py 
```

6. Check the files； 対象ファイルの中身を見てを結果を確認する。

### 💡It is different from real work thing.




