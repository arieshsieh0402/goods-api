# goods-api

根據某題目寫的 api，主要是練習使用 jwt 驗證。
題目並未完全依據 RESTful API 風格，也未遵循 JSON:API 規範去定義每個 endpoints
的 request body 與 responses。但基本上我就先按照題目的定義來實作。

## 安裝所需套件

1. 我這邊將 [api](./api/) 與 [database](./database/) 分開不同的環境，因此分別使用各自的 requirements.txt 安裝所需套件

    ```shell
    $ pip install -r requirements.txt
    ```

## 設置 `config.json`

1. [api](./api/) 與 [database](./database/) 有各自的 `config.json`。內容參考 `config-example.json` 來做設定。記得把檔名改成 `config.json`。


## 透過 docker-compose 啟動容器

1. [database](./database/) 裡有 [docker-compose.yaml](./database/docker-compose.yaml) 檔供參考及運行。敏感參數另使用 `.env` 檔裡設置並傳入 docker-compose.yaml。
