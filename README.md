# discord_cpu_status
cpu and gpu status in Discord Custom Status

>このプログラムはTOSに反しています。自己責任でどうぞ

## Run
requestsとpsutilをインストール

```
pip install requests psutil
```

GPUはNvidiaのみ対応

**token.txt**に特殊トークンをセット

## トークン取得方法

01.Discordで[Ctrl + Shift + i]で開発者ウィンドウを出す

02.上の**NetWork**タブを開く

03.Discordからカスタムステータスを設定する

04.Networkタブから [setting] という項目を探す

05.[setting] の中から Request Header を探し **authorization** の部分にあるトークンをコピー

06.トークンを token.txt に貼り付け保存
