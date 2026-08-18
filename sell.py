
import streamlit as st

# ---------------- PAGE SETTINGS ----------------
st.set_page_config(
    page_title="AutoMart - Buy & Sell Cars",
    page_icon="🚗",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
.main {
    background-color: #f5f7fa;
}

.car-card {
    background: white;
    padding: 18px;
    border-radius: 15px;
    margin-bottom: 20px;
    box-shadow: 0 2px 10px #ddd;
}

.price {
    color: #0b7a35;
    font-size: 22px;
    font-weight: bold;
}

.title {
    color: #1f2937;
}

.small {
    color: #666;
}

</style>
""", unsafe_allow_html=True)


# ---------------- CAR DATABASE ----------------
cars = [
    {
        "name": "Hyundai Creta",
        "year": 2022,
        "price": 1250000,
        "km": 25000,
        "fuel": "Petrol",
        "transmission": "Automatic",
        "city": "Chennai",
        "owner": "First Owner",
        "icon": "🚙"
    },
    {
        "name": "Maruti Swift",
        "year": 2021,
        "price": 650000,
        "km": 30000,
        "fuel": "Petrol",
        "transmission": "Manual",
        "city": "Coimbatore",
        "owner": "First Owner",
        "icon": "🚗"
    },
    {
        "name": "Toyota Innova",
        "year": 2020,
        "price": 1450000,
        "km": 45000,
        "fuel": "Diesel",
        "transmission": "Manual",
        "city": "Madurai",
        "owner": "Second Owner",
        "icon": "🚐"
    },
    {
        "name": "Tata Nexon",
        "year": 2023,
        "price": 950000,
        "km": 15000,
        "fuel": "Petrol",
        "transmission": "Manual",
        "city": "Chennai",
        "owner": "First Owner",
        "icon": "🚙"
    },
    {
        "name": "Honda City",
        "year": 2022,
        "price": 1100000,
        "km": 20000,
        "fuel": "Petrol",
        "transmission": "Automatic",
        "city": "Bangalore",
        "owner": "First Owner",
        "icon": "🚘"
    },
    {
        "name": "Mahindra Thar",
        "year": 2023,
        "price": 1550000,
        "km": 10000,
        "fuel": "Diesel",
        "transmission": "Manual",
        "city": "Chennai",
        "owner": "First Owner",
        "icon": "🚙"
    }
]


# ---------------- SESSION STATE ----------------
if "favorites" not in st.session_state:
    st.session_state.favorites = []

if "selected_car" not in st.session_state:
    st.session_state.selected_car = None


# ---------------- HEADER ----------------
st.title("🚗 AutoMart")

st.subheader("Buy & Sell Cars Easily")

st.write(
    "Find your dream car or sell your car quickly and safely."
)

st.divider()


# ---------------- NAVIGATION ----------------
page = st.radio(
    "Navigation",
    ["🏠 Home", "🚗 Buy Cars", "💰 Sell Your Car", "❤️ Favorites"],
    horizontal=True
)


# ==================================================
# HOME
# ==================================================

if page == "🏠 Home":

    st.header("Find Your Perfect Car")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("🚗 Cars Available", len(cars))

    with col2:
        st.metric("📍 Cities", len(set(c["city"] for c in cars)))

    with col3:
        st.metric("👤 Sellers", len(cars))

    st.divider()

    st.subheader("🔥 Featured Cars")

    cols = st.columns(3)

    for i, car in enumerate(cars[:3]):

        with cols[i]:

            st.markdown(
                f"""
                <div class="car-card">

                <div style="font-size:70px;text-align:center;">
                {car["icon"]}
                </div>

                <h2>{car["name"]}</h2>

                <p>{car["year"]} • {car["km"]:,} km</p>

                <p>{car["fuel"]} • {car["transmission"]}</p>

                <p class="price">
                ₹{car["price"]:,}
                </p>

                <p>📍 {car["city"]}</p>

                </div>
                """,
                unsafe_allow_html=True
            )


# ==================================================
# BUY CARS
# ==================================================

elif page == "🚗 Buy Cars":

    st.header("🚗 Buy a Car")

    # Search
    search = st.text_input(
        "🔎 Search",
        placeholder="Search car name..."
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        fuel = st.selectbox(
            "Fuel",
            ["All", "Petrol", "Diesel"]
        )

    with col2:

        transmission = st.selectbox(
            "Transmission",
            ["All", "Manual", "Automatic"]
        )

    with col3:

        city = st.selectbox(
            "City",
            ["All"] + sorted(
                list(set(c["city"] for c in cars))
            )
        )

    with col4:

        max_price = st.slider(
            "Maximum Price",
            300000,
            2000000,
            2000000,
            step=50000
        )

    st.divider()

    # Filter cars
    filtered = []

    for car in cars:

        if search:
            if search.lower() not in car["name"].lower():
                continue

        if fuel != "All" and car["fuel"] != fuel:
            continue

        if transmission != "All":
            if car["transmission"] != transmission:
                continue

        if city != "All" and car["city"] != city:
            continue

        if car["price"] > max_price:
            continue

        filtered.append(car)

    st.write(f"**{len(filtered)} cars found**")

    # Display cars
    for car in filtered:

        col1, col2 = st.columns([1, 2])

        with col1:

            st.markdown(
                f"""
                <div style="
                background:white;
                padding:30px;
                border-radius:15px;
                text-align:center;
                font-size:100px;
                ">
                {car["icon"]}
                </div>
                """,
                unsafe_allow_html=True
            )

        with col2:

            st.subheader(car["name"])

            st.write(
                f"📅 {car['year']}   |   "
                f"🛣️ {car['km']:,} km"
            )

            st.write(
                f"⛽ {car['fuel']}   |   "
                f"⚙️ {car['transmission']}"
            )

            st.write(
                f"📍 {car['city']}   |   "
                f"👤 {car['owner']}"
            )

            st.markdown(
                f"### ₹{car['price']:,}"
            )

            col_a, col_b = st.columns(2)

            with col_a:

                if st.button(
                    "❤️ Favorite",
                    key="fav_" + car["name"]
                ):

                    if car["name"] not in st.session_state.favorites:

                        st.session_state.favorites.append(
                            car["name"]
                        )

                        st.success("Added to favorites!")

            with col_b:

                if st.button(
                    "📞 Contact Seller",
                    key="contact_" + car["name"]
                ):

                    st.info(
                        "Seller Phone: +91 98765 43210"
                    )

        st.divider()


# ==================================================
# SELL YOUR CAR
# ==================================================

elif page == "💰 Sell Your Car":

    st.header("💰 Sell Your Car")

    st.write(
        "Enter your car details to create a listing."
    )

    with st.form("sell_car"):

        name = st.text_input(
            "Car Name",
            placeholder="Example: Hyundai i20"
        )

        year = st.number_input(
            "Manufacturing Year",
            min_value=1990,
            max_value=2026,
            value=2022
        )

        price = st.number_input(
            "Expected Price ₹",
            min_value=50000,
            value=500000
        )

        km = st.number_input(
            "Kilometers Driven",
            min_value=0,
            value=25000
        )

        fuel = st.selectbox(
            "Fuel Type",
            ["Petrol", "Diesel", "Electric", "CNG"]
        )

        transmission = st.selectbox(
            "Transmission",
            ["Manual", "Automatic"]
        )

        city = st.text_input(
            "City",
            placeholder="Example: Chennai"
        )

        owner = st.selectbox(
            "Owner",
            ["First Owner", "Second Owner", "Third Owner"]
        )

        phone = st.text_input(
            "Contact Number"
        )

        submitted = st.form_submit_button(
            "🚗 Publish Car Listing"
        )

        if submitted:

            if name and city and phone:

                st.success(
                    f"🎉 Your {name} listing has been submitted!"
                )

                st.info(
                    "Our team will contact you shortly."
                )

            else:

                st.error(
                    "Please fill in all required fields."
                )


# ==================================================
# FAVORITES
# ==================================================

elif page == "❤️ Favorites":

    st.header("❤️ My Favorite Cars")

    if not st.session_state.favorites:

        st.info(
            "You haven't added any cars to favorites yet."
        )

    else:

        for favorite in st.session_state.favorites:

            car = next(
                (
                    c for c in cars
                    if c["name"] == favorite
                ),
                None
            )

            if car:

                st.subheader(
                    f"{car['icon']} {car['name']}"
                )

                st.write(
                    f"₹{car['price']:,} | "
                    f"{car['year']} | "
                    f"{car['km']:,} km | "
                    f"{car['city']}"
                )

                st.divider()


# ---------------- FOOTER ----------------

st.divider()

st.markdown(
    """
    <div style="text-align:center">

    <h3>🚗 AutoMart</h3>

    <p>
    Buy and sell cars with confidence.
    </p>

    <p>
    📞 +91 98765 43210 |
    📧 support@automart.com
    </p>

    <p>
    © 2026 AutoMart
    </p>

    </div>
    """,
    unsafe_allow_html=True
)

