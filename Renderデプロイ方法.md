# 🚀 Renderへのデプロイ方法

## 📋 準備するもの
- GitHubアカウント
- Renderアカウント（無料：https://render.com/）
- 以下の3ファイル：
  - `server.py`
  - `restaurant_finder.html`
  - `requirements.txt`

## 🎯 デプロイ手順

### ステップ1: GitHubリポジトリを作成

1. **GitHubにログイン** → https://github.com/
2. **新しいリポジトリを作成**
   - 右上の「+」→「New repository」
   - Repository name: `gourmet-finder`（任意の名前でOK）
   - Public を選択
   - 「Create repository」をクリック

3. **ファイルをアップロード**
   - 「uploading an existing file」をクリック
   - `server.py`、`restaurant_finder.html`、`requirements.txt` の3ファイルをドラッグ＆ドロップ
   - 「Commit changes」をクリック

### ステップ2: Renderでデプロイ

1. **Renderにログイン** → https://render.com/
   - GitHubアカウントでサインアップ/ログイン

2. **新しいWebサービスを作成**
   - ダッシュボードで「New +」→「Web Service」をクリック
   - 「Connect a repository」で先ほど作成したGitHubリポジトリを選択
   - 「Connect」をクリック

3. **設定を入力**
   ```
   Name: gourmet-finder（任意の名前）
   Region: Singapore（日本に近いリージョン）
   Branch: main
   Runtime: Python 3
   Build Command: (空欄でOK)
   Start Command: python server.py
   ```

4. **プランを選択**
   - 「Free」を選択
   - 「Create Web Service」をクリック

5. **デプロイ完了を待つ**
   - 数分待つとデプロイ完了
   - 画面上部に表示されるURL（例：`https://gourmet-finder.onrender.com`）をコピー

### ステップ3: アプリにアクセス

ブラウザで以下にアクセス：
```
https://あなたのアプリ名.onrender.com/restaurant_finder.html
```

例：`https://gourmet-finder.onrender.com/restaurant_finder.html`

## ✨ 完成！

これでインターネット上のどこからでもアクセスできるようになりました！

## ⚠️ 重要な注意点

### 1. 無料プランの制限
- **15分間アクセスがないとスリープ状態になります**
- スリープ状態から復帰するには、アクセスすると自動的に起動（30秒〜1分かかる）
- 月750時間まで無料で利用可能

### 2. 初回アクセスが遅い
スリープ状態から復帰する際は、初回アクセスに30秒〜1分ほどかかります。
これは正常な動作です。少し待てば表示されます。

### 3. APIキーの扱い
- **APIキーはユーザーが各自入力する形式なので安全です**
- コードにAPIキーを直接書き込まないでください

## 🔄 アプリの更新方法

ファイルを修正したい場合：

1. **GitHubのリポジトリページへ**
2. **修正したいファイルをクリック**
3. **鉛筆アイコン（Edit）をクリック**
4. **ファイルを編集**
5. **「Commit changes」をクリック**

→ Renderが自動的に新しいバージョンをデプロイします！

## 💡 トラブルシューティング

### アクセスできない / 404エラー
- URLに `/restaurant_finder.html` が含まれているか確認
- 正しいURL例：`https://your-app.onrender.com/restaurant_finder.html`

### サーバーエラー
- Renderのダッシュボードで「Logs」を確認
- エラーメッセージが表示されます

### スリープから復帰しない
- 1分ほど待ってからブラウザをリフレッシュ
- それでもダメな場合は、Renderダッシュボードで「Manual Deploy」→「Clear build cache & deploy」

## 📱 スマホからもアクセス可能

デプロイが完了すれば、スマホのブラウザからも同じURLでアクセスできます！
外出先でもレストラン検索ができるようになります。

## 🎉 URLを短くしたい場合

1. **カスタムドメインを設定**（有料プランが必要）
2. **bit.lyなどの短縮URLサービスを使用**
   - https://bitly.com/
   - 長いRender URLを短縮URLに変換

## 🔐 セキュリティについて

- このアプリはユーザーがAPIキーを入力する形式なので安全です
- プロキシサーバーは単にCORS問題を回避するだけで、APIキーを保存しません
- すべての通信はHTTPSで暗号化されます

---

何か問題があれば、Renderのドキュメントも参考にしてください：
https://render.com/docs/web-services
