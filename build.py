#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""index.html を8言語ぶん生成する。

    python3 build.py

文章は下の LANGS に言語ごとに置く。アプリ内の画面名は、アプリの翻訳
（unko_tracker/scripts/localizations.tsv）と同じ語を使うこと。
ポリシーを変えたら、各言語の updated（最終更新日）も改める。
"""
from html import escape
from pathlib import Path

FORM = "https://docs.google.com/forms/d/e/1FAIpQLSe3w0xD6LzK3mYLEYjBdabHse9kcyP7LgYntcwPfgEZ3PbEjw/viewform"
DEVICE_FIELD = "entry.1959946652"

# 言語コードはアプリと同じ。names は切り替えボタンの表記。
ORDER = ["ja", "en", "es", "fr", "de", "pt-BR", "zh-Hans", "ko"]
NAMES = {"ja": "日本語", "en": "English", "es": "Español", "fr": "Français", "de": "Deutsch",
         "pt-BR": "Português", "zh-Hans": "简体中文", "ko": "한국어"}
HTML_LANG = {"ja": "ja", "en": "en", "es": "es", "fr": "fr", "de": "de", "pt-BR": "pt-BR", "zh-Hans": "zh-Hans", "ko": "ko"}
REFUND = {"ja": "https://support.apple.com/ja-jp/118223", "en": "https://support.apple.com/118223",
          "es": "https://support.apple.com/es-es/118223", "fr": "https://support.apple.com/fr-fr/118223",
          "de": "https://support.apple.com/de-de/118223", "pt-BR": "https://support.apple.com/pt-br/118223",
          "zh-Hans": "https://support.apple.com/zh-cn/118223", "ko": "https://support.apple.com/ko-kr/118223"}
GOOGLE_HL = {"ja": "ja", "en": "en", "es": "es", "fr": "fr", "de": "de", "pt-BR": "pt-BR", "zh-Hans": "zh-CN", "ko": "ko"}

LANGS = {}

LANGS["ja"] = dict(
    title="サポート・プライバシーポリシー",
    lead="うんこ博士と一緒につける、iPhone向けの排便観察ノートです。",
    nav_support="サポート", nav_privacy="プライバシーポリシー",
    support_h="サポート",
    support_intro="よくある質問をまとめました。ここにない場合は、いちばん下のフォームから連絡してください。",
    faq=[
        ("アプリについて", [
            ("UNKO LAB は何をするアプリ？",
             "排便の形（ブリストルスケール）・色・量・症状・メモを記録し、月カレンダーやふり返りで眺めるための観察ノートです。博士のキャラクターが、記録の傾向と、その根拠になる研究・公的資料を紹介します。記録したぶんだけ「ぷにぷに・うんこタワー」が高くなります。"),
            ("医療アプリですか？",
             "いいえ。UNKO LAB は観察と学習のためのアプリで、診断・治療・薬の判断はしません。博士の「見立て」は記録の傾向を言葉にしたもので、医療者の判断の代わりにはなりません。血便・黒色便・発熱を伴う下痢・強い腹痛・体重減少などがあるときは、医療機関を受診してください。緊急のときは各地域の救急番号へ。"),
            ("「出なかった日」はどう扱われる？",
             "記録のない日は、入力なしで自動的に「出なかった日」として扱われます。あとから記録を足せば、その日の記録に変わります。"),
        ]),
        ("データ", [
            ("記録はどこに保存される？",
             "お使いの iPhone の中だけです。アカウントは不要で、開発者のサーバーへは送信しません。iOS のバックアップ設定によっては、iCloud や端末のバックアップに含まれます。"),
            ("記録を書き出したい",
             "設定 → 記録の持ち出し → 「CSVを共有」で、全項目を CSV ファイルとして共有できます（Pro の機能です）。共有操作をしたときだけ、選んだ相手やアプリへ記録が渡ります。"),
            ("記録を消したい",
             "設定 → 「すべての記録を削除」で端末内の記録を消せます。アプリを削除しても消えます。開発者側には記録がないため、削除の依頼は不要です。"),
        ]),
        ("UNKO LAB Pro（買い切り）", [
            ("Pro で何が変わる？",
             "広告なし、タワーの積み上げが10倍、全項目の CSV 書き出し、収録文献をすべて読める、の4つです。一度だけのお支払いで、自動更新はありません。記録・月カレンダー・博士の見立てと出典・受診案内は、これからも無料です。"),
            ("機種変更したら Pro が消えた",
             "同じ Apple アカウントでサインインし、設定 → UNKO LAB Pro → 「購入を復元」を押してください。購入は Apple が管理しているので、再購入は不要です。"),
            ("返金したい",
             "App Store の購入はすべて Apple が処理します。<a href=\"{refund}\" target=\"_blank\" rel=\"noopener\">Apple の返金申請ページ</a>から手続きしてください。"),
        ]),
        ("広告", [
            ("広告はどこに出る？",
             "無料版では、ホーム下部にバナー広告が1つ出ます。記録の入力画面や受診案内を遮る広告はありません。Pro では広告を読み込みません。"),
            ("広告の設定を変えたい",
             "同意の確認が必要な地域では、設定に「広告のプライバシー設定」が表示され、いつでも変更できます。"),
        ]),
        ("その他", [
            ("対応言語は？",
             "日本語・英語・スペイン語・フランス語・ドイツ語・ポルトガル語（ブラジル）・簡体字中国語・韓国語。端末の言語に従うか、設定で選べます。収録文献の日本語以外の版は要点の翻訳です。"),
            ("不具合を見つけた",
             "再現手順を添えて、下のフォームから知らせてください。アプリの設定 → 「お問い合わせ」から開くと、機種と iOS のバージョンは自動で入ります。"),
        ]),
    ],
    contact_h="問い合わせ",
    contact_p="Google フォームで受け付けます（英語のフォームですが、日本語で書いて構いません）。アプリの設定の「お問い合わせ」から開くと、機種と iOS のバージョンが自動で入ります。返信には数日いただくことがあります。",
    cta="問い合わせフォームを開く",
    privacy_h="プライバシーポリシー",
    updated="最終更新日：2026年9月13日",
    privacy_intro="このポリシーは、iPhone アプリ「UNKO LAB」（以下「本アプリ」）がどんなデータを扱い、どう使うかを説明します。本アプリは個人の開発者（GitHub: ki-84）が開発・公開しています。",
    sections=[
        ("要点", None, [
            "アカウントは不要で、開発者のサーバーはありません。記録は端末の中だけに保存されます。",
            "開発者は、あなたの記録を受け取りません。見ることもできません。",
            "無料版の広告は非パーソナライズで、排便の記録を広告会社に渡すことはありません。",
            "本アプリはユーザーのトラッキングを行いません。",
        ], None),
        ("端末に保存されるデータ", "本アプリは、あなたが入力した次の情報を端末内に保存します。", [
            "排便の記録：日時、形（ブリストルスケール）、色、量、血・腹痛・いきみ・切迫感・残便感・粘液・夜間の排便、所要時間、24時間以内の下剤、発熱・嘔吐・脱水感・ガス・体重減少の有無、食事・薬のメモ、タグ、自由記述",
            "アプリの設定：表示言語、タワーの進み具合など",
        ], "これらは開発者に送信されません。iOS のバックアップ設定に応じて、iCloud バックアップや端末のバックアップに含まれることがあります。バックアップの扱いは Apple のポリシーに従います。"),
        ("共有", "設定の「CSVを共有」など、あなたが共有操作をしたときだけ、選んだ相手やアプリへ記録が渡ります。共有先での取り扱いは、その相手やアプリのポリシーに従います。", None, None),
        ("購入", "UNKO LAB Pro の購入は Apple の App Store が処理します。本アプリが受け取るのは「購入済みかどうか」の情報だけで、氏名・支払い情報は受け取りません。詳しくは <a href=\"https://www.apple.com/legal/privacy/\" target=\"_blank\" rel=\"noopener\">Apple のプライバシーポリシー</a>をご覧ください。", None, None),
        ("広告（無料版）", "無料版はホーム画面下部に、Google の Mobile Ads SDK（AdMob）によるバナー広告を表示します。", [
            "広告リクエストはすべて非パーソナライズ（<code>npa=1</code>）に設定しています。App Tracking Transparency のトラッキング許可は求めません。",
            "広告 SDK は、広告の配信・計測・不正防止のために、端末の情報（機種、OS のバージョン、IP アドレス、IP から推定されるおおまかな地域、広告の表示・タップ）を Google に送ることがあります。",
            "EEA・英国・スイスなど同意の確認が必要な地域では、Google の User Messaging Platform で同意を確認します。設定の「広告のプライバシー設定」からいつでも変更できます。",
            "広告の機能は排便の記録に触れない設計で、記録の内容や博士への質問を広告会社に渡すことはありません。",
            "Pro では広告を読み込みません。",
        ], "Google のデータの取り扱いについては、<a href=\"{gpriv}\" target=\"_blank\" rel=\"noopener\">Google のプライバシーポリシー</a>と<a href=\"{gpartner}\" target=\"_blank\" rel=\"noopener\">Google のサービスを使用するサイトやアプリから収集した情報の Google での使用</a>をご覧ください。"),
        ("健康に関する情報の扱い", "排便の記録は健康に関わる情報です。本アプリはこれを端末内の記録・表示・ふり返りにだけ使い、広告や第三者への提供には使いません。Apple の HealthKit には接続しません。本アプリの内容は医療上の助言ではなく、診断・治療の代わりにはなりません。", None, None),
        ("外部リンク", "収録文献の「原文・論文を開く」などのリンクは、お使いのブラウザで外部サイトを開きます。リンク先での取り扱いは、各サイトのポリシーに従います。", None, None),
        ("子どものプライバシー", "本アプリは13歳未満の子どもを対象にしていません。子どもから個人情報を意図的に集めることはありません。", None, None),
        ("あなたにできること", None, [
            "記録の削除：設定 → 「すべての記録を削除」、またはアプリの削除",
            "広告の同意の変更：設定 → 「広告のプライバシー設定」（表示される地域のみ）",
            "記録の持ち出し：設定 → 記録の持ち出し → 「CSVを共有」（Pro）",
        ], None),
        ("ポリシーの変更", "内容を変えるときは、このページを更新し、最終更新日を改めます。", None, None),
    ],
    privacy_contact_h="問い合わせ",
    privacy_contact_p="このポリシーについての質問は、サポートと同じフォームから受け付けます。フォームは Google フォームで、入力内容は Google に保存され、開発者が読みます。メールアドレスは、返信を希望するときだけ書いてください。",
    footer="UNKO LAB — サポート・プライバシーポリシー",
)

LANGS["en"] = dict(
    title="Support &amp; Privacy Policy",
    lead="A bowel-movement diary for iPhone, kept together with the Poop Professor.",
    nav_support="Support", nav_privacy="Privacy Policy",
    support_h="Support",
    support_intro="Answers to common questions. If yours isn't here, use the contact form at the bottom.",
    faq=[
        ("About the app", [
            ("What does UNKO LAB do?",
             "It is an observation diary for bowel movements: shape (Bristol scale), colour, amount, symptoms and notes, viewed on a monthly calendar and in a weekly review. The Professor character points out patterns in your log and the research or public-health sources behind them. Every entry raises your \"Squishy Poop Tower\"."),
            ("Is it a medical app?",
             "No. UNKO LAB is for observation and learning. It does not diagnose, treat or make decisions about medication. The Professor's readings put a pattern in your log into words; they are not a substitute for a clinician. If you notice blood or black stools, diarrhoea with fever, severe abdominal pain or weight loss, please see a healthcare professional. In an emergency, call your local emergency number."),
            ("How are days without a bowel movement handled?",
             "A day with no entry is automatically treated as a day without a movement — nothing to enter. Adding an entry later turns it into a recorded day."),
        ]),
        ("Your data", [
            ("Where is my log stored?",
             "Only on your iPhone. There is no account and nothing is sent to a server run by the developer. Depending on your iOS settings, the data may be included in iCloud or device backups."),
            ("Can I export my log?",
             "Settings → Export records → \"Share CSV\" exports every field as a CSV file (a Pro feature). Your records leave the device only when you share them, and only to the app or person you choose."),
            ("How do I delete my data?",
             "Settings → \"Delete all records\" erases the log on the device. Deleting the app does the same. The developer holds no copy, so there is nothing to request."),
        ]),
        ("UNKO LAB Pro (one-time purchase)", [
            ("What does Pro include?",
             "Four things: no ads, a tower that grows 10× faster, full-detail CSV export, and the complete research library. It is a single payment with no automatic renewal. Logging, the monthly calendar, the Professor's readings with their sources and consultation guidance stay free."),
            ("I switched phones and lost Pro",
             "Sign in with the same Apple account, then open Settings → UNKO LAB Pro → \"Restore purchases\". Apple keeps the purchase, so you never pay twice."),
            ("I want a refund",
             "All App Store purchases are handled by Apple. Please use <a href=\"{refund}\" target=\"_blank\" rel=\"noopener\">Apple's refund request page</a>."),
        ]),
        ("Ads", [
            ("Where do ads appear?",
             "The free version shows one banner at the bottom of the Home tab. No ad ever covers the entry form or consultation guidance. Pro does not load ads."),
            ("Can I change my ad choices?",
             "In regions where consent is required, Settings shows \"Ad privacy choices\", which you can change at any time."),
        ]),
        ("Other", [
            ("Which languages are supported?",
             "Japanese, English, Spanish, French, German, Portuguese (Brazil), Simplified Chinese and Korean. The app follows the device language or a choice made in Settings. Non-Japanese versions of the research cards are summaries of the key points."),
            ("I found a bug",
             "Please use the form below with the steps to reproduce it. Opening the form from Settings → \"Contact\" in the app fills in your device model and iOS version."),
        ]),
    ],
    contact_h="Contact",
    contact_p="Requests are received through a Google Form. Opening it from \"Contact\" in the app's Settings fills in your device and iOS version. Replies may take a few days.",
    cta="Open the contact form",
    privacy_h="Privacy Policy",
    updated="Last updated: 13 September 2026",
    privacy_intro="This policy explains what data the iPhone app \"UNKO LAB\" (the \"app\") handles and how it is used. The app is developed and published by an independent developer (GitHub: ki-84).",
    sections=[
        ("In short", None, [
            "No account, and no server run by the developer. Your log lives only on your device.",
            "The developer never receives your records and cannot see them.",
            "Ads in the free version are non-personalised, and your bowel log is never passed to advertisers.",
            "The app does not track you.",
        ], None),
        ("Data stored on your device", "The app stores the following information that you enter, on the device only:", [
            "Bowel-movement records: date and time, shape (Bristol scale), colour, amount, blood, abdominal pain, straining, urgency, incomplete evacuation, mucus, night-time movements, time spent, laxative use in the last 24 hours, fever, vomiting, dehydration, gas, weight loss, notes on food and medicine, tags and free text",
            "App settings: display language, tower progress and similar",
        ], "None of this is sent to the developer. Depending on your iOS settings it may be included in iCloud or device backups, which are governed by Apple's policies."),
        ("Sharing", "Your records leave the device only when you use a share action such as \"Share CSV\" in Settings, and only to the app or person you choose. Their handling of the data is governed by that recipient's policies.", None, None),
        ("Purchases", "UNKO LAB Pro is sold through Apple's App Store. The app receives only whether the purchase is active — never your name or payment details. See <a href=\"https://www.apple.com/legal/privacy/\" target=\"_blank\" rel=\"noopener\">Apple's privacy policy</a>.", None, None),
        ("Advertising (free version)", "The free version shows a banner at the bottom of the Home tab using Google's Mobile Ads SDK (AdMob).", [
            "Every ad request is configured as non-personalised (<code>npa=1</code>). The app does not ask for App Tracking Transparency permission.",
            "To deliver, measure and protect ads, the SDK may send device information to Google — device model, OS version, IP address, an approximate region derived from the IP address, and ad impressions and taps.",
            "In the EEA, the UK, Switzerland and other regions where consent is required, consent is collected through Google's User Messaging Platform. You can change it at any time via \"Ad privacy choices\" in Settings.",
            "The advertising code has no access to your bowel records. Neither your entries nor your questions to the Professor are ever passed to advertisers.",
            "Pro does not load ads.",
        ], "For Google's handling of data, see the <a href=\"{gpriv}\" target=\"_blank\" rel=\"noopener\">Google Privacy Policy</a> and <a href=\"{gpartner}\" target=\"_blank\" rel=\"noopener\">How Google uses information from sites or apps that use its services</a>."),
        ("Health information", "Bowel records are health-related information. The app uses them only for logging, display and review on your device — never for advertising or disclosure to third parties. The app does not connect to Apple HealthKit. Nothing in the app is medical advice or a substitute for diagnosis or treatment.", None, None),
        ("External links", "Links such as \"Open the original source\" on research cards open external sites in your browser. Those sites' own policies apply.", None, None),
        ("Children's privacy", "The app is not directed at children under 13 and does not knowingly collect personal information from children.", None, None),
        ("Your choices", None, [
            "Delete your log: Settings → \"Delete all records\", or delete the app",
            "Change ad consent: Settings → \"Ad privacy choices\" (shown only where required)",
            "Export your log: Settings → Export records → \"Share CSV\" (Pro)",
        ], None),
        ("Changes to this policy", "Changes will be posted on this page with an updated \"Last updated\" date.", None, None),
    ],
    privacy_contact_h="Contact",
    privacy_contact_p="Questions about this policy can be sent through the same contact form used for support. The form is a Google Form: what you enter is stored by Google and read by the developer. Give an email address only if you want a reply.",
    footer="UNKO LAB — Support &amp; Privacy Policy",
)

LANGS["es"] = dict(
    title="Soporte y política de privacidad",
    lead="Un diario de deposiciones para iPhone, que llevas junto al Profesor Caca.",
    nav_support="Soporte", nav_privacy="Política de privacidad",
    support_h="Soporte",
    support_intro="Respuestas a las preguntas más frecuentes. Si la tuya no está aquí, usa el formulario de contacto al final.",
    faq=[
        ("Sobre la app", [
            ("¿Qué hace UNKO LAB?",
             "Es un diario de observación de las deposiciones: forma (escala de Bristol), color, cantidad, síntomas y notas, que puedes ver en un calendario mensual y en un resumen semanal. El personaje del Profesor señala tendencias en tus registros y las fuentes científicas o de salud pública que las respaldan. Cada registro hace crecer tu «Torre de Popó Blandita»."),
            ("¿Es una app médica?",
             "No. UNKO LAB sirve para observar y aprender. No diagnostica, no trata ni decide sobre medicamentos. Las lecturas del Profesor ponen en palabras una tendencia de tus registros; no sustituyen a un profesional sanitario. Si observas sangre o heces negras, diarrea con fiebre, dolor abdominal intenso o pérdida de peso, consulta a un profesional. En una emergencia, llama al número de emergencias de tu zona."),
            ("¿Cómo se tratan los días sin deposición?",
             "Un día sin registro se considera automáticamente un día sin deposición: no hay que introducir nada. Si más tarde añades un registro, pasa a ser un día registrado."),
        ]),
        ("Tus datos", [
            ("¿Dónde se guardan mis registros?",
             "Solo en tu iPhone. No hay cuenta y no se envía nada a un servidor del desarrollador. Según tus ajustes de iOS, los datos pueden incluirse en las copias de seguridad de iCloud o del dispositivo."),
            ("¿Puedo exportar mis registros?",
             "Ajustes → Exportar registros → «Compartir CSV» exporta todos los campos en un archivo CSV (función Pro). Tus registros solo salen del dispositivo cuando los compartes, y solo hacia la app o la persona que elijas."),
            ("¿Cómo borro mis datos?",
             "Ajustes → «Eliminar todos los registros» borra el diario del dispositivo. Eliminar la app hace lo mismo. El desarrollador no guarda ninguna copia, así que no hay nada que solicitar."),
        ]),
        ("UNKO LAB Pro (compra única)", [
            ("¿Qué incluye Pro?",
             "Cuatro cosas: sin anuncios, una torre que crece 10 veces más rápido, exportación CSV completa y la biblioteca de estudios al completo. Es un pago único sin renovación automática. Los registros, el calendario mensual, las lecturas del Profesor con sus fuentes y la orientación para consultar siguen siendo gratis."),
            ("Cambié de teléfono y perdí Pro",
             "Inicia sesión con la misma cuenta de Apple y abre Ajustes → UNKO LAB Pro → «Restaurar compras». Apple conserva la compra, así que nunca pagas dos veces."),
            ("Quiero un reembolso",
             "Todas las compras del App Store las gestiona Apple. Usa la <a href=\"{refund}\" target=\"_blank\" rel=\"noopener\">página de solicitud de reembolso de Apple</a>."),
        ]),
        ("Anuncios", [
            ("¿Dónde aparecen los anuncios?",
             "La versión gratuita muestra un banner en la parte inferior de la pestaña de inicio. Ningún anuncio cubre el formulario de registro ni la orientación para consultar. Pro no carga anuncios."),
            ("¿Puedo cambiar mis preferencias de anuncios?",
             "En las regiones donde se requiere consentimiento, Ajustes muestra «Privacidad de anuncios», que puedes cambiar en cualquier momento."),
        ]),
        ("Otros", [
            ("¿Qué idiomas admite?",
             "Japonés, inglés, español, francés, alemán, portugués (Brasil), chino simplificado y coreano. La app sigue el idioma del dispositivo o el que elijas en Ajustes. Las versiones de las fichas de estudios en idiomas distintos del japonés son resúmenes de los puntos clave."),
            ("He encontrado un error",
             "Usa el formulario de abajo e incluye los pasos para reproducirlo. Si abres el formulario desde Ajustes → «Contacto» en la app, el modelo de dispositivo y la versión de iOS se rellenan solos."),
        ]),
    ],
    contact_h="Contacto",
    contact_p="Las solicitudes se reciben mediante un formulario de Google (está en inglés, pero puedes escribir en español). Si lo abres desde «Contacto» en los Ajustes de la app, el dispositivo y la versión de iOS se rellenan solos. La respuesta puede tardar unos días.",
    cta="Abrir el formulario de contacto",
    privacy_h="Política de privacidad",
    updated="Última actualización: 13 de septiembre de 2026",
    privacy_intro="Esta política explica qué datos maneja la app para iPhone «UNKO LAB» (la «app») y cómo se usan. La app la desarrolla y publica un desarrollador independiente (GitHub: ki-84).",
    sections=[
        ("En resumen", None, [
            "Sin cuenta y sin servidor del desarrollador. Tus registros viven solo en tu dispositivo.",
            "El desarrollador nunca recibe tus registros y no puede verlos.",
            "Los anuncios de la versión gratuita no son personalizados, y tu diario nunca se entrega a anunciantes.",
            "La app no te rastrea.",
        ], None),
        ("Datos guardados en tu dispositivo", "La app guarda, solo en el dispositivo, la siguiente información que introduces:", [
            "Registros de deposiciones: fecha y hora, forma (escala de Bristol), color, cantidad, sangre, dolor abdominal, esfuerzo, urgencia, evacuación incompleta, moco, deposiciones nocturnas, tiempo empleado, uso de laxantes en las últimas 24 horas, fiebre, vómitos, deshidratación, gases, pérdida de peso, notas sobre comida y medicamentos, etiquetas y texto libre",
            "Ajustes de la app: idioma, progreso de la torre y similares",
        ], "Nada de esto se envía al desarrollador. Según tus ajustes de iOS, puede incluirse en las copias de seguridad de iCloud o del dispositivo, que se rigen por las políticas de Apple."),
        ("Compartir", "Tus registros solo salen del dispositivo cuando usas una acción de compartir, como «Compartir CSV» en Ajustes, y solo hacia la app o la persona que elijas. El tratamiento posterior se rige por las políticas de ese destinatario.", None, None),
        ("Compras", "UNKO LAB Pro se vende a través del App Store de Apple. La app solo recibe si la compra está activa; nunca tu nombre ni tus datos de pago. Consulta la <a href=\"https://www.apple.com/legal/privacy/\" target=\"_blank\" rel=\"noopener\">política de privacidad de Apple</a>.", None, None),
        ("Publicidad (versión gratuita)", "La versión gratuita muestra un banner en la parte inferior de la pestaña de inicio mediante el SDK Mobile Ads de Google (AdMob).", [
            "Todas las solicitudes de anuncios están configuradas como no personalizadas (<code>npa=1</code>). La app no pide el permiso de App Tracking Transparency.",
            "Para entregar, medir y proteger los anuncios, el SDK puede enviar a Google información del dispositivo: modelo, versión del sistema, dirección IP, una región aproximada derivada de la IP, e impresiones y toques en los anuncios.",
            "En el EEE, el Reino Unido, Suiza y otras regiones donde se requiere consentimiento, este se recoge mediante la User Messaging Platform de Google. Puedes cambiarlo en cualquier momento en «Privacidad de anuncios», en Ajustes.",
            "El código de publicidad no tiene acceso a tus registros. Ni tus entradas ni tus preguntas al Profesor se entregan nunca a anunciantes.",
            "Pro no carga anuncios.",
        ], "Sobre el tratamiento de datos por parte de Google, consulta la <a href=\"{gpriv}\" target=\"_blank\" rel=\"noopener\">Política de privacidad de Google</a> y <a href=\"{gpartner}\" target=\"_blank\" rel=\"noopener\">Cómo usa Google la información de sitios o apps que utilizan sus servicios</a>."),
        ("Información de salud", "Los registros de deposiciones son información relacionada con la salud. La app los usa solo para registrar, mostrar y revisar en tu dispositivo; nunca para publicidad ni para cederlos a terceros. La app no se conecta a Apple HealthKit. Nada en la app constituye consejo médico ni sustituye un diagnóstico o tratamiento.", None, None),
        ("Enlaces externos", "Enlaces como «Abrir la fuente original» en las fichas de estudios abren sitios externos en tu navegador. Se aplican las políticas de esos sitios.", None, None),
        ("Privacidad de los menores", "La app no está dirigida a menores de 13 años y no recoge a sabiendas información personal de menores.", None, None),
        ("Tus opciones", None, [
            "Borrar tus registros: Ajustes → «Eliminar todos los registros», o eliminar la app",
            "Cambiar el consentimiento de anuncios: Ajustes → «Privacidad de anuncios» (solo donde se requiere)",
            "Exportar tus registros: Ajustes → Exportar registros → «Compartir CSV» (Pro)",
        ], None),
        ("Cambios en esta política", "Los cambios se publicarán en esta página con una nueva fecha de «Última actualización».", None, None),
    ],
    privacy_contact_h="Contacto",
    privacy_contact_p="Las preguntas sobre esta política pueden enviarse por el mismo formulario de contacto que el soporte. Es un formulario de Google: lo que escribas lo almacena Google y lo lee el desarrollador. Indica un correo electrónico solo si quieres respuesta.",
    footer="UNKO LAB — Soporte y política de privacidad",
)

LANGS["fr"] = dict(
    title="Assistance et politique de confidentialité",
    lead="Un journal des selles pour iPhone, tenu en compagnie du Professeur Caca.",
    nav_support="Assistance", nav_privacy="Politique de confidentialité",
    support_h="Assistance",
    support_intro="Réponses aux questions fréquentes. Si la vôtre n'y figure pas, utilisez le formulaire de contact en bas de page.",
    faq=[
        ("À propos de l'app", [
            ("Que fait UNKO LAB ?",
             "C'est un journal d'observation des selles : forme (échelle de Bristol), couleur, quantité, symptômes et notes, consultables sur un calendrier mensuel et dans un bilan hebdomadaire. Le personnage du Professeur relève des tendances dans vos notes et cite les études ou sources de santé publique qui les étayent. Chaque note fait grandir votre « tour des petits cacas »."),
            ("Est-ce une app médicale ?",
             "Non. UNKO LAB sert à observer et à apprendre. Elle ne pose pas de diagnostic, ne traite pas et ne décide rien concernant les médicaments. Les lectures du Professeur mettent en mots une tendance de vos notes ; elles ne remplacent pas un professionnel de santé. En cas de sang ou de selles noires, de diarrhée avec fièvre, de douleur abdominale intense ou de perte de poids, consultez un professionnel. En cas d'urgence, appelez le numéro d'urgence de votre région."),
            ("Comment sont traités les jours sans selles ?",
             "Un jour sans note est automatiquement considéré comme un jour sans selles : rien à saisir. Si vous ajoutez une note plus tard, il devient un jour noté."),
        ]),
        ("Vos données", [
            ("Où mes notes sont-elles stockées ?",
             "Uniquement sur votre iPhone. Il n'y a pas de compte et rien n'est envoyé à un serveur du développeur. Selon vos réglages iOS, les données peuvent figurer dans les sauvegardes iCloud ou de l'appareil."),
            ("Puis-je exporter mes notes ?",
             "Réglages → Exporter les notes → « Partager CSV » exporte tous les champs dans un fichier CSV (fonction Pro). Vos notes ne quittent l'appareil que lorsque vous les partagez, et seulement vers l'app ou la personne de votre choix."),
            ("Comment supprimer mes données ?",
             "Réglages → « Supprimer toutes les notes » efface le journal de l'appareil. Supprimer l'app a le même effet. Le développeur n'en détient aucune copie : il n'y a rien à demander."),
        ]),
        ("UNKO LAB Pro (achat unique)", [
            ("Que comprend Pro ?",
             "Quatre choses : pas de publicité, une tour qui grandit 10 fois plus vite, un export CSV détaillé et la bibliothèque d'études complète. C'est un paiement unique, sans renouvellement automatique. Les notes, le calendrier mensuel, les lectures du Professeur avec leurs sources et les conseils de consultation restent gratuits."),
            ("J'ai changé de téléphone et perdu Pro",
             "Connectez-vous avec le même compte Apple, puis ouvrez Réglages → UNKO LAB Pro → « Restaurer les achats ». Apple conserve l'achat : vous ne payez jamais deux fois."),
            ("Je souhaite un remboursement",
             "Tous les achats de l'App Store sont gérés par Apple. Utilisez la <a href=\"{refund}\" target=\"_blank\" rel=\"noopener\">page de demande de remboursement d'Apple</a>."),
        ]),
        ("Publicité", [
            ("Où apparaissent les annonces ?",
             "La version gratuite affiche une bannière en bas de l'onglet Accueil. Aucune annonce ne recouvre le formulaire de saisie ni les conseils de consultation. Pro ne charge aucune annonce."),
            ("Puis-je modifier mes choix publicitaires ?",
             "Dans les régions où le consentement est requis, les Réglages affichent « Confidentialité des annonces », modifiable à tout moment."),
        ]),
        ("Autres", [
            ("Quelles langues sont prises en charge ?",
             "Japonais, anglais, espagnol, français, allemand, portugais (Brésil), chinois simplifié et coréen. L'app suit la langue de l'appareil ou celle choisie dans les Réglages. Les fiches d'études dans les langues autres que le japonais sont des résumés des points clés."),
            ("J'ai trouvé un bug",
             "Utilisez le formulaire ci-dessous en indiquant les étapes pour le reproduire. En ouvrant le formulaire depuis Réglages → « Contact » dans l'app, le modèle d'appareil et la version d'iOS sont remplis automatiquement."),
        ]),
    ],
    contact_h="Contact",
    contact_p="Les demandes sont reçues via un formulaire Google (en anglais, mais vous pouvez écrire en français). En l'ouvrant depuis « Contact » dans les Réglages de l'app, l'appareil et la version d'iOS sont remplis automatiquement. La réponse peut prendre quelques jours.",
    cta="Ouvrir le formulaire de contact",
    privacy_h="Politique de confidentialité",
    updated="Dernière mise à jour : 13 septembre 2026",
    privacy_intro="Cette politique explique quelles données l'app iPhone « UNKO LAB » (l'« app ») traite et comment elles sont utilisées. L'app est développée et publiée par un développeur indépendant (GitHub : ki-84).",
    sections=[
        ("En bref", None, [
            "Pas de compte, et pas de serveur géré par le développeur. Vos notes ne vivent que sur votre appareil.",
            "Le développeur ne reçoit jamais vos notes et ne peut pas les voir.",
            "Les annonces de la version gratuite ne sont pas personnalisées, et votre journal n'est jamais transmis aux annonceurs.",
            "L'app ne vous suit pas.",
        ], None),
        ("Données stockées sur votre appareil", "L'app stocke, uniquement sur l'appareil, les informations suivantes que vous saisissez :", [
            "Notes de selles : date et heure, forme (échelle de Bristol), couleur, quantité, sang, douleur abdominale, effort, urgence, évacuation incomplète, mucus, selles nocturnes, durée, laxatif dans les 24 dernières heures, fièvre, vomissements, déshydratation, gaz, perte de poids, notes sur l'alimentation et les médicaments, étiquettes et texte libre",
            "Réglages de l'app : langue d'affichage, progression de la tour, etc.",
        ], "Rien de tout cela n'est envoyé au développeur. Selon vos réglages iOS, ces données peuvent figurer dans les sauvegardes iCloud ou de l'appareil, régies par les politiques d'Apple."),
        ("Partage", "Vos notes ne quittent l'appareil que lorsque vous utilisez une action de partage, comme « Partager CSV » dans les Réglages, et seulement vers l'app ou la personne de votre choix. Leur traitement ultérieur relève des politiques de ce destinataire.", None, None),
        ("Achats", "UNKO LAB Pro est vendu via l'App Store d'Apple. L'app ne reçoit que l'information « achat actif ou non » — jamais votre nom ni vos données de paiement. Voir la <a href=\"https://www.apple.com/legal/privacy/\" target=\"_blank\" rel=\"noopener\">politique de confidentialité d'Apple</a>.", None, None),
        ("Publicité (version gratuite)", "La version gratuite affiche une bannière en bas de l'onglet Accueil via le SDK Mobile Ads de Google (AdMob).", [
            "Chaque requête publicitaire est configurée comme non personnalisée (<code>npa=1</code>). L'app ne demande pas l'autorisation App Tracking Transparency.",
            "Pour diffuser, mesurer et protéger les annonces, le SDK peut envoyer à Google des informations sur l'appareil : modèle, version du système, adresse IP, région approximative déduite de l'IP, affichages et touchers d'annonces.",
            "Dans l'EEE, au Royaume-Uni, en Suisse et dans les autres régions où le consentement est requis, il est recueilli via la User Messaging Platform de Google. Vous pouvez le modifier à tout moment dans « Confidentialité des annonces », dans les Réglages.",
            "Le code publicitaire n'a pas accès à vos notes. Ni vos entrées ni vos questions au Professeur ne sont jamais transmises aux annonceurs.",
            "Pro ne charge aucune annonce.",
        ], "Pour le traitement des données par Google, consultez la <a href=\"{gpriv}\" target=\"_blank\" rel=\"noopener\">politique de confidentialité de Google</a> et <a href=\"{gpartner}\" target=\"_blank\" rel=\"noopener\">Comment Google utilise les informations provenant de sites ou d'applications qui utilisent ses services</a>."),
        ("Informations de santé", "Les notes de selles sont des informations liées à la santé. L'app ne les utilise que pour la saisie, l'affichage et le bilan sur votre appareil — jamais pour la publicité ni pour les communiquer à des tiers. L'app ne se connecte pas à Apple HealthKit. Rien dans l'app ne constitue un avis médical ni ne remplace un diagnostic ou un traitement.", None, None),
        ("Liens externes", "Les liens comme « Ouvrir la source originale » sur les fiches d'études ouvrent des sites externes dans votre navigateur. Les politiques de ces sites s'appliquent.", None, None),
        ("Vie privée des enfants", "L'app ne s'adresse pas aux enfants de moins de 13 ans et ne collecte pas sciemment d'informations personnelles auprès d'enfants.", None, None),
        ("Vos choix", None, [
            "Supprimer vos notes : Réglages → « Supprimer toutes les notes », ou supprimer l'app",
            "Modifier le consentement publicitaire : Réglages → « Confidentialité des annonces » (affiché seulement là où c'est requis)",
            "Exporter vos notes : Réglages → Exporter les notes → « Partager CSV » (Pro)",
        ], None),
        ("Modifications de cette politique", "Les modifications seront publiées sur cette page avec une nouvelle date de « Dernière mise à jour ».", None, None),
    ],
    privacy_contact_h="Contact",
    privacy_contact_p="Les questions sur cette politique peuvent être envoyées via le même formulaire de contact que l'assistance. C'est un formulaire Google : ce que vous saisissez est stocké par Google et lu par le développeur. N'indiquez une adresse e-mail que si vous souhaitez une réponse.",
    footer="UNKO LAB — Assistance et politique de confidentialité",
)

LANGS["de"] = dict(
    title="Support und Datenschutzerklärung",
    lead="Ein Stuhlgang-Tagebuch für das iPhone, geführt zusammen mit dem Kackprofessor.",
    nav_support="Support", nav_privacy="Datenschutzerklärung",
    support_h="Support",
    support_intro="Antworten auf häufige Fragen. Fehlt deine, nutze das Kontaktformular ganz unten.",
    faq=[
        ("Über die App", [
            ("Was macht UNKO LAB?",
             "Es ist ein Beobachtungstagebuch für den Stuhlgang: Form (Bristol-Skala), Farbe, Menge, Beschwerden und Notizen, dargestellt im Monatskalender und in einem Wochenrückblick. Die Figur des Professors weist auf Muster in deinen Einträgen hin und nennt die Studien oder öffentlichen Gesundheitsquellen dahinter. Jeder Eintrag lässt deinen „weichen Pups-Turm“ wachsen."),
            ("Ist das eine medizinische App?",
             "Nein. UNKO LAB dient dem Beobachten und Lernen. Die App stellt keine Diagnosen, behandelt nicht und trifft keine Entscheidungen über Medikamente. Die Einschätzungen des Professors fassen ein Muster in deinen Einträgen in Worte; sie ersetzen keine Fachperson. Bei Blut oder schwarzem Stuhl, Durchfall mit Fieber, starken Bauchschmerzen oder Gewichtsverlust wende dich bitte an eine Ärztin oder einen Arzt. Im Notfall rufe die Notrufnummer deiner Region an."),
            ("Wie werden Tage ohne Stuhlgang behandelt?",
             "Ein Tag ohne Eintrag gilt automatisch als Tag ohne Stuhlgang – nichts einzutragen. Fügst du später einen Eintrag hinzu, wird daraus ein erfasster Tag."),
        ]),
        ("Deine Daten", [
            ("Wo werden meine Einträge gespeichert?",
             "Nur auf deinem iPhone. Es gibt kein Konto, und nichts wird an einen Server des Entwicklers gesendet. Je nach iOS-Einstellungen können die Daten in iCloud- oder Geräte-Backups enthalten sein."),
            ("Kann ich meine Einträge exportieren?",
             "Einstellungen → Daten exportieren → „CSV teilen“ exportiert alle Felder als CSV-Datei (Pro-Funktion). Deine Einträge verlassen das Gerät nur, wenn du sie teilst, und nur an die App oder Person, die du auswählst."),
            ("Wie lösche ich meine Daten?",
             "Einstellungen → „Alle Einträge löschen“ entfernt das Tagebuch vom Gerät. Das Löschen der App bewirkt dasselbe. Der Entwickler hat keine Kopie, es gibt also nichts zu beantragen."),
        ]),
        ("UNKO LAB Pro (Einmalkauf)", [
            ("Was enthält Pro?",
             "Vier Dinge: keine Werbung, ein Turm, der 10-mal schneller wächst, vollständiger CSV-Export und die komplette Studienbibliothek. Es ist eine einmalige Zahlung ohne automatische Verlängerung. Einträge, Monatskalender, die Einschätzungen des Professors samt Quellen und Hinweise zum Arztbesuch bleiben kostenlos."),
            ("Ich habe das Telefon gewechselt und Pro verloren",
             "Melde dich mit demselben Apple-Account an und öffne Einstellungen → UNKO LAB Pro → „Käufe wiederherstellen“. Apple bewahrt den Kauf auf, du zahlst nie doppelt."),
            ("Ich möchte eine Rückerstattung",
             "Alle App-Store-Käufe wickelt Apple ab. Bitte nutze die <a href=\"{refund}\" target=\"_blank\" rel=\"noopener\">Seite für Rückerstattungsanträge von Apple</a>."),
        ]),
        ("Werbung", [
            ("Wo erscheint Werbung?",
             "Die kostenlose Version zeigt ein Banner am unteren Rand des Home-Tabs. Keine Anzeige verdeckt je das Eingabeformular oder die Hinweise zum Arztbesuch. Pro lädt keine Werbung."),
            ("Kann ich meine Werbeeinstellungen ändern?",
             "In Regionen, in denen eine Einwilligung erforderlich ist, zeigen die Einstellungen „Datenschutz für Werbung“, jederzeit änderbar."),
        ]),
        ("Sonstiges", [
            ("Welche Sprachen werden unterstützt?",
             "Japanisch, Englisch, Spanisch, Französisch, Deutsch, Portugiesisch (Brasilien), vereinfachtes Chinesisch und Koreanisch. Die App folgt der Gerätesprache oder der Auswahl in den Einstellungen. Die Studienkarten in anderen Sprachen als Japanisch sind Zusammenfassungen der Kernpunkte."),
            ("Ich habe einen Fehler gefunden",
             "Nutze bitte das Formular unten und beschreibe die Schritte, mit denen er sich reproduzieren lässt. Öffnest du das Formular über Einstellungen → „Kontakt“ in der App, werden Gerätemodell und iOS-Version automatisch eingetragen."),
        ]),
    ],
    contact_h="Kontakt",
    contact_p="Anfragen gehen über ein Google-Formular ein (auf Englisch, du kannst aber auf Deutsch schreiben). Öffnest du es über „Kontakt“ in den Einstellungen der App, werden Gerät und iOS-Version automatisch eingetragen. Eine Antwort kann ein paar Tage dauern.",
    cta="Kontaktformular öffnen",
    privacy_h="Datenschutzerklärung",
    updated="Zuletzt aktualisiert: 13. September 2026",
    privacy_intro="Diese Erklärung beschreibt, welche Daten die iPhone-App „UNKO LAB“ (die „App“) verarbeitet und wie sie verwendet werden. Die App wird von einem unabhängigen Entwickler (GitHub: ki-84) entwickelt und veröffentlicht.",
    sections=[
        ("Kurz gesagt", None, [
            "Kein Konto und kein Server des Entwicklers. Deine Einträge liegen nur auf deinem Gerät.",
            "Der Entwickler erhält deine Einträge nie und kann sie nicht sehen.",
            "Die Werbung in der kostenlosen Version ist nicht personalisiert, und dein Tagebuch wird nie an Werbetreibende weitergegeben.",
            "Die App trackt dich nicht.",
        ], None),
        ("Auf deinem Gerät gespeicherte Daten", "Die App speichert folgende von dir eingegebene Informationen, ausschließlich auf dem Gerät:", [
            "Stuhlgang-Einträge: Datum und Uhrzeit, Form (Bristol-Skala), Farbe, Menge, Blut, Bauchschmerzen, Pressen, Stuhldrang, unvollständige Entleerung, Schleim, nächtlicher Stuhlgang, Dauer, Abführmittel in den letzten 24 Stunden, Fieber, Erbrechen, Dehydrierung, Blähungen, Gewichtsverlust, Notizen zu Essen und Medikamenten, Tags und Freitext",
            "App-Einstellungen: Anzeigesprache, Turmfortschritt und Ähnliches",
        ], "Nichts davon wird an den Entwickler gesendet. Je nach iOS-Einstellungen kann es in iCloud- oder Geräte-Backups enthalten sein, für die Apples Richtlinien gelten."),
        ("Teilen", "Deine Einträge verlassen das Gerät nur, wenn du eine Teilen-Aktion wie „CSV teilen“ in den Einstellungen nutzt, und nur an die App oder Person, die du auswählst. Der weitere Umgang richtet sich nach den Richtlinien dieses Empfängers.", None, None),
        ("Käufe", "UNKO LAB Pro wird über Apples App Store verkauft. Die App erfährt nur, ob der Kauf aktiv ist – nie deinen Namen oder Zahlungsdaten. Siehe <a href=\"https://www.apple.com/legal/privacy/\" target=\"_blank\" rel=\"noopener\">Apples Datenschutzrichtlinie</a>.", None, None),
        ("Werbung (kostenlose Version)", "Die kostenlose Version zeigt am unteren Rand des Home-Tabs ein Banner über Googles Mobile Ads SDK (AdMob).", [
            "Jede Werbeanfrage ist als nicht personalisiert konfiguriert (<code>npa=1</code>). Die App fragt nicht nach der App-Tracking-Transparency-Erlaubnis.",
            "Um Anzeigen auszuliefern, zu messen und zu schützen, kann das SDK Geräteinformationen an Google senden – Gerätemodell, Betriebssystemversion, IP-Adresse, eine aus der IP abgeleitete ungefähre Region sowie Einblendungen und Antippen von Anzeigen.",
            "Im EWR, im Vereinigten Königreich, in der Schweiz und in anderen Regionen mit Einwilligungspflicht wird die Einwilligung über Googles User Messaging Platform eingeholt. Du kannst sie jederzeit unter „Datenschutz für Werbung“ in den Einstellungen ändern.",
            "Der Werbecode hat keinen Zugriff auf deine Einträge. Weder deine Einträge noch deine Fragen an den Professor werden je an Werbetreibende weitergegeben.",
            "Pro lädt keine Werbung.",
        ], "Zum Umgang von Google mit Daten siehe die <a href=\"{gpriv}\" target=\"_blank\" rel=\"noopener\">Datenschutzerklärung von Google</a> und <a href=\"{gpartner}\" target=\"_blank\" rel=\"noopener\">Wie Google Informationen von Websites oder Apps verwendet, die seine Dienste nutzen</a>."),
        ("Gesundheitsinformationen", "Stuhlgang-Einträge sind gesundheitsbezogene Informationen. Die App nutzt sie nur zum Erfassen, Anzeigen und Zurückblicken auf deinem Gerät – nie für Werbung oder zur Weitergabe an Dritte. Die App verbindet sich nicht mit Apple HealthKit. Nichts in der App ist ein medizinischer Rat oder ersetzt Diagnose oder Behandlung.", None, None),
        ("Externe Links", "Links wie „Originalquelle öffnen“ auf den Studienkarten öffnen externe Seiten in deinem Browser. Dort gelten die Richtlinien der jeweiligen Seite.", None, None),
        ("Datenschutz von Kindern", "Die App richtet sich nicht an Kinder unter 13 Jahren und erhebt wissentlich keine personenbezogenen Daten von Kindern.", None, None),
        ("Deine Möglichkeiten", None, [
            "Einträge löschen: Einstellungen → „Alle Einträge löschen“ oder die App löschen",
            "Werbeeinwilligung ändern: Einstellungen → „Datenschutz für Werbung“ (nur dort angezeigt, wo erforderlich)",
            "Einträge exportieren: Einstellungen → Daten exportieren → „CSV teilen“ (Pro)",
        ], None),
        ("Änderungen dieser Erklärung", "Änderungen werden auf dieser Seite mit neuem Datum unter „Zuletzt aktualisiert“ veröffentlicht.", None, None),
    ],
    privacy_contact_h="Kontakt",
    privacy_contact_p="Fragen zu dieser Erklärung kannst du über dasselbe Kontaktformular wie für den Support senden. Es ist ein Google-Formular: Deine Eingaben speichert Google, gelesen werden sie vom Entwickler. Gib eine E-Mail-Adresse nur an, wenn du eine Antwort möchtest.",
    footer="UNKO LAB — Support und Datenschutzerklärung",
)

LANGS["pt-BR"] = dict(
    title="Suporte e política de privacidade",
    lead="Um diário de evacuações para iPhone, mantido junto com o Professor Cocô.",
    nav_support="Suporte", nav_privacy="Política de privacidade",
    support_h="Suporte",
    support_intro="Respostas para as perguntas mais comuns. Se a sua não estiver aqui, use o formulário de contato no fim da página.",
    faq=[
        ("Sobre o app", [
            ("O que o UNKO LAB faz?",
             "É um diário de observação das evacuações: forma (escala de Bristol), cor, quantidade, sintomas e anotações, vistos em um calendário mensal e em uma revisão semanal. O personagem do Professor aponta padrões nos seus registros e as fontes científicas ou de saúde pública por trás deles. Cada registro faz crescer sua «Torre do Cocô Fofinho»."),
            ("É um app médico?",
             "Não. O UNKO LAB serve para observar e aprender. Ele não diagnostica, não trata nem decide sobre medicamentos. As leituras do Professor colocam em palavras um padrão dos seus registros; não substituem um profissional de saúde. Se notar sangue ou fezes escuras, diarreia com febre, dor abdominal forte ou perda de peso, procure um profissional. Em uma emergência, ligue para o número de emergência da sua região."),
            ("Como são tratados os dias sem evacuação?",
             "Um dia sem registro é automaticamente tratado como dia sem evacuação: não há nada a preencher. Se você adicionar um registro depois, ele passa a ser um dia registrado."),
        ]),
        ("Seus dados", [
            ("Onde meus registros ficam guardados?",
             "Somente no seu iPhone. Não há conta e nada é enviado a um servidor do desenvolvedor. Dependendo dos ajustes do iOS, os dados podem entrar nos backups do iCloud ou do aparelho."),
            ("Posso exportar meus registros?",
             "Ajustes → Exportar registros → «Compartilhar CSV» exporta todos os campos em um arquivo CSV (recurso Pro). Seus registros só saem do aparelho quando você os compartilha, e só para o app ou a pessoa que escolher."),
            ("Como apago meus dados?",
             "Ajustes → «Excluir todos os registros» apaga o diário do aparelho. Excluir o app faz o mesmo. O desenvolvedor não guarda nenhuma cópia, então não há nada a solicitar."),
        ]),
        ("UNKO LAB Pro (compra única)", [
            ("O que o Pro inclui?",
             "Quatro coisas: sem anúncios, uma torre que cresce 10 vezes mais rápido, exportação CSV completa e a biblioteca de estudos inteira. É um pagamento único, sem renovação automática. Registros, calendário mensal, as leituras do Professor com suas fontes e a orientação para consulta continuam grátis."),
            ("Troquei de celular e perdi o Pro",
             "Entre com a mesma conta Apple e abra Ajustes → UNKO LAB Pro → «Restaurar compras». A Apple guarda a compra, então você nunca paga duas vezes."),
            ("Quero um reembolso",
             "Todas as compras da App Store são tratadas pela Apple. Use a <a href=\"{refund}\" target=\"_blank\" rel=\"noopener\">página de solicitação de reembolso da Apple</a>."),
        ]),
        ("Anúncios", [
            ("Onde os anúncios aparecem?",
             "A versão gratuita mostra um banner na parte de baixo da aba Início. Nenhum anúncio cobre o formulário de registro nem a orientação para consulta. O Pro não carrega anúncios."),
            ("Posso mudar minhas escolhas de anúncios?",
             "Nas regiões onde o consentimento é exigido, os Ajustes mostram «Privacidade dos anúncios», que você pode mudar a qualquer momento."),
        ]),
        ("Outros", [
            ("Quais idiomas são suportados?",
             "Japonês, inglês, espanhol, francês, alemão, português (Brasil), chinês simplificado e coreano. O app segue o idioma do aparelho ou a escolha feita nos Ajustes. As fichas de estudos em idiomas que não o japonês são resumos dos pontos principais."),
            ("Encontrei um erro",
             "Use o formulário abaixo com os passos para reproduzi-lo. Ao abrir o formulário por Ajustes → «Contato» no app, o modelo do aparelho e a versão do iOS são preenchidos automaticamente."),
        ]),
    ],
    contact_h="Contato",
    contact_p="As solicitações chegam por um formulário do Google (em inglês, mas você pode escrever em português). Ao abri-lo por «Contato» nos Ajustes do app, o aparelho e a versão do iOS são preenchidos automaticamente. A resposta pode levar alguns dias.",
    cta="Abrir o formulário de contato",
    privacy_h="Política de privacidade",
    updated="Última atualização: 13 de setembro de 2026",
    privacy_intro="Esta política explica quais dados o app para iPhone «UNKO LAB» (o «app») trata e como são usados. O app é desenvolvido e publicado por um desenvolvedor independente (GitHub: ki-84).",
    sections=[
        ("Em resumo", None, [
            "Sem conta e sem servidor do desenvolvedor. Seus registros ficam só no seu aparelho.",
            "O desenvolvedor nunca recebe seus registros e não consegue vê-los.",
            "Os anúncios da versão gratuita não são personalizados, e seu diário nunca é repassado a anunciantes.",
            "O app não rastreia você.",
        ], None),
        ("Dados guardados no seu aparelho", "O app guarda, somente no aparelho, as seguintes informações que você insere:", [
            "Registros de evacuação: data e hora, forma (escala de Bristol), cor, quantidade, sangue, dor abdominal, esforço, urgência, evacuação incompleta, muco, evacuações noturnas, tempo gasto, uso de laxante nas últimas 24 horas, febre, vômito, desidratação, gases, perda de peso, anotações sobre comida e remédios, etiquetas e texto livre",
            "Ajustes do app: idioma de exibição, progresso da torre e afins",
        ], "Nada disso é enviado ao desenvolvedor. Dependendo dos ajustes do iOS, pode entrar nos backups do iCloud ou do aparelho, que seguem as políticas da Apple."),
        ("Compartilhamento", "Seus registros só saem do aparelho quando você usa uma ação de compartilhar, como «Compartilhar CSV» nos Ajustes, e só para o app ou a pessoa que escolher. O tratamento posterior segue as políticas desse destinatário.", None, None),
        ("Compras", "O UNKO LAB Pro é vendido pela App Store da Apple. O app recebe apenas se a compra está ativa — nunca seu nome ou dados de pagamento. Veja a <a href=\"https://www.apple.com/legal/privacy/\" target=\"_blank\" rel=\"noopener\">política de privacidade da Apple</a>.", None, None),
        ("Publicidade (versão gratuita)", "A versão gratuita mostra um banner na parte de baixo da aba Início usando o SDK Mobile Ads do Google (AdMob).", [
            "Toda solicitação de anúncio é configurada como não personalizada (<code>npa=1</code>). O app não pede a permissão de App Tracking Transparency.",
            "Para entregar, medir e proteger os anúncios, o SDK pode enviar ao Google informações do aparelho: modelo, versão do sistema, endereço IP, uma região aproximada derivada do IP, e exibições e toques nos anúncios.",
            "No EEE, no Reino Unido, na Suíça e em outras regiões onde o consentimento é exigido, ele é coletado pela User Messaging Platform do Google. Você pode mudá-lo a qualquer momento em «Privacidade dos anúncios», nos Ajustes.",
            "O código de publicidade não tem acesso aos seus registros. Nem seus registros nem suas perguntas ao Professor são repassados a anunciantes.",
            "O Pro não carrega anúncios.",
        ], "Sobre o tratamento de dados pelo Google, veja a <a href=\"{gpriv}\" target=\"_blank\" rel=\"noopener\">Política de Privacidade do Google</a> e <a href=\"{gpartner}\" target=\"_blank\" rel=\"noopener\">Como o Google usa informações de sites ou apps que utilizam seus serviços</a>."),
        ("Informações de saúde", "Registros de evacuação são informações relacionadas à saúde. O app os usa apenas para registrar, exibir e revisar no seu aparelho — nunca para publicidade ou repasse a terceiros. O app não se conecta ao Apple HealthKit. Nada no app é orientação médica nem substitui diagnóstico ou tratamento.", None, None),
        ("Links externos", "Links como «Abrir a fonte original» nas fichas de estudos abrem sites externos no seu navegador. Valem as políticas desses sites.", None, None),
        ("Privacidade de crianças", "O app não é destinado a menores de 13 anos e não coleta conscientemente informações pessoais de crianças.", None, None),
        ("Suas escolhas", None, [
            "Apagar seus registros: Ajustes → «Excluir todos os registros», ou excluir o app",
            "Mudar o consentimento de anúncios: Ajustes → «Privacidade dos anúncios» (mostrado só onde é exigido)",
            "Exportar seus registros: Ajustes → Exportar registros → «Compartilhar CSV» (Pro)",
        ], None),
        ("Mudanças nesta política", "As mudanças serão publicadas nesta página com uma nova data de «Última atualização».", None, None),
    ],
    privacy_contact_h="Contato",
    privacy_contact_p="Perguntas sobre esta política podem ser enviadas pelo mesmo formulário de contato do suporte. É um formulário do Google: o que você escreve fica armazenado no Google e é lido pelo desenvolvedor. Informe um e-mail só se quiser resposta.",
    footer="UNKO LAB — Suporte e política de privacidade",
)

LANGS["zh-Hans"] = dict(
    title="支持与隐私政策",
    lead="和便便博士一起记录的 iPhone 排便观察日记。",
    nav_support="支持", nav_privacy="隐私政策",
    support_h="支持",
    support_intro="这里整理了常见问题。如果没有你要找的，请使用页面底部的联系表单。",
    faq=[
        ("关于本应用", [
            ("UNKO LAB 是做什么的？",
             "它是一本排便观察日记：记录形状（布里斯托分类）、颜色、量、症状和备注，并在月历和每周回顾中查看。博士这个角色会指出你记录中的规律，以及背后的研究或公共卫生资料。每记录一次，你的「软乎乎便便塔」就会长高。"),
            ("这是医疗应用吗？",
             "不是。UNKO LAB 用于观察和学习，不做诊断、不做治疗，也不对用药做判断。博士的「解读」只是把记录中的规律说出来，不能替代医疗人员的判断。如果出现血便或黑便、伴有发热的腹泻、剧烈腹痛或体重下降，请去医疗机构就诊。紧急情况请拨打当地急救电话。"),
            ("没有排便的日子怎么处理？",
             "没有记录的日子会自动视为「未排便」，无需输入。之后补上记录，它就变成有记录的一天。"),
        ]),
        ("你的数据", [
            ("记录保存在哪里？",
             "只保存在你的 iPhone 上。不需要账户，也不会发送到开发者的服务器。根据 iOS 的设置，数据可能会包含在 iCloud 或设备备份中。"),
            ("可以导出记录吗？",
             "设置 → 导出记录 → 「分享CSV」可以把全部字段导出为 CSV 文件（Pro 功能）。只有在你执行分享操作时，记录才会离开设备，并且只发送给你选择的应用或对象。"),
            ("怎么删除数据？",
             "设置 → 「删除所有记录」会清除设备上的日记。删除应用也是一样。开发者没有任何副本，所以无需提出删除请求。"),
        ]),
        ("UNKO LAB Pro（一次性购买）", [
            ("Pro 包含什么？",
             "四项：无广告、塔的增长变为10倍、全部字段的 CSV 导出、阅读全部收录文献。一次付款，没有自动续费。记录、月历、博士的解读及其出处和就诊提示将继续免费。"),
            ("换了手机后 Pro 没了",
             "用同一个 Apple 账户登录，然后打开设置 → UNKO LAB Pro → 「恢复购买」。购买记录由 Apple 保管，不会重复付费。"),
            ("我想退款",
             "App Store 的购买全部由 Apple 处理。请使用 <a href=\"{refund}\" target=\"_blank\" rel=\"noopener\">Apple 的退款申请页面</a>。"),
        ]),
        ("广告", [
            ("广告显示在哪里？",
             "免费版在首页标签页底部显示一条横幅广告。广告不会遮挡记录表单或就诊提示。Pro 不加载广告。"),
            ("可以更改广告设置吗？",
             "在需要征得同意的地区，设置里会显示「广告隐私设置」，随时可以更改。"),
        ]),
        ("其他", [
            ("支持哪些语言？",
             "日语、英语、西班牙语、法语、德语、葡萄牙语（巴西）、简体中文和韩语。应用会跟随设备语言，也可以在设置中选择。日语以外版本的文献卡片是要点摘要。"),
            ("我发现了问题",
             "请通过下面的表单告诉我们，并附上重现步骤。从应用的设置 → 「联系我们」打开表单时，机型和 iOS 版本会自动填入。"),
        ]),
    ],
    contact_h="联系我们",
    contact_p="通过 Google 表单接收（表单是英文的，但可以用中文填写）。从应用设置中的「联系我们」打开时，设备和 iOS 版本会自动填入。回复可能需要几天。",
    cta="打开联系表单",
    privacy_h="隐私政策",
    updated="最后更新：2026年9月13日",
    privacy_intro="本政策说明 iPhone 应用「UNKO LAB」（以下称「本应用」）处理哪些数据以及如何使用。本应用由独立开发者（GitHub: ki-84）开发和发布。",
    sections=[
        ("要点", None, [
            "不需要账户，也没有开发者的服务器。你的记录只保存在你的设备上。",
            "开发者不会收到你的记录，也无法查看。",
            "免费版的广告是非个性化的，你的排便记录绝不会提供给广告商。",
            "本应用不跟踪用户。",
        ], None),
        ("保存在设备上的数据", "本应用只在设备上保存你输入的以下信息：", [
            "排便记录：日期时间、形状（布里斯托分类）、颜色、量、便血、腹痛、用力、急迫感、排便不尽感、黏液、夜间排便、所用时间、24小时内是否用过泻药、发热、呕吐、脱水感、排气、体重下降、饮食和用药备注、标签、自由文本",
            "应用设置：显示语言、塔的进度等",
        ], "这些信息不会发送给开发者。根据 iOS 的设置，可能会包含在 iCloud 或设备备份中，备份遵循 Apple 的政策。"),
        ("分享", "只有当你执行分享操作（例如设置中的「分享CSV」）时，记录才会离开设备，并且只发送给你选择的应用或对象。之后的处理遵循该接收方的政策。", None, None),
        ("购买", "UNKO LAB Pro 通过 Apple 的 App Store 销售。本应用只会收到「是否已购买」的信息，不会收到你的姓名或支付信息。详见 <a href=\"https://www.apple.com/legal/privacy/\" target=\"_blank\" rel=\"noopener\">Apple 隐私政策</a>。", None, None),
        ("广告（免费版）", "免费版通过 Google Mobile Ads SDK（AdMob）在首页标签页底部显示横幅广告。", [
            "所有广告请求都设置为非个性化（<code>npa=1</code>）。本应用不会请求 App Tracking Transparency 的跟踪许可。",
            "为了投放、统计和保护广告，SDK 可能会向 Google 发送设备信息：机型、系统版本、IP 地址、根据 IP 推测的大致地区，以及广告的展示和点击。",
            "在欧洲经济区、英国、瑞士等需要征得同意的地区，会通过 Google 的 User Messaging Platform 收集同意。你可以随时在设置中的「广告隐私设置」更改。",
            "广告代码无法访问你的排便记录。你的记录和向博士提出的问题绝不会交给广告商。",
            "Pro 不加载广告。",
        ], "关于 Google 对数据的处理，请参阅 <a href=\"{gpriv}\" target=\"_blank\" rel=\"noopener\">Google 隐私权政策</a>和<a href=\"{gpartner}\" target=\"_blank\" rel=\"noopener\">Google 如何使用来自使用其服务的网站或应用的信息</a>。"),
        ("健康信息", "排便记录属于与健康相关的信息。本应用只在你的设备上用于记录、显示和回顾，绝不用于广告或提供给第三方。本应用不连接 Apple HealthKit。应用中的内容不是医疗建议，也不能替代诊断或治疗。", None, None),
        ("外部链接", "文献卡片上的「打开原文」等链接会在你的浏览器中打开外部网站，适用各网站自己的政策。", None, None),
        ("儿童隐私", "本应用不面向13岁以下儿童，也不会有意收集儿童的个人信息。", None, None),
        ("你可以做的", None, [
            "删除记录：设置 → 「删除所有记录」，或删除应用",
            "更改广告同意：设置 → 「广告隐私设置」（仅在需要的地区显示）",
            "导出记录：设置 → 导出记录 → 「分享CSV」（Pro）",
        ], None),
        ("本政策的变更", "变更会发布在本页面，并更新「最后更新」日期。", None, None),
    ],
    privacy_contact_h="联系我们",
    privacy_contact_p="关于本政策的问题，可以通过与支持相同的联系表单发送。该表单是 Google 表单，你填写的内容由 Google 存储，并由开发者阅读。只有在希望得到回复时才需要填写电子邮件地址。",
    footer="UNKO LAB — 支持与隐私政策",
)

LANGS["ko"] = dict(
    title="지원 및 개인정보 처리방침",
    lead="응가 박사와 함께 쓰는 iPhone용 배변 관찰 일기입니다.",
    nav_support="지원", nav_privacy="개인정보 처리방침",
    support_h="지원",
    support_intro="자주 묻는 질문을 모았습니다. 찾는 내용이 없으면 맨 아래 문의 양식을 이용해 주세요.",
    faq=[
        ("앱 소개", [
            ("UNKO LAB은 무엇을 하는 앱인가요?",
             "배변의 모양(브리스톨 척도)·색·양·증상·메모를 기록하고, 월간 달력과 주간 돌아보기로 살펴보는 관찰 일기입니다. 박사 캐릭터가 기록의 패턴과 그 근거가 되는 연구·공공 보건 자료를 알려 줍니다. 기록할수록 「말랑말랑 응가탑」이 높아집니다."),
            ("의료 앱인가요?",
             "아닙니다. UNKO LAB은 관찰과 학습을 위한 앱으로, 진단·치료·약에 관한 판단을 하지 않습니다. 박사의 「해석」은 기록의 패턴을 말로 옮긴 것이며 의료인의 판단을 대신하지 않습니다. 혈변이나 검은 변, 열을 동반한 설사, 심한 복통, 체중 감소가 있으면 의료기관을 방문해 주세요. 응급 상황에는 지역의 응급 번호로 연락하세요."),
            ("배변이 없는 날은 어떻게 처리되나요?",
             "기록이 없는 날은 입력 없이 자동으로 「배변 없는 날」로 처리됩니다. 나중에 기록을 추가하면 그날의 기록으로 바뀝니다."),
        ]),
        ("데이터", [
            ("기록은 어디에 저장되나요?",
             "사용 중인 iPhone 안에만 저장됩니다. 계정이 필요 없고, 개발자의 서버로 전송하지 않습니다. iOS 백업 설정에 따라 iCloud나 기기 백업에 포함될 수 있습니다."),
            ("기록을 내보내고 싶어요",
             "설정 → 기록 내보내기 → 「CSV 공유」로 전체 항목을 CSV 파일로 공유할 수 있습니다(Pro 기능). 공유 조작을 했을 때만, 선택한 상대나 앱으로 기록이 전달됩니다."),
            ("기록을 지우고 싶어요",
             "설정 → 「모든 기록 삭제」로 기기 안의 기록을 지울 수 있습니다. 앱을 삭제해도 지워집니다. 개발자 쪽에는 기록이 없으므로 삭제 요청은 필요 없습니다."),
        ]),
        ("UNKO LAB Pro (일회성 구매)", [
            ("Pro에서는 무엇이 달라지나요?",
             "광고 없음, 탑이 10배로 자람, 전체 항목 CSV 내보내기, 수록 문헌 전체 읽기, 이 네 가지입니다. 한 번만 결제하며 자동 갱신은 없습니다. 기록·월간 달력·박사의 해석과 출처·진료 안내는 앞으로도 무료입니다."),
            ("기기를 바꿨더니 Pro가 사라졌어요",
             "같은 Apple 계정으로 로그인한 뒤 설정 → UNKO LAB Pro → 「구매 복원」을 눌러 주세요. 구매는 Apple이 관리하므로 다시 결제할 필요가 없습니다."),
            ("환불하고 싶어요",
             "App Store 구매는 모두 Apple이 처리합니다. <a href=\"{refund}\" target=\"_blank\" rel=\"noopener\">Apple 환불 요청 페이지</a>에서 진행해 주세요."),
        ]),
        ("광고", [
            ("광고는 어디에 나오나요?",
             "무료 버전에서는 홈 탭 하단에 배너 광고가 하나 표시됩니다. 기록 입력 화면이나 진료 안내를 가리는 광고는 없습니다. Pro에서는 광고를 불러오지 않습니다."),
            ("광고 설정을 바꾸고 싶어요",
             "동의 확인이 필요한 지역에서는 설정에 「광고 개인정보 설정」이 표시되며 언제든지 바꿀 수 있습니다."),
        ]),
        ("기타", [
            ("지원 언어는 무엇인가요?",
             "일본어·영어·스페인어·프랑스어·독일어·포르투갈어(브라질)·중국어 간체·한국어입니다. 기기 언어를 따르거나 설정에서 고를 수 있습니다. 일본어 이외의 문헌 카드는 요점을 번역한 것입니다."),
            ("오류를 발견했어요",
             "재현 절차를 적어 아래 양식으로 알려 주세요. 앱의 설정 → 「문의하기」에서 열면 기종과 iOS 버전이 자동으로 들어갑니다."),
        ]),
    ],
    contact_h="문의",
    contact_p="Google 설문지로 접수합니다(영어 양식이지만 한국어로 써도 됩니다). 앱 설정의 「문의하기」에서 열면 기기와 iOS 버전이 자동으로 들어갑니다. 답장까지 며칠 걸릴 수 있습니다.",
    cta="문의 양식 열기",
    privacy_h="개인정보 처리방침",
    updated="최종 업데이트: 2026년 9월 13일",
    privacy_intro="이 방침은 iPhone 앱 「UNKO LAB」(이하 「앱」)이 어떤 데이터를 다루고 어떻게 사용하는지 설명합니다. 앱은 개인 개발자(GitHub: ki-84)가 개발·배포합니다.",
    sections=[
        ("요점", None, [
            "계정이 필요 없고 개발자의 서버도 없습니다. 기록은 기기 안에만 저장됩니다.",
            "개발자는 여러분의 기록을 받지 않으며 볼 수도 없습니다.",
            "무료 버전의 광고는 비개인화이며, 배변 기록을 광고사에 넘기지 않습니다.",
            "앱은 사용자를 추적하지 않습니다.",
        ], None),
        ("기기에 저장되는 데이터", "앱은 여러분이 입력한 다음 정보를 기기 안에만 저장합니다.", [
            "배변 기록: 일시, 모양(브리스톨 척도), 색, 양, 혈액·복통·힘주기·급박감·잔변감·점액·야간 배변, 소요 시간, 24시간 이내 완하제, 발열·구토·탈수감·가스·체중 감소 여부, 식사·약 메모, 태그, 자유 기술",
            "앱 설정: 표시 언어, 탑의 진행 상황 등",
        ], "이 정보는 개발자에게 전송되지 않습니다. iOS 백업 설정에 따라 iCloud 백업이나 기기 백업에 포함될 수 있으며, 백업은 Apple의 방침을 따릅니다."),
        ("공유", "설정의 「CSV 공유」처럼 여러분이 공유 조작을 했을 때만, 선택한 상대나 앱으로 기록이 전달됩니다. 이후의 취급은 그 상대나 앱의 방침을 따릅니다.", None, None),
        ("구매", "UNKO LAB Pro 구매는 Apple의 App Store가 처리합니다. 앱이 받는 것은 「구매 여부」뿐이며, 이름이나 결제 정보는 받지 않습니다. 자세한 내용은 <a href=\"https://www.apple.com/legal/privacy/\" target=\"_blank\" rel=\"noopener\">Apple 개인정보 처리방침</a>을 참고하세요.", None, None),
        ("광고 (무료 버전)", "무료 버전은 Google Mobile Ads SDK(AdMob)를 통해 홈 탭 하단에 배너 광고를 표시합니다.", [
            "모든 광고 요청은 비개인화(<code>npa=1</code>)로 설정되어 있습니다. App Tracking Transparency의 추적 허용을 요청하지 않습니다.",
            "광고 SDK는 광고의 게재·측정·부정 방지를 위해 기기 정보(기종, OS 버전, IP 주소, IP로 추정한 대략적인 지역, 광고 노출·탭)를 Google에 보낼 수 있습니다.",
            "EEA·영국·스위스 등 동의 확인이 필요한 지역에서는 Google의 User Messaging Platform으로 동의를 확인합니다. 설정의 「광고 개인정보 설정」에서 언제든지 바꿀 수 있습니다.",
            "광고 코드는 배변 기록에 접근할 수 없도록 만들어져 있으며, 기록 내용이나 박사에게 한 질문을 광고사에 넘기지 않습니다.",
            "Pro에서는 광고를 불러오지 않습니다.",
        ], "Google의 데이터 취급은 <a href=\"{gpriv}\" target=\"_blank\" rel=\"noopener\">Google 개인정보처리방침</a>과 <a href=\"{gpartner}\" target=\"_blank\" rel=\"noopener\">Google 서비스를 사용하는 사이트나 앱에서 수집한 정보를 Google이 사용하는 방식</a>을 참고하세요."),
        ("건강 정보의 취급", "배변 기록은 건강과 관련된 정보입니다. 앱은 이를 기기 안에서의 기록·표시·돌아보기에만 사용하며, 광고나 제3자 제공에는 사용하지 않습니다. Apple HealthKit과 연결하지 않습니다. 앱의 내용은 의학적 조언이 아니며 진단·치료를 대신하지 않습니다.", None, None),
        ("외부 링크", "문헌 카드의 「원문 열기」 같은 링크는 사용 중인 브라우저에서 외부 사이트를 엽니다. 링크 대상의 취급은 각 사이트의 방침을 따릅니다.", None, None),
        ("어린이의 개인정보", "앱은 13세 미만 어린이를 대상으로 하지 않으며, 어린이의 개인정보를 의도적으로 수집하지 않습니다.", None, None),
        ("여러분이 할 수 있는 것", None, [
            "기록 삭제: 설정 → 「모든 기록 삭제」, 또는 앱 삭제",
            "광고 동의 변경: 설정 → 「광고 개인정보 설정」(표시되는 지역만)",
            "기록 내보내기: 설정 → 기록 내보내기 → 「CSV 공유」(Pro)",
        ], None),
        ("방침의 변경", "내용을 바꿀 때는 이 페이지를 갱신하고 최종 업데이트 날짜를 고칩니다.", None, None),
    ],
    privacy_contact_h="문의",
    privacy_contact_p="이 방침에 관한 질문은 지원과 같은 문의 양식으로 받습니다. 양식은 Google 설문지이며, 입력 내용은 Google에 저장되고 개발자가 읽습니다. 이메일 주소는 답장을 원할 때만 적어 주세요.",
    footer="UNKO LAB — 지원 및 개인정보 처리방침",
)

assert list(LANGS) == ORDER, "LANGS の順序を ORDER に揃える"

STYLE = """
  :root {
    --bg: #f6f2ea; --surface: #ffffff; --surface-2: #ece6d8;
    --ink: #1f2a27; --ink-dim: #5d6a66; --accent: #1f615a;
    --line: rgba(31,42,39,0.14);
    --shadow: 0 1px 2px rgba(31,42,39,0.06), 0 8px 24px rgba(31,42,39,0.05);
    --radius: 14px;
    --font-body: -apple-system, "Hiragino Sans", "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  }
  @media (prefers-color-scheme: dark) {
    :root {
      --bg: #151a19; --surface: #1d2422; --surface-2: #26302d;
      --ink: #e9ece8; --ink-dim: #9fada8; --accent: #7fc4b8;
      --line: rgba(233,236,232,0.12);
      --shadow: 0 1px 2px rgba(0,0,0,0.3), 0 10px 30px rgba(0,0,0,0.35);
    }
  }
  * { box-sizing: border-box; }
  html { scroll-behavior: smooth; }
  body { margin: 0; background: var(--bg); color: var(--ink); font-family: var(--font-body); line-height: 1.7; -webkit-font-smoothing: antialiased; }
  a { color: var(--accent); }
  header.hero { max-width: 720px; margin: 0 auto; padding: 40px 24px 20px; }
  .eyebrow { font-size: 12px; letter-spacing: 0.18em; text-transform: uppercase; color: var(--accent); margin-bottom: 8px; font-weight: 700; }
  h1 { font-size: clamp(24px, 5vw, 34px); margin: 0 0 10px; letter-spacing: -0.01em; }
  .lead { color: var(--ink-dim); margin: 0 0 14px; }
  nav.jump { display: flex; flex-wrap: wrap; gap: 8px 16px; font-size: 14px; margin-bottom: 6px; }
  .lang { display: flex; flex-wrap: wrap; gap: 6px; margin: 14px 0 0; }
  .lang button { border: 1px solid var(--line); background: var(--surface); color: var(--ink); padding: 6px 12px; border-radius: 999px; font: inherit; font-size: 13px; cursor: pointer; }
  .lang button[aria-pressed="true"] { background: var(--accent); border-color: var(--accent); color: #fff; }
  main { max-width: 720px; margin: 0 auto; padding: 0 24px 64px; }
  section.card { background: var(--surface); border: 1px solid var(--line); border-radius: var(--radius); box-shadow: var(--shadow); padding: 28px 26px; margin-bottom: 22px; }
  section.card .tag { font-size: 12px; letter-spacing: 0.14em; text-transform: uppercase; color: var(--accent); font-weight: 700; margin-bottom: 4px; }
  section.card h2 { margin: 0 0 12px; font-size: 22px; }
  section.card h3 { margin: 22px 0 8px; font-size: 16px; }
  section.card p { margin: 0 0 12px; }
  section.card ul { margin: 0 0 12px; padding-left: 1.2em; }
  section.card li { margin-bottom: 6px; }
  .q { font-weight: 700; margin-bottom: 2px; }
  .a { color: var(--ink-dim); }
  .cta { display: inline-block; background: var(--accent); color: #fff; text-decoration: none; padding: 10px 18px; border-radius: 999px; font-weight: 700; }
  .meta { font-size: 13px; color: var(--ink-dim); }
  footer.foot { max-width: 720px; margin: 0 auto; padding: 0 24px 40px; font-size: 13px; color: var(--ink-dim); }
  [hidden] { display: none !important; }
"""


def block(code, t):
    """1言語ぶんの見出し・サポート・ポリシー。"""
    refund, gpriv, gpartner = REFUND[code], f"https://policies.google.com/privacy?hl={GOOGLE_HL[code]}", f"https://policies.google.com/technologies/partner-sites?hl={GOOGLE_HL[code]}"
    fmt = lambda s: s.format(refund=refund, gpriv=gpriv, gpartner=gpartner)
    out = [f'<div data-lang="{code}" lang="{HTML_LANG[code]}" hidden>']
    out.append(f'<header class="hero"><div class="eyebrow">UNKO LAB</div><h1>{t["title"]}</h1><p class="lead">{t["lead"]}</p>'
               f'<nav class="jump"><a href="#support-{code}">{t["nav_support"]}</a><a href="#privacy-{code}">{t["nav_privacy"]}</a></nav>'
               f'<div class="lang" role="group" aria-label="Language">' + "".join(f'<button type="button" data-set-lang="{c}" aria-pressed="{str(c == code).lower()}">{NAMES[c]}</button>' for c in ORDER) + '</div></header>')
    out.append('<main>')
    # サポート
    out.append(f'<section class="card" id="support-{code}"><div class="tag">Support</div><h2>{t["support_h"]}</h2><p>{t["support_intro"]}</p>')
    for heading, qas in t["faq"]:
        out.append(f'<h3>{heading}</h3>')
        for q, a in qas:
            out.append(f'<p class="q">{q}</p><p class="a">{fmt(a)}</p>')
    out.append(f'<h3>{t["contact_h"]}</h3><p>{t["contact_p"]}</p><a class="cta" href="{FORM}" target="_blank" rel="noopener">{t["cta"]}</a></section>')
    # ポリシー
    out.append(f'<section class="card" id="privacy-{code}"><div class="tag">Privacy Policy</div><h2>{t["privacy_h"]}</h2><p class="meta">{t["updated"]}</p><p>{t["privacy_intro"]}</p>')
    for heading, lead, items, trailer in t["sections"]:
        out.append(f'<h3>{heading}</h3>')
        if lead: out.append(f'<p>{fmt(lead)}</p>')
        if items: out.append('<ul>' + "".join(f'<li>{fmt(i)}</li>' for i in items) + '</ul>')
        if trailer: out.append(f'<p>{fmt(trailer)}</p>')
    out.append(f'<h3>{t["privacy_contact_h"]}</h3><p>{t["privacy_contact_p"]}</p><a class="cta" href="{FORM}" target="_blank" rel="noopener">{t["cta"]}</a></section>')
    out.append(f'</main><footer class="foot">{t["footer"]}</footer></div>')
    return "\n".join(out)


SCRIPT = """
(function () {
  var order = %s;
  function show(lang) {
    document.documentElement.lang = lang;
    document.querySelectorAll('[data-lang]').forEach(function (el) { el.hidden = el.getAttribute('data-lang') !== lang; });
    document.querySelectorAll('[data-set-lang]').forEach(function (b) { b.setAttribute('aria-pressed', String(b.getAttribute('data-set-lang') === lang)); });
    try { localStorage.setItem('lang', lang); } catch (e) {}
  }
  document.querySelectorAll('[data-set-lang]').forEach(function (b) {
    b.addEventListener('click', function () { show(b.getAttribute('data-set-lang')); });
  });
  function fromHash(hash) {
    var m = hash.match(/^#(?:support|privacy)(?:-([A-Za-z-]+))?$/);
    if (!m) return null;
    return m[1] && order.indexOf(m[1]) >= 0 ? m[1] : (m[1] ? null : 'ja');
  }
  function fromBrowser() {
    var l = (navigator.language || 'en').toLowerCase();
    if (l.indexOf('ja') === 0) return 'ja';
    if (l.indexOf('es') === 0) return 'es';
    if (l.indexOf('fr') === 0) return 'fr';
    if (l.indexOf('de') === 0) return 'de';
    if (l.indexOf('pt') === 0) return 'pt-BR';
    if (l.indexOf('zh') === 0) return 'zh-Hans';
    if (l.indexOf('ko') === 0) return 'ko';
    return 'en';
  }
  var wanted = fromHash(location.hash);
  if (!wanted) { try { wanted = localStorage.getItem('lang'); } catch (e) {} }
  if (!wanted || order.indexOf(wanted) < 0) wanted = fromBrowser();
  show(wanted);
  if (location.hash) {
    var id = location.hash.slice(1);
    if (id === 'support' || id === 'privacy') id += '-ja';
    var t = document.getElementById(id); if (t) t.scrollIntoView();
  }
  var ua = (navigator.userAgent || '').match(/iPhone OS (\\d+)_(\\d+)/);
  if (ua) {
    document.querySelectorAll('a.cta').forEach(function (a) {
      a.href += '?usp=pp_url&%s=' + encodeURIComponent('iPhone / iOS ' + ua[1] + '.' + ua[2]);
    });
  }
})();
""" % (str(ORDER).replace("'", '"'), DEVICE_FIELD)


def build():
    parts = ['<!doctype html>', '<html lang="ja">', '<head>', '<meta charset="utf-8">',
             '<meta name="viewport" content="width=device-width, initial-scale=1">',
             '<title>UNKO LAB — Support &amp; Privacy Policy</title>',
             '<meta name="description" content="Support and privacy policy for UNKO LAB, a bowel-movement diary for iPhone. サポートとプライバシーポリシー。">',
             '<style>' + STYLE + '</style>', '</head>', '<body>']
    for code in ORDER:
        parts.append(block(code, LANGS[code]))
    # JS なしでも読めるよう、英語だけは最初から表示しておく
    parts.append('<noscript><style>[data-lang="en"] { display: block !important; }</style></noscript>')
    parts.append('<script>' + SCRIPT + '</script>')
    parts.append('</body></html>')
    Path(__file__).with_name('index.html').write_text("\n".join(parts) + "\n", encoding='utf-8')
    print('index.html:', len(ORDER), 'languages')


if __name__ == '__main__':
    build()
