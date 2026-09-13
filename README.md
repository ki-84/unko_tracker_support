# UNKO LAB — サポート・プライバシーポリシー

iPhone アプリ「UNKO LAB」のサポートページとプライバシーポリシー。GitHub Pages で公開しています。

- 公開URL: https://ki-84.github.io/unko_tracker_support/
- 言語：アプリと同じ8言語（ja, en, es, fr, de, pt-BR, zh-Hans, ko）。ブラウザの言語で自動選択、ボタンで切り替え
- 節へのリンク：`#support-<言語>` / `#privacy-<言語>`（例 `#privacy-en`）。`#support` `#privacy` は日本語

## 編集のしかた

文章は `build.py` の `LANGS` に言語ごとに置いてあります。直したら

```
python3 build.py
```

で `index.html` を作り直してコミットします（`index.html` を直接編集しない）。ポリシーの内容を変えたら、各言語の `updated`（最終更新日）も改めてください。アプリ内の画面名は、アプリの翻訳（`unko_tracker/scripts/localizations.tsv`）と同じ語を使います。

問い合わせは Google フォーム。アプリから開くと「Device and iOS version」に機種と iOS が入ります（`entry.1959946652`）。フォームを作り直したら ID も変わるので、`build.py` とアプリの `SupportSite.contactDeviceField` を揃えてください。
