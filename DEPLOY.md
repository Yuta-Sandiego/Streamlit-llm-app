# Streamlit Community Cloud デプロイガイド

## 🚀 デプロイ手順

### 1. GitHubリポジトリの準備
- ✅ 既に完了：プロジェクトはGitHubにアップロード済み
- ✅ 既に完了：`.env`ファイルは`.gitignore`で除外済み

### 2. Streamlit Community Cloudでのデプロイ

1. **Streamlit Community Cloudにアクセス**
   - https://share.streamlit.io/ にアクセス
   - GitHubアカウントでサインイン

2. **新しいアプリを作成**
   - 「New app」をクリック
   - リポジトリ: `Yuta-Sandiego/streamlit-llm-app`
   - ブランチ: `main`
   - メインファイル: `app.py`

3. **シークレット設定（重要）**
   - デプロイ設定画面で「Advanced settings」をクリック
   - 「Secrets」セクションに以下を追加：

```toml
[api_keys]
OPENAI_API_KEY = "sk-your-actual-openai-api-key-here"
```

4. **デプロイ実行**
   - 「Deploy!」ボタンをクリック
   - 数分でアプリがデプロイされます

### 3. デプロイ後の確認
- アプリが正常に起動することを確認
- 専門家選択機能が動作することを確認
- LLMからの応答が正常に表示されることを確認

## 🔐 セキュリティのポイント

### ✅ 正しい設定
- `.env`ファイルはGitHubにアップロードされない
- APIキーはStreamlit Community Cloudのシークレット機能で安全に管理
- シークレット設定はプラットフォーム上でのみ行う

### ❌ やってはいけないこと
- `.env`ファイルをGitにコミットする
- APIキーをソースコードに直接書く
- パブリックリポジトリにAPIキーを含める

## 🛠️ トラブルシューティング

### よくある問題と解決方法

1. **「APIキーが設定されていません」エラー**
   - Streamlit Community Cloudの「Secrets」設定を確認
   - APIキーの形式が正しいか確認（`sk-`で始まる）

2. **アプリが起動しない**
   - `requirements.txt`にすべての依存関係が含まれているか確認
   - ログを確認してエラーの詳細を特定

3. **LLMの呼び出しエラー**
   - OpenAI APIキーが有効で残高があるか確認
   - ネットワーク接続の問題がないか確認

## 📝 更新手順

アプリを更新する場合：
1. ローカルでコードを修正
2. GitHubにプッシュ
3. Streamlit Community Cloudが自動的に再デプロイ

## 🔗 参考リンク
- [Streamlit Community Cloud Documentation](https://docs.streamlit.io/streamlit-community-cloud)
- [Streamlit Secrets Management](https://docs.streamlit.io/streamlit-community-cloud/manage-your-app/secrets-management)