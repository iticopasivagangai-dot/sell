
import streamlit as st
import os

# =====================================================
# PAGE SETTINGS
# =====================================================

st.set_page_config(
    page_title="AutoMart - Buy & Sell Cars",
    page_icon="🚗",
    layout="wide"
)

# =====================================================
# CSS
# =====================================================

st.markdown("""
<style>

.main {
    background-color: #f5f7fa;
}

.car-card {
    background-color: white;
    padding: 15px;
    border-radius: 15px;
    box-shadow: 0 2px 10px #dddddd;
    margin-bottom: 20px;
}

.price {
    color: #0a8f3d;
    font-size: 24px;
    font-weight: bold;
}

.car-title {
    font-size: 24px;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# CAR DATABASE
# =====================================================

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
        "image": "C:\Users\HP\Pictures\creta.jpg"
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
        "image": "images/swift.jpg"
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
        "image": "images/innova.jpg"
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
        "image": "images/nexon.jpg"
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
        "image": "images/city.jpg"
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
        "image": "images/thar.jpg"
    }
]

# =====================================================
# SESSION STATE
# =====================================================

if "favorites" not in st.session_state:
    st.session_state.favorites = []

# =====================================================
# HEADER
# =====================================================

st.title("🚗 AutoMart")

st.subheader("Buy & Sell Cars Easily")

st.write(
    "Find your dream car or sell your car quickly and safely."
)

st.divider()

# =====================================================
# NAVIGATION
# =====================================================

page = st.radio(
    "Navigation",
    [
        "🏠 Home",
        "🚗 Buy Cars",
        "💰 Sell Your Car",
        "❤️ Favorites"
    ],
    horizontal=True
)

# =====================================================
# HOME
# =====================================================

if page == "🏠 Home":

    st.header("Find Your Perfect Car")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "🚗 Cars Available",
            len(cars)
        )

    with col2:
        st.metric(
            "📍 Cities",
            len(set(car["city"] for car in cars))
        )

    with col3:
        st.metric(
            "👤 Sellers",
            len(cars)
        )

    st.divider()

    st.header("🔥 Featured Cars")

    cols = st.columns(3)

    for i, car in enumerate(cars[:3]):

        with cols[i]:

            # Display image
            if os.path.exists(car["image"]):
                st.image(
                    car["image"],
                    use_container_width=True
                )
            else:
                st.info(
                    "Car image not found.\n\n"
                    + car["image"]
                )

            st.subheader(car["name"])

            st.write(
                f"📅 {car['year']} | "
                f"🛣️ {car['km']:,} km"
            )

            st.write(
                f"⛽ {car['fuel']} | "
                f"⚙️ {car['transmission']}"
            )

            st.markdown(
                f"### ₹{car['price']:,}"
            )

            st.write(
                f"📍 {car['city']}"
            )

# =====================================================
# BUY CARS
# =====================================================

elif page == "🚗 Buy Cars":

    st.header("🚗 Buy a Car")

    # Search
    search = st.text_input(
        "🔎 Search Car",
        placeholder="Example: Hyundai, Honda, Tata..."
    )

    # Filters
    col1, col2, col3, col4 = st.columns(4)

    with col1:

        fuel = st.selectbox(
            "Fuel Type",
            [
                "All",
                "Petrol",
                "Diesel",
                "Electric",
                "CNG"
            ]
        )

    with col2:

        transmission = st.selectbox(
            "Transmission",
            [
                "All",
                "Manual",
                "Automatic"
            ]
        )

    with col3:

        city = st.selectbox(
            "City",
            ["All"] +
            sorted(
                set(car["city"] for car in cars)
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

    # =================================================
    # FILTER CARS
    # =================================================

    filtered_cars = []

    for car in cars:

        if search:

            if search.lower() not in car["name"].lower():
                continue

        if fuel != "All":

            if car["fuel"] != fuel:
                continue

        if transmission != "All":

            if car["transmission"] != transmission:
                continue

        if city != "All":

            if car["city"] != city:
                continue

        if car["price"] > max_price:
            continue

        filtered_cars.append(car)

    st.write(
        f"### {len(filtered_cars)} Cars Found"
    )

    # =================================================
    # DISPLAY CARS
    # =================================================

    for car in filtered_cars:

        col1, col2 = st.columns([1, 2])

        # Car Image
        with col1:

            if os.path.exists(car["image"]):

                st.image(
                    car["image"],
                    use_container_width=True
                )

            else:

                st.warning(
                    f"Image missing: {car['image']}"
                )

        # Car Details
        with col2:

            st.markdown(
                f"## {car['name']}"
            )

            st.write(
                f"📅 **Year:** {car['year']}"
            )

            st.write(
                f"🛣️ **Kilometers:** "
                f"{car['km']:,} km"
            )

            st.write(
                f"⛽ **Fuel:** {car['fuel']}"
            )

            st.write(
                f"⚙️ **Transmission:** "
                f"{car['transmission']}"
            )

            st.write(
                f"👤 **Owner:** {car['owner']}"
            )

            st.write(
                f"📍 **Location:** {car['city']}"
            )

            st.markdown(
                f"### 💰 ₹{car['price']:,}"
            )

            col_a, col_b = st.columns(2)

            # Favorite
            with col_a:

                if st.button(
                    "❤️ Favorite",
                    key="favorite_" + car["name"]
                ):

                    if car["name"] not in st.session_state.favorites:

                        st.session_state.favorites.append(
                            car["name"]
                        )

                        st.success(
                            "Added to Favorites!"
                        )

                    else:

                        st.info(
                            "Already in Favorites."
                        )

            # Contact Seller
            with col_b:

                if st.button(
                    "📞 Contact Seller",
                    key="contact_" + car["name"]
                ):

                    st.success(
                        "Seller Contact: "
                        "+91 98765 43210"
                    )

        st.divider()

# =====================================================
# SELL YOUR CAR
# =====================================================

elif page == "💰 Sell Your Car":

    st.header("💰 Sell Your Car")

    st.write(
        "Create your car listing and reach potential buyers."
    )

    with st.form("sell_car_form"):

        col1, col2 = st.columns(2)

        with col1:

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

        with col2:

            fuel = st.selectbox(
                "Fuel Type",
                [
                    "Petrol",
                    "Diesel",
                    "Electric",
                    "CNG"
                ]
            )

            transmission = st.selectbox(
                "Transmission",
                [
                    "Manual",
                    "Automatic"
                ]
            )

            city = st.text_input(
                "City",
                placeholder="Example: Chennai"
            )

            owner = st.selectbox(
                "Owner",
                [
                    "First Owner",
                    "Second Owner",
                    "Third Owner"
                ]
            )

        phone = st.text_input(
            "Contact Number"
        )

        image = st.file_uploader(
            "Upload Car Image",
            type=[
                "jpg",
                "jpeg",
                "png"
            ]
        )

        description = st.text_area(
            "Car Description",
            placeholder="Describe your car..."
        )

        submitted = st.form_submit_button(
            "🚗 Publish Car Listing"
        )

        if submitted:

            if not name or not city or not phone:

                st.error(
                    "Please fill in all required fields."
                )

            else:

                st.success(
                    f"🎉 {name} listing created successfully!"
                )

                st.write(
                    f"**Price:** ₹{price:,}"
                )

                st.write(
                    f"**Location:** {city}"
                )

                if image:

                    st.image(
                        image,
                        caption=name,
                        width=400
                    )

# =====================================================
# FAVORITES
# =====================================================

elif page == "❤️ Favorites":

    st.header("❤️ My Favorite Cars")

    if not st.session_state.favorites:

        st.info(
            "You have not added any cars to favorites."
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

                col1, col2 = st.columns([1, 2])

                with col1:

                    if os.path.exists(car["image"]):

                        st.image(
                            car["image"],
                            use_container_width=True
                        )

                with col2:

                    st.subheader(
                        car["name"]
                    )

                    st.write(
                        f"📅 {car['year']}"
                    )

                    st.write(
                        f"🛣️ {car['km']:,} km"
                    )

                    st.write(
                        f"⛽ {car['fuel']}"
                    )

                    st.markdown(
                        f"### ₹{car['price']:,}"
                    )

                st.divider()

# =====================================================
# FOOTER
# =====================================================

st.divider()

st.markdown(
    """
    <div style="text-align:center">

    <h2>🚗 AutoMart</h2>

    <p>
    Your trusted platform to buy and sell cars.
    </p>

    <p>
    📞 +91 98765 43210
    &nbsp;&nbsp; | &nbsp;&nbsp;
    📧 support@automart.com
    </p>

    <p>
    © 2026 AutoMart. All Rights Reserved.
    </p>

    </div>
    """,
    unsafe_allow_html=True
)


