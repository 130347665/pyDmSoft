# 一個使用Python封裝大漠插件的庫

這個模組是為了封裝大漠7.2213版本，並封裝了大漠插件的API，以便讓IDE都可以有代碼提示。

這些方法是從大漠插件DLL的倒出函數，生成的Python方法，因為目前沒有看到封裝比較完整python調用大漠的Libary，便有了這個。

## 安裝

```pip install pydmsoft```

## 功能
### 初始化
```
# 已在系統註冊大漠調用
dm = DM()
# 使用免註冊調用 只需要在第一次調用一次即可 其餘的可直接使用 dm=DM()
dm = DM(DmRegPath="path_to_dmreg.dll", DMPath="path_to_dm.dll")
```
## 使用範例
1. 註冊
   ```
   result = dm.Reg(code, Ver)
   print(result)
   ```

2. OCR 辨識
    ```
    result = dm.Ocr(0, 0, 100, 100, "ffffff-000000", 0.9)
    print(result)
    ```

3. 尋找文字
    ```
    result = dm.FindStr(0, 0, 500, 500, "example", "ffffff-000000", 0.9)
    print(result)
    ```

4. 截圖
    ```
    dm.Capture(0, 0, 200, 200, "screenshot.png")
    ```

5. 模擬鍵盤操作
    ```
    # 按下 'A' 鍵
    dm.KeyPress(65) 
    ```

## 注意事項
請確保大漠的dll檔案和註冊檔案路徑正確。另外，當使用免註冊調用時，需同時提供DmRegPath和DMPath。

## 開發者資訊

這是一個開源的封裝項目，歡迎貢獻及提供建議。