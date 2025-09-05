# Meal Review App


![Django](https://img.shields.io/badge/Framework-Django-green)
![VirtualEnv](https://img.shields.io/badge/Environment-virtualenv-yellow?logo=python&logoColor=white)
![TailwindCSS](https://img.shields.io/badge/Style-Tailwind_CSS-38B2AC?logo=tailwindcss&logoColor=white)


<br>

### Django製・食事レビュー共有アプリ
### 写真投稿・コメント・星評価で日常の食体験を記録＆シェア

<br>

## ⭐ デモ動画

<br>

### 食事のレビューを投稿する流れを確認できるデモ動画

<br>

![Image](https://github.com/user-attachments/assets/f17c8762-7242-4cc2-92d8-93762df1a333)

<br>

## **📝 サービス紹介と導入ガイド**

- [サービスの特徴・開発の目的](#サービスの特徴・開発の目的)

- [セットアップ手順](#セットアップ手順)

- [基本的な使い方](#基本的な使い方)

<br>

## **🛠️ 技術構成**

- [システム全体の構成図](#システム全体の構成図)

- [使用技術](#使用技術)


<br>

## **💡 開発の振り返りと展望**

- [設計上のこだわり](#設計上のこだわり)

- [苦労した点](#苦労した点)

- [追加予定の機能](#追加予定の機能)

<br>

## **📚 出典・ライセンス**

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

### 3. 仮想環境の起動

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
    <td><img width="533" height="427" alt="Image" src="https://github.com/user-attachments/assets/dc9ec02c-db7e-4115-ba2a-b255186cb9ee" />
</td>
    <td><img width="533" height="398" alt="Image" src="https://github.com/user-attachments/assets/67b689af-3685-4ec9-bf9d-63305ca7714f" />
</td>
  </tr>
</table>

<br>

### 2. 投稿一覧の閲覧

<br>

<img width="531" height="227" alt="Image" src="https://github.com/user-attachments/assets/68d5c754-49e2-4797-89d0-8dac52a59c3f" />

<br>

### 3. 投稿の手順

<br> 

![Image](https://github.com/user-attachments/assets/09617f11-0377-4eda-8a8f-deca0b9f17f5)

<br>

### 4. レビューの手順

<br>

![Image](https://github.com/user-attachments/assets/a5236d0c-97e6-449b-9660-4453029bb160)


<br>

---

## <a id="システム全体の構成図"></a>⚙️ システム全体の構成図

<br>

<img width="900" alt="スクリーンショット 2025-05-20 6 18 47" src="https://github.com/user-attachments/assets/511381b4-674b-4c58-a6fd-8a0f6afcdccb" />

<br>

<img width="532" height="390" alt="Image" src="https://github.com/user-attachments/assets/1faf76bf-30de-4c33-8d8b-07c9fc8c6c14" />

<br>

---

## <a id="使用技術"></a>🧰 使用技術

<br>

### 1. 技術選定の理由

- **`Django`**

  認証やDB操作が充実しており、効率的なWeb開発が可能なため。

- **`venv`**

  依存関係をプロジェクトごとに安全に管理できるため。
 
- **`Tailwind`**

  柔軟かつ効率的にUIをデザインできるため

<br>

### 2. 技術スタックと 開発環境 の全体像

<br>

| カテゴリ         | 採用技術 と 使用ツール                                                                                               |
|------------------|---------------------------------------------------------------------------------------------------------------------|
| 開発言語         | ![Python](https://img.shields.io/badge/Python-3.8-blue) <br> DjangoフレームワークによるWebアプリ構築 |
| フレームワーク   | ![Django](https://img.shields.io/badge/Framework-Django-green) <br> 管理機能・認証・ORMなどを包括的に提供 |
| スタイリング     | ![Tailwind CSS](https://img.shields.io/badge/CSS-Tailwind_CSS-blue) <br> ウェブサイトの装飾に使用 |
| 仮想環境         | ![venv](https://img.shields.io/badge/Env-venv-lightgrey) <br> 依存関係を安全に管理するためのPython標準仮想環境 |
| 開発環境         | ![macOS](https://img.shields.io/badge/OS-macOS-lightgrey)&nbsp;&nbsp;&nbsp;&nbsp;![VSCode](https://img.shields.io/badge/Editor-VSCode-blue) |
| バージョン管理   | ![Git](https://img.shields.io/badge/VersionControl-Git-orange)&nbsp;&nbsp;&nbsp;&nbsp;![GitHub](https://img.shields.io/badge/Repo-GitHub-black) |
| ドキュメント・図 | ![Mermaid](https://img.shields.io/badge/Diagram-Mermaid-green)&nbsp;&nbsp;&nbsp;&nbsp;![LaTeX](https://img.shields.io/badge/Doc-LaTeX-9cf) |


<br>

---

## <a id="設計上のこだわり"></a>🌟 設計上のこだわり

<br>

<ul>
  <li>
    <h3>シンプルかつ直感的なUI設計</h3>
    <p>初めてのユーザーでも直感的に使えるよう、投稿や評価もワンクリックで完結できるようにしました。</p>
  </li>
</ul>

<br>

<ul>
  <li>
    <h3>機能ごとのアプリ分割による保守性向上</h3>
    <p>Djangoの各アプリ（例：reviews、accounts）を機能ごとに分割し、拡張しやすい設計にしました。</p>
  </li>
</ul>

<br>

---
## <a id="苦労した点"></a> ⚠️ 苦労した点

<br>

<ul>
  <li>
    <h3>Djangoのリレーションモデルにおける集計処理</h3>
    <p>MealRating を Meal に紐づけて集計する処理（評価件数や平均点）に慣れるまで時間がかかりました。</p>
    <p>特にテンプレートでの表示ロジックとの連携に工夫を要しました。</p>
  </li>
</ul>

<br>

<ul>
  <li>
    <h3>UIと機能性のバランス調整</h3>
    <p>情報量が多くなりがちな食事レビューを、視覚的にわかりやすく・直感的に</p>
    <p>評価できるようにするUI設計に試行錯誤しました。</p>
  </li>
</ul>

<br>

---

## <a id="追加予定の機能"></a> 🔥 追加予定の機能

<br>

<ul>
  <li>
    <h3>お気に入り登録機能</h3>
    <p>気に入った投稿をブックマークして後から見返せる「お気に入り」機能を実装したいと考えています。</p>
  </li>
</ul>

<br>




---
## <a id="参考文献"></a>📗 参考文献

<br>

### 公式ドキュメント

- [Python](https://docs.python.org/ja/3/)

  Pythonコードの基本的な書き方を参照

- [Django](https://docs.djangoproject.com/ja/stable/)

  ウェブサイトを作るためのフレームワークとしての使い方を参照

- [venv](https://docs.python.org/ja/3/library/venv.html)

  グローバル環境に影響を与えず、プロジェクト単位でライブラリの導入・管理を可能にするために参照


<br>

---

## <a id="ライセンス情報"></a>📜 ライセンス情報

<br>

<ul>
  <li>
    本プロジェクトの全コード・構成・図・UIなどの著作権は、制作者である Tenshin Noji に帰属します。<br><br>
    採用選考や個人的な学習を目的とした閲覧・参照は歓迎しますが、<br><br>
    無断転載・複製・商用利用・二次配布は禁止とさせていただきます。<br><br>
    ライセンス全文はリポジトリ内の <a href="./LICENSE.md" target="_blank">LICENSEファイル</a>をご覧ください。
  </li>
</ul>

<br>
