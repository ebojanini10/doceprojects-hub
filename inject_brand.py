from pathlib import Path

src = Path(r"C:\Users\Eboja\AppData\Local\Temp\doceprojects-hub\entrenoos\entrenoos-hub-clean.html")
html = src.read_text(encoding="utf-8")

fonts = """    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,900;1,9..144,300&family=Plus+Jakarta+Sans:wght@400;600;700&family=Fira+Code:wght@400&display=swap" rel="stylesheet">"""

brand_css = """    <style id="entrenos-brand">
        html, body { height: 100%; margin: 0; padding: 0; }
        .staticrypt-body {
            background: #0f1013 !important;
            display: flex !important;
            flex-direction: column !important;
            align-items: center !important;
            justify-content: center !important;
            min-height: 100vh !important;
            padding: 24px !important;
            font-family: 'Plus Jakarta Sans', sans-serif !important;
            -webkit-font-smoothing: antialiased;
        }
        @keyframes fadeUp {
            from { opacity: 0; transform: translateY(14px); }
            to   { opacity: 1; transform: translateY(0); }
        }
        @keyframes glowPulse {
            0%, 100% { box-shadow: 0 0 0 0 rgba(201,168,76,0); }
            50%       { box-shadow: 0 0 0 6px rgba(201,168,76,0.14); }
        }
        .en-logo { margin-bottom: 28px; text-align: center; position: relative; z-index: 1; animation: fadeUp 0.5s ease both; }
        .en-logo-mark { display: inline-flex; align-items: baseline; }
        .en-logo .entre { font-family: 'Fraunces', serif; font-style: italic; font-weight: 300; font-size: clamp(2.4rem, 10vw, 3.2rem); color: #C9A84C; }
        .en-logo .nos { font-family: 'Fraunces', serif; font-style: normal; font-weight: 900; font-size: clamp(2.4rem, 10vw, 3.2rem); color: #F0E6CC; letter-spacing: -0.05em; }
        .en-tagline { font-family: 'Fira Code', monospace; font-size: 0.68rem; letter-spacing: 0.16em; text-transform: uppercase; color: #5c6070; margin-top: 8px; }
        #staticrypt_content { position: relative; z-index: 1; width: 100%; display: flex; flex-direction: column; align-items: center; }
        .staticrypt-page { width: 100% !important; max-width: 420px !important; padding: 0 !important; margin: 0 !important; animation: fadeUp 0.5s 0.07s ease both; }
        .staticrypt-form {
            background: #1c1e24 !important;
            border: 1px solid #252830 !important;
            border-top: 2px solid rgba(201,168,76,0.4) !important;
            border-radius: 20px !important;
            padding: 32px 28px 36px !important;
            max-width: none !important;
            margin: 0 !important;
            box-shadow: none !important;
            text-align: left !important;
        }
        .en-lock { width: 44px; height: 44px; margin: 0 auto 18px; display: flex; align-items: center; justify-content: center; background: rgba(201,168,76,0.1); border: 1px solid rgba(201,168,76,0.25); border-radius: 12px; }
        .en-lock svg { width: 20px; height: 20px; stroke: #E8C96A; fill: none; stroke-width: 1.75; stroke-linecap: round; stroke-linejoin: round; }
        .staticrypt-instructions { background: rgba(201,168,76,0.07) !important; border: 1px solid rgba(201,168,76,0.18) !important; border-radius: 10px !important; padding: 14px 16px !important; margin-bottom: 24px !important; }
        .staticrypt-title { font-family: 'Fira Code', monospace !important; font-size: 0.62rem !important; letter-spacing: 0.12em !important; text-transform: uppercase !important; color: #E8C96A !important; margin-bottom: 6px !important; }
        .staticrypt-instructions > p:last-child { font-family: 'Fira Code', monospace !important; font-size: 0.78rem !important; color: #c8cad4 !important; line-height: 1.7 !important; margin: 0 !important; }
        .en-field-label { display: block; font-family: 'Fira Code', monospace; font-size: 0.7rem; letter-spacing: 0.1em; text-transform: uppercase; color: #a0a3ad; margin-bottom: 8px; }
        .staticrypt-form input[type="password"],
        .staticrypt-form input[type="text"],
        input[type="password"],
        input[type="text"] {
            width: 100% !important;
            padding: 15px 18px !important;
            background: #272a32 !important;
            border: 2px solid rgba(201,168,76,0.55) !important;
            border-radius: 12px !important;
            color: #F0E6CC !important;
            font-family: 'Plus Jakarta Sans', sans-serif !important;
            font-size: 1rem !important;
            outline: none !important;
            box-sizing: border-box !important;
            transition: border-color 0.2s, box-shadow 0.2s !important;
            caret-color: #E8C96A !important;
            animation: glowPulse 2.5s 1s ease infinite !important;
        }
        .staticrypt-form input[type="password"]:focus,
        .staticrypt-form input[type="text"]:focus,
        input[type="password"]:focus,
        input[type="text"]:focus {
            border-color: #E8C96A !important;
            box-shadow: 0 0 0 4px rgba(201,168,76,0.18) !important;
            animation: none !important;
        }
        .staticrypt-form input[type="password"]::placeholder,
        input[type="password"]::placeholder { color: #7a7e8a !important; font-style: italic !important; }
        .staticrypt-password-container { position: relative; margin-bottom: 14px; }
        .staticrypt-decrypt-button,
        .staticrypt-form input[type="submit"],
        .staticrypt-form button {
            width: 100% !important;
            padding: 15px !important;
            background: #C9A84C !important;
            color: #0a0b0d !important;
            font-family: 'Plus Jakarta Sans', sans-serif !important;
            font-weight: 800 !important;
            font-size: 0.94rem !important;
            letter-spacing: 0.04em !important;
            border: none !important;
            border-radius: 12px !important;
            cursor: pointer !important;
            transition: background 0.2s, transform 0.15s, box-shadow 0.2s !important;
            box-shadow: none !important;
        }
        .staticrypt-decrypt-button:hover { background: #E8C96A !important; transform: translateY(-1px) !important; box-shadow: 0 6px 24px rgba(201,168,76,0.32) !important; }
        .staticrypt-decrypt-button:active { transform: translateY(0) !important; }
        .staticrypt-error { color: #ff6b6b !important; font-family: 'Fira Code', monospace !important; font-size: 0.8rem !important; background: rgba(255,107,107,0.08) !important; border: 1px solid rgba(255,107,107,0.2) !important; border-radius: 8px !important; padding: 10px 14px !important; margin-top: 12px !important; text-align: center !important; }
        .staticrypt-hr { display: none !important; }
        .en-footer { margin-top: 20px; font-family: 'Fira Code', monospace; font-size: 0.6rem; color: #353840; letter-spacing: 0.06em; text-align: center; position: relative; z-index: 1; }
        @media (max-width: 480px) {
            .staticrypt-form { padding: 24px 16px 28px !important; }
            .en-logo .entre, .en-logo .nos { font-size: 2.6rem; }
        }
    </style>"""

# 1. fonts + css before </head>
html = html.replace("    </head>", fonts + "\n" + brand_css + "\n    </head>")

# 2. logo before .staticrypt-page
logo_html = (
    '\n        <div class="en-logo">'
    '\n            <div class="en-logo-mark">'
    '<span class="entre">entre</span><span class="nos">Nos</span>'
    '</div>'
    '\n            <div class="en-tagline">el dinero vuelve a ser de la gente</div>'
    '\n        </div>\n'
)
html = html.replace(
    '<div class="staticrypt-page">',
    logo_html + '        <div class="staticrypt-page">'
)

# 3. lock icon before instructions
lock = (
    '                    <div class="en-lock">'
    '<svg viewBox="0 0 24 24">'
    '<rect x="3" y="11" width="18" height="11" rx="2" ry="2"/>'
    '<path d="M7 11V7a5 5 0 0 1 10 0v4"/>'
    '</svg></div>\n'
)
html = html.replace(
    '<div class="staticrypt-instructions">',
    lock + '                    <div class="staticrypt-instructions">'
)

# 4. field label before password container
label = '                        <label class="en-field-label">contrasena</label>\n'
html = html.replace(
    '<div class="staticrypt-password-container">',
    label + '                        <div class="staticrypt-password-container">'
)

# 5. footer — insert after the closing </div> of staticrypt-page
# Find the pattern and insert footer
page_close = '            </div>\n\n        <script'
footer = '\n        <div class="en-footer">EntreNos x 12:12 Projects - confidencial</div>'
html = html.replace(page_close, '            </div>' + footer + '\n\n        <script', 1)

src.write_text(html, encoding="utf-8")
print(f"Done - {len(html):,} bytes")
