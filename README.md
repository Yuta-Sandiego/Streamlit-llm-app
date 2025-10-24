# 🧠 専門家モード付き LLM チャットアプリ

LangChainとStreamlitを使用した、専門家の視点でLLMが応答するチャットアプリです。

## 🚀 機能

- **専門家モード選択**: 経済アナリスト、ソフトウェアエンジニア、心理カウンセラーの3つの専門家から選択可能
- **LangChain統合**: ChatOpenAIを使用してLLMと連携
- **安全なAPIキー管理**: Streamlitのシークレット機能でAPIキーを安全に管理
- **ユーザーフレンドリーUI**: 直感的なStreamlitインターフェース

## 📋 必要要件

- Python 3.11+
- OpenAI APIキー
- インターネット接続

## 🛠️ セットアップ

### 1. 仮想環境の設定

```bash
# 仮想環境をアクティブ化（Windows）
.\env\Scripts\activate.bat

# または PowerShell
.\env\Scripts\Activate.ps1
```

### 2. 依存関係のインストール

```bash
pip install -r requirements.txt
```

### 3. APIキーの設定

1. `.streamlit/secrets.toml` ファイルを開きます
2. 以下の部分を実際のOpenAI APIキーに置き換えます：

```toml
[api_keys]
OPENAI_API_KEY = "sk-your-actual-openai-api-key-here"
```

⚠️ **重要**: 実際のAPIキーを設定してください。このファイルはGitにコミットされません。

### 4. アプリの起動

```bash
streamlit run app.py
```

## 🎯 使用方法

1. ブラウザで http://localhost:8501 にアクセス
2. 専門家の種類をラジオボタンから選択
3. 質問を入力欄に記入
4. 「送信」ボタンをクリック
5. 選択した専門家の視点でLLMが回答を生成

## 🔒 セキュリティ

- APIキーはStreamlitのシークレット機能で管理
- `.streamlit/secrets.toml` は `.gitignore` に含まれており、Gitにコミットされません
- 実行時のエラーハンドリングでAPIキーの漏洩を防止

## 📁 ファイル構造

```
Streamlit-llm-app/
├── app.py                    # メインアプリケーション
├── requirements.txt          # Python依存関係
├── .streamlit/
│   └── secrets.toml         # APIキー設定（Git除外）
├── .gitignore               # Git除外設定
└── README.md               # このファイル
```

## 🐛 トラブルシューティング

### APIキーエラー
- `.streamlit/secrets.toml` ファイルが存在するか確認
- APIキーが正しく設定されているか確認
- OpenAI APIキーが有効で残高があるか確認

### モジュールエラー
- 正しい仮想環境がアクティブ化されているか確認
- `pip install -r requirements.txt` で依存関係を再インストール

### アプリが起動しない
- ポート8501が使用中でないか確認
- Streamlitの最新版を使用しているか確認

## 📝 ライセンス

このプロジェクトはMITライセンスの下で公開されています。

## 🤝 貢献

プルリクエストや課題の報告を歓迎します。