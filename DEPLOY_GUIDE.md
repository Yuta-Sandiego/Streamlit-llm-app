# Streamlit Community Cloud デプロイガイド

## 🚀 デプロイ手順

### 1. GitHubリポジトリの準備
- ✅ プロジェクトをGitHubにプッシュ済み
- ✅ `.env`ファイルは`.gitignore`で除外済み

### 2. Streamlit Community Cloudでのデプロイ

#### Step 1: アクセスとサインイン
1. https://share.streamlit.io/ にアクセス
2. GitHubアカウントでサインイン

#### Step 2: 新しいアプリを作成
1. 「New app」ボタンをクリック
2. 以下を設定：
   - **Repository**: `Yuta-Sandiego/streamlit-llm-app`
   - **Branch**: `main`
   - **Main file path**: `app.py`

#### Step 3: Secrets設定（重要）
1. **「Advanced settings」をクリック**
2. **「Secrets」セクションに以下をコピー&ペースト：**

```toml
[api_keys]
OPENAI_API_KEY = "sk-your-actual-openai-api-key-here"
```

⚠️ **重要**: `sk-your-actual-openai-api-key-here` の部分を実際のOpenAI APIキーに置き換えてください。

#### Step 4: デプロイ実行
1. 「Deploy!」ボタンをクリック
2. 数分でアプリがデプロイされます

### 3. デプロイ後の確認
- アプリが正常に起動することを確認
- 専門家選択機能が動作することを確認
- LLMからの応答が正常に表示されることを確認

## 🔧 デプロイ後の管理

### Secretsの更新方法
1. Streamlit Community Cloudのダッシュボードにアクセス
2. あなたのアプリを選択
3. 右上の「⚙️」（設定）ボタンをクリック
4. 左メニューの「Secrets」を選択
5. 設定を更新して「Save」

### アプリの再起動
- コードを更新してGitHubにプッシュすると自動的に再デプロイ
- 手動での再起動も可能（設定画面から）

## 🐛 トラブルシューティング

### よくあるエラーと解決方法

1. **「APIキーが設定されていません」エラー**
   - Streamlit Community Cloudの「Secrets」設定を確認
   - APIキーの形式が正しいか確認（`sk-`で始まる）
   - シークレット設定後にアプリを再起動

2. **「ModuleNotFoundError」エラー**
   - `requirements.txt`にすべての依存関係が含まれているか確認
   - 特に以下のパッケージが必要：
     - `streamlit`
     - `langchain-openai`
     - `langchain-core`
     - `python-dotenv`

3. **アプリが起動しない**
   - ログを確認してエラーの詳細を特定
   - ファイルパスが正しいか確認
   - ブランチ名が正しいか確認

## 🔐 セキュリティのポイント

### ✅ 正しい設定
- APIキーはStreamlit Community Cloudのシークレット機能で管理
- `.env`ファイルはGitHubにアップロードされない
- シークレット設定はプラットフォーム上でのみ行う

### ❌ やってはいけないこと
- APIキーをソースコードに直接書く
- `.env`ファイルをGitにコミットする
- パブリックリポジトリにAPIキーを含める

## 📝 更新手順

コードを更新する場合：
1. ローカルでコードを修正
2. `git add .`
3. `git commit -m "更新内容"`
4. `git push`
5. Streamlit Community Cloudが自動的に再デプロイ

## 🔗 参考リンク
- [Streamlit Community Cloud Documentation](https://docs.streamlit.io/streamlit-community-cloud)
- [Streamlit Secrets Management](https://docs.streamlit.io/streamlit-community-cloud/manage-your-app/secrets-management)