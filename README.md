# Meal Rating Site 

![Django](https://img.shields.io/badge/Framework-Django-green)
![VirtualEnv](https://img.shields.io/badge/Environment-virtualenv-yellow?logo=python&logoColor=white)
![TailwindCSS](https://img.shields.io/badge/Style-Tailwind_CSS-38B2AC?logo=tailwindcss&logoColor=white)


<br>

### Djangoで構築された、食事を記録・共有・評価できるレビューアプリ
### 写真投稿、コメント、星評価機能で、日常の食事体験をシェアしよう！

<br>

## ⭐ デモ動画

<br>

### 食事のレビューを投稿する流れを確認できるデモ動画

<br>

https://github.com/user-attachments/assets/f9f4e9d2-5579-40e8-b307-a562745fbbd4

<br>

## **📝 サービス紹介と導入ガイド**

- [サービスの特徴・開発の目的](#サービスの特徴・開発の目的)

- [セットアップ手順](#セットアップ手順)

- [基本的な使い方](#基本的な使い方)

<br>

## **🛠️ 技術構成**

- [システム全体の構成図](#システム全体の構成図)

- [使用技術](#使用技術)

- [クラス構成 と アーキテクチャ](#クラス構成とアーキテクチャ)

<br>

## **💡 開発の振り返りと展望**

- [設計上のこだわり](#設計上のこだわり)

- [苦労した点](#苦労した点)

- [追加予定の機能](#追加予定の機能)

<br>

## **📚 参考情報・ライセンス**

- [参考文献](#参考文献)

- [ライセンス情報](#ライセンス情報)

<br>

---

## <a id="サービスの特徴・開発の目的"></a> 📝 サービスの特徴・開発の目的

<br>

###  サービスの全体像

- このプロジェクトは、**食事のレビューを投稿してシェアできるサービス**です。

- ユーザーはログイン後、食事の写真とコメントを投稿したり、他の投稿に星評価を付けたりできます。


<br>

###  できること

<div style="height:8px;"></div>

- **食事投稿**  

  料理名、画像、国名、説明などを入力し、食事情報を投稿できます。

- **食事一覧の閲覧**
  
  投稿されたすべての食事が一覧で表示され、誰でも閲覧可能です。

- **星評価の投稿**  

  他のユーザーが投稿した食事に対して、0〜5の星評価をつけることができます。

- **ユーザー認証**

  サインアップ・ログイン機能により、ユーザー管理を実現しています。


<br>


###  作成のきっかけ

<div style="height:8px;"></div>

1. **課題意識**

   食事を記録・共有し、他人の投稿にも評価できる仕組みで食への関心を高めたいと考えた。
   
3. **解決アプローチ**

   Djangoで認証・投稿・星評価・一覧表示などを実装し、UIやバリデーションにも対応。
  
3. **得られた学び**

   Djangoの構造理解、フォームとモデルの連携、ログイン管理やテンプレート操作の習得。

<br>

---

## <a id="セットアップ手順"></a> 🚀 セットアップ手順

<br>

### 1. 前提条件

以下を事前にインストールしてください

- [Python 3.8以上](https://www.python.org/downloads/)

- [venv (仮想環境)]( https://docs.python.org/ja/3/library/venv.html)

- [Git](https://git-scm.com/)

  
<br>

### 2. リポジトリのクローン

以下のコマンドをターミナルで実行します

```bash
git@github.com:BackendExplorer/Meal-Rating-App.git
```
```bash
cd Online-Chat
```

<br>

### 3. 仮想環境の有効化

```bash
# macOS/Linux の場合
source venv/bin/activate
```

```bash
# Windows　の場合
venv\Scripts\activate
```

<br>

### 4. サーバの起動

```bash
cd Meal-Rating-App
```

```bash
python3 manage.py runserver
```

<br>

### 5. アプリにアクセス

ブラウザで http://127.0.0.1:8000/ を開く。

<br>

---

## <a id="基本的な使い方"></a>🧑‍💻 基本的な使い方

<br>

### 1. サインアップ・ログイン

<br>

- ウェブサイトにアクセスしたらまずユーザー登録をします。

- すでにアカウントがある場合は「ログイン」からサインインしてください。

<br>

<table>
  <tr>
    <td><img src="https://github.com/user-attachments/assets/581f936f-70e1-433f-b8cc-b34aad77120b" width="100%" alt="サインアップフォーム" /></td>
    <td><img src="https://github.com/user-attachments/assets/66f40d21-972a-44d5-899c-f1d119341a9c" width="100%" alt="ログインフォーム" /></td>
  </tr>
</table>

<br>

### 2. 投稿一覧の閲覧

<br>

<img width="655" alt="スクリーンショット 2025-05-20 5 35 02" src="https://github.com/user-attachments/assets/4ea9bb03-40b2-4619-9ad2-a6fc13e6df62" />

<br>

### 3. 投稿の手順

<br> 

https://github.com/user-attachments/assets/3541257d-17dd-4bba-95f5-1c85d1074ac7

<br>

### 4. レビューの手順

<br>

https://github.com/user-attachments/assets/6cb1dd35-6b2a-4860-bd59-21818d773dfb

<br>

