
import json
from pathlib import Path
from urllib.parse import urlparse

import requests
import streamlit as st

DATA_FILE = Path("services.json")


def load_services():
    if not DATA_FILE.exists():
        return []

    try:
        data = json.loads(DATA_FILE.read_text(encoding="utf-8"))
        return data if isinstance(data, list) else []
    except (json.JSONDecodeError, OSError):
        return []


def save_services(services):
    DATA_FILE.write_text(
        json.dumps(services, ensure_ascii=False, indent=4),
        encoding="utf-8"
    )


def validate_url(raw_url):
    url = raw_url.strip()

    if not url:
        return None

    if "://" not in url:
        url = "https://" + url

    try:
        parsed = urlparse(url)
        if parsed.scheme not in ("http", "https"):
            return None
        if not parsed.netloc or not parsed.hostname:
            return None
    except ValueError:
        return None

    return url


st.set_page_config(
    page_title="MiniOps - Servis İzleme",
    page_icon="🛠️",
    layout="centered"
)

st.title("MiniOps – Servis İzleme Sistemi")
st.write("Web servislerinizi ekleyin ve erişilebilirliklerini kontrol edin.")

if "services" not in st.session_state:
    st.session_state.services = load_services()

if "results" not in st.session_state:
    st.session_state.results = {}


st.subheader("Yeni Servis Ekle")

with st.form("service_form", clear_on_submit=True):
    name = st.text_input("Servis Adı")
    raw_url = st.text_input(
        "Servis URL Adresi",
        placeholder="https://example.com"
    )

    submitted = st.form_submit_button(
        "Servis Ekle",
        type="primary"
    )

if submitted:
    url = validate_url(raw_url)

    if not name.strip():
        st.error("Lütfen servis adı girin.")

    elif url is None:
        st.error("Geçerli bir HTTP veya HTTPS adresi girin.")

    elif any(s["url"] == url for s in st.session_state.services):
        st.warning("Bu servis zaten kayıtlı.")

    else:
        service = {
            "name": name.strip(),
            "url": url
        }

        st.session_state.services.append(service)
        save_services(st.session_state.services)
        st.success("Servis başarıyla eklendi!")


st.divider()
st.subheader("Kayıtlı Servisler")

if not st.session_state.services:
    st.info("Henüz kayıtlı servis bulunmuyor.")

for index, service in enumerate(st.session_state.services):

    with st.container(border=True):
        col1, col2 = st.columns([3, 1])

        with col1:
            st.markdown(f"**{service['name']}**")
            st.caption(service["url"])

        with col2:
            check = st.button(
                "Kontrol Et",
                key=f"check_{index}",
                use_container_width=True
            )

        if check:
            try:
                response = requests.get(
                    service["url"],
                    timeout=8
                )

                st.session_state.results[service["url"]] = {
                    "status": response.status_code,
                    "time": round(
                        response.elapsed.total_seconds() * 1000, 2
                    ),
                    "error": None
                }

            except requests.RequestException as error:
                st.session_state.results[service["url"]] = {
                    "error": str(error)
                }

            st.rerun()

        result = st.session_state.results.get(service["url"])

        if result:
            if result.get("error"):
                st.error("Servise erişilemedi: " + result["error"])
            elif result["status"] < 400:
                st.success(
                    f"HTTP {result['status']} | "
                    f"Yanıt süresi: {result['time']} ms"
                )
            else:
                st.warning(
                    f"HTTP {result['status']} | "
                    f"Yanıt süresi: {result['time']} ms"
                )
