import streamlit as st

st.set_page_config(
    page_title="고양이 도감",
    page_icon="🐱"
)

st.title("🐾 Streamlit 고양이 도감")
st.text("고양이를 하나씩 추가해서 도감을 채워보세요!")

trait_emoji_dict = {
    "털 없음": "🧼",
    "장모": "🧣",
    "단모": "✂️",
    "털 빠짐 적음": "🍃",
    "활동적": "🏃‍♂️",
    "조용함": "😴",
    "사회적": "👥",
    "독립적": "🙅‍♀️",
    "개성 강함": "🌟",
    "사교적": "🎉",
}

initial_cats = [

    {
        "name": "스핑크스",
        "traits": ["털 없음", "사회적"],
        "image_url": "https://i.namu.wiki/i/VVWK3D5bTOLLNdRrsgeQ23e6LkETDU7K9jGsXRqvKXgBhj-rPhXBAfIJd-DJRrAS1gTwLCaXbG7xG4dUK-qn31roDFCOwGjDq-ibDZiF3Wl5Rk2hftIvwyt1RLO_0t6TL1zOTDC_GQYHSNslG6oo-w.webp"
    },
    {
        "name": "페르시안",
        "traits": ["장모", "조용함"],
        "image_url": "https://cdn.pixabay.com/photo/2017/11/09/21/41/cat-2934720_1280.jpg"
    },
    {
        "name": "러시안블루",
        "traits": ["단모", "조용함"],
        "image_url": "https://i.namu.wiki/i/AkU_L00q6HSW914Z-l8gMVgTnNScv1uzURQwhjSFvtOweYyY4UoNeBsLxqg7kd5SEdlZigaQjBhQaejKZkCnYtaNbSGlG3zGqk5ptftzeth_xl4p6USkcvew9FinJAYO3QKaWgGAsKn4iQolB-ZgLw.webp"
    },
    {
        "name": "벵갈",
        "traits": ["단모", "활동적"],
        "image_url": "https://i.namu.wiki/i/7GNVxLpW36eXdYPJ5nud2VsB35lAyO9n4mAFDaGEQq2UPW0XZe7GjU9QrUdrSv2JIVaWFR0sJSj7yAc1FJkIEFa9-PB_QQeTC9v7wWurLA1h_AaZeElRGBige6UfFaQysF9etr24G6d9PejqenqpTA.webp"
    },
    {
        "name": "메인쿤",
        "traits": ["장모", "사회적"],
        "image_url": "https://i.namu.wiki/i/BkpuZKQBdh1aIWtvQBfu2xxaNNeSaktyRFp1xIQzFKAen_5NlG4fWO8C4nkb83gDblwtH8Z14jusLsKjKcSDCgoOafrpDnP9i4qSo-SWMn1aU6cvDJm4HVp6TMxcWztn5dVX4Ic-OcIOT4g_bFJD7g.webp"
    },
    {
        "name": "스코티시 폴드",
        "traits": ["털 빠짐 적음", "조용함"],
        "image_url": "https://i.namu.wiki/i/BMh4IGH2ZSqURH3-A27SdIrACJgF6tomXcFHNhtoaEkYqOjM8wSRF1d8lLUuHZVijYmJyVa2CpMh7qJZAvijCvs0NxKpJXQzBAhw1C2HILxURfizjWNX9Svt9gJDkqnp3eoCqIR_AjRSb-igys__-Q.webp"
    },
]

example_cat = {
    "name": "노르웨이 숲 고양이",
    "traits": ["장모", "독립적"],
    "image_url": "https://i.namu.wiki/i/T-aQh8JaIfJpcUPdSICxucHGa_bEEqPDTqiwa9vT6V2gnSsof1_8YZHZIrG29AxSHScbG4FavhEC9jdZpeXiSo41Pdd8f_4mBAtOiWVCdxR46MId4BEp6DxtrazsCbXrTtDQGYHignvooSqJ6w9IXg.webp"
}

if "cats" not in st.session_state:
    st.session_state.cats = initial_cats

auto_complete = st.toggle("예시 데이터로 채우기")

with st.form(key="form"):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input(
            label="고양이 이름",
            value=example_cat["name"] if auto_complete else ""
        )
    with col2:
        traits = st.multiselect(
            label="고양이 특성",
            options=list(trait_emoji_dict.keys()),
            max_selections=3,
            default=example_cat["traits"] if auto_complete else []
        )
    image_url = st.text_input(
        label="고양이 이미지 URL",
        value=example_cat["image_url"] if auto_complete else ""
    )
    submit = st.form_submit_button(label="추가")
    if submit:
        if not name:
            st.error("고양이 이름을 입력해주세요.")
        elif len(traits) == 0:
            st.error("고양이 특성을 적어도 한 개 선택해주세요.")
        else:
            st.success("고양이를 도감에 추가했습니다!")
            st.session_state.cats.append({
                "name": name,
                "traits": traits,
                "image_url": image_url if image_url else "./images/default_cat.png"
            })

for i in range(0, len(st.session_state.cats), 3):
    row_cats = st.session_state.cats[i:i+3]
    cols = st.columns(3)
    for j in range(len(row_cats)):
        with cols[j]:
            cat = row_cats[j]
            with st.expander(label=f"**{i+j+1}. {cat['name']}**", expanded=True):
                st.image(cat["image_url"])
                emoji_traits = [f"{trait_emoji_dict[t]} {t}" for t in cat["traits"]]
                st.text(" / ".join(emoji_traits))
                delete_button = st.button(label="삭제", key=i+j, use_container_width=True)
                if delete_button:
                    del st.session_state.cats[i+j]
                    st.rerun()
