import streamlit as st
import pandas as pd
import random
import time
import pydeck as pdk

# 1. Production UI Theme & Layout Configuration
st.set_page_config(
    page_title="NCPOR Polar Command Center", 
    page_icon="❄️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom High-Tech Styling Enhancements
st.markdown("""
    <style>
    .stApp { background-color: #0b0f19; color: #f8fafc; }
    div[data-testid="stMetricValue"] { font-size: 28px !important; font-weight: bold !important; color: #38bdf8 !important; }
    .stProgress > div > div > div > div { background-color: #ef4444 !important; }
    </style>
""", unsafe_allow_html=True)

# 2. Permanent Mock Database Setup (Simulated Storage State)
if 'comnap_cargo_db' not in st.session_state:
    st.session_state.comnap_cargo_db = pd.DataFrame([
        {"Manifest ID": "MFT-2026-001", "Item": "Aviation Fuel (Jet A-1)", "Category": "Fuel", "Quantity": 1500, "Unit": "Liters", "Min Threshold": 2000, "Status": "CRITICAL"},
        {"Item": "Arctic Survival Rations", "Manifest ID": "MFT-2026-002", "Category": "Food", "Quantity": 5000, "Unit": "Packs", "Min Threshold": 1000, "Status": "SAFE"},
        {"Item": "Thermal Extreme Outerwear", "Manifest ID": "MFT-2026-003", "Category": "Clothing", "Quantity": 120, "Unit": "Sets", "Min Threshold": 50, "Status": "SAFE"},
        {"Item": "Medical Oxygen Cylinders", "Manifest ID": "MFT-2026-004", "Category": "Medical", "Quantity": 15, "Unit": "Cylinders", "Min Threshold": 30, "Status": "CRITICAL"},
    ])

# Global Emergency Trigger Initialization
if 'emergency_broadcast_active' not in st.session_state:
    st.session_state.emergency_broadcast_active = False

# --- APP HEADER ---
st.title("❄️ Integrated Polar Expedition Logistics & Asset Management")
st.caption("🌐 Ministry of Earth Sciences (MoES) | National Centre for Polar and Ocean Research (NCPOR) | Live System")
st.write("---")

# Global Active Emergency Header Alert banner
if st.session_state.emergency_broadcast_active:
    st.error("🚨 GLOBAL RED ALERT PROTOCOL IS ACTIVE. SATCOM COMMUNICATIONS APPLIED OVER ALL SATELLITE CHANNELS.")

# 3. Sidebar Navigation Control Board
menu = st.sidebar.radio(
    "🛰️ CONTROL ENGINE MODULES:",
    ["📊 Operations Overview", "🚢 COMNAP Cargo Registry", "🫁 Live Personnel Biometrics", "🌤️ Climate Telemetry Grid", "🚨 Emergency Control System"]
)

st.sidebar.write("---")
st.sidebar.status("📡 Telemetry Syncing: ACTIVE", state="running")

# --- MODULE 1: OPERATIONS OVERVIEW (NEON DARK GRID PATTERN) ---
if menu == "📊 Operations Overview":
    st.subheader("📍 Real-Time Spatial Positioning & Terrain Telemetry")
    
    m1, m2, m3 = st.columns(3)
    m1.metric(label="Active Polar Nodes", value="3 Stations", delta="Online")
    crit_qty = len(st.session_state.comnap_cargo_db[st.session_state.comnap_cargo_db['Status']=='CRITICAL'])
    m2.metric(label="Critical Supply Breaches", value=f"{crit_qty} Flagged", delta="Action Required", delta_color="inverse")
    m3.metric(label="System Satellite Feed", value="Secure Encryption", delta="Connected")
    
    st.write("#### 📡 3D Coordinate Cartography Grid (Neon Outpost Vector Layout)")
    
    # Precise Antarctic Coordinates for India's Stations
    map_data = pd.DataFrame([
        {"name": "Bharati Station (India)", "latitude": -69.4083, "longitude": 76.1944},
        {"name": "Maitri Station (India)", "latitude": -70.7667, "longitude": 11.7333},
        {"name": "Field Camp Alpha", "latitude": -72.0000, "longitude": 45.0000}
    ])
    
    # Custom camera point angled down at the Antarctic coast layout grid
    view_state = pdk.ViewState(
        latitude=-68.0,
        longitude=45.0,
        zoom=2.2,
        pitch=35
    )
    
    # Pulsing neon cyan markers representing polar stations
    layer = pdk.Layer(
        "ScatterplotLayer",
        map_data,
        get_position=["longitude", "latitude"],
        get_color=[56, 189, 248, 200],  # Neon Blue/Cyan nodes
        get_radius=120000,
        pickable=True
    )
    
    # Native Pydeck Canvas Engine using the clean vector map theme setup
    st.pydeck_chart(pdk.Deck(
        map_style="light",  # Standard baseline theme contrast 
        initial_view_state=view_state,
        layers=[layer],
        tooltip={"text": "{name}"}
    ))

# --- MODULE 2: COMNAP CARGO REGISTRY ---
elif menu == "🚢 COMNAP Cargo Registry":
    st.subheader("🚢 Central Vessel & Station Cargo Inventory Ledger")
    
    critical_items = st.session_state.comnap_cargo_db[st.session_state.comnap_cargo_db['Status'] == 'CRITICAL']
    if not critical_items.empty:
        for idx, row in critical_items.iterrows():
            st.error(f"🤖 **AUTOMATED SMART TRACER:** Storage Alert on `{row['Item']}`. Below safety buffer target. Automated indent queued.")

    st.write("#### 🔍 Filter System Ledger")
    search_box = st.text_input("Enter item keyword or ID reference:", "")
    
    display_db = st.session_state.comnap_cargo_db
    if search_box:
        display_db = display_db[display_db['Item'].str.contains(search_box, case=False)]
        
    st.dataframe(display_db, use_container_width=True, hide_index=True)
    
    with st.expander("➕ Inject New Cargo Manifest Entry"):
        with st.form("cargo_entry_form", clear_on_submit=True):
            col1, col2 = st.columns(2)
            with col1:
                i_name = st.text_input("Cargo Item Name")
                m_id = st.text_input("Manifest ID Reference", value=f"MFT-2026-{random.randint(100,999)}")
                cat = st.selectbox("Category Group", ["Fuel", "Food", "Clothing", "Medical", "Equipment"])
            with col2:
                current_qty = st.number_input("Stored Stock Quantity", min_value=0, value=100)
                u_type = st.text_input("Unit Measurement Label", value="Units")
                safety_t = st.number_input("Minimum Safety Level Buffer", min_value=0, value=50)
            
            if st.form_submit_button("Commit Entry to Main Ledger"):
                if i_name:
                    stat = "SAFE" if current_qty >= safety_t else "CRITICAL"
                    new_item = {"Manifest ID": m_id, "Item": i_name, "Category": cat, "Quantity": current_qty, "Unit": u_type, "Min Threshold": safety_t, "Status": stat}
                    st.session_state.comnap_cargo_db = pd.concat([st.session_state.comnap_cargo_db, pd.DataFrame([new_item])], ignore_index=True)
                    st.success("Entry saved successfully.")
                    st.rerun()

# --- MODULE 3: LIVE PERSONNEL BIOMETRICS ---
elif menu == "🫁 Live Personnel Biometrics":
    st.subheader("👤 High-Frequency Radio Telemetry Biometric Stream")
    st.caption("🔄 Telemetry Loop Active: Data elements updating dynamically every 1.0 seconds.")
    
    team = [
        {"Name": "Dr. Aarav Sharma", "Role": "Lead Meteorologist", "Loc": "Bharati Station", "HR": 72, "SYS": 120, "DIA": 80, "SpO2": 98, "Temp": 36.6, "O2": 82},
        {"Name": "Sarah Jenkins", "Role": "Logistics Chief", "Loc": "Maitri Station", "HR": 76, "SYS": 122, "DIA": 82, "SpO2": 99, "Temp": 36.8, "O2": 91},
        {"Name": "Cmdr. Rajesh Kumar", "Role": "Expedition Leader", "Loc": "Ice Outpost Alpha", "HR": 106, "SYS": 141, "DIA": 92, "SpO2": 91, "Temp": 34.4, "O2": 14}
    ]
    
    for p in team:
        live_hr = p["HR"] + random.randint(-3, 3)
        live_sys = p["SYS"] + random.randint(-4, 4)
        live_dia = p["DIA"] + random.randint(-2, 2)
        live_spo2 = min(100, p["SpO2"] + random.randint(-1, 1))
        live_temp = round(p["Temp"] + random.uniform(-0.2, 0.2), 1)
        
        with st.container(border=True):
            h_col, d_col = st.columns(2)
            with h_col:
                st.markdown(f"### 👤 {p['Name']}")
                st.write(f"*{p['Role']}*")
                st.markdown(f"📍 **Node:** {p['Loc']}")
            with d_col:
                c1, c2, c3, c4 = st.columns(4)
                c1.metric("❤️ Heart Rate", f"{live_hr} BPM")
                c2.metric("🩺 Blood Pressure", f"{live_sys}/{live_dia} mmHg")
                
                if live_spo2 < 93:
                    c3.metric("🚨 Oxygen (SpO2)", f"{live_spo2}%", "LOW HYPOXIA", delta_color="inverse")
                else:
                    c3.metric("🟢 Oxygen (SpO2)", f"{live_spo2}%")
                    
                if live_temp < 35.0:
                    c4.metric("🥶 Core Body Temp", f"{live_temp}°C", "HYPOTHERMIA", delta_color="inverse")
                else:
                    c4.metric("🌡️ Core Body Temp", f"{live_temp}°C")
                
                st.write(f"**Life-Support Oxygen Cylinder Reserves Level:** {p['O2']}%")
                if p["O2"] < 20:
                    st.progress(p["O2"] / 100)
                    st.markdown("<span style='color:#ef4444; font-weight:bold;'>🚨 CRITICAL DEPLETION</span>", unsafe_allow_html=True)
                else:
                    st.progress(p["O2"] / 100)

# --- MODULE 4: CLIMATE TELEMETRY ---
elif menu == "🌤️ Climate Telemetry Grid":
    st.subheader("🌤️ Automated Weather Telemetry Matrix")
    col1, col2, col3 = st.columns(3)
    col1.metric("Bharati Station Node", "-22°C", "Wind: 14 knots")
    col2.metric("Maitri Station Node", "-29°C", "Wind: 39 knots")
    col3.metric("Field Camp Outpost Alpha", "-44°C", "Wind: 64 knots 🚨", delta_color="inverse")
    st.error("🤖 **AUTOMATED MITIGATION RULE EXECUTION:** Operations locked down at Outpost Alpha due to blizzard conditions.")

# --- MODULE 5: EMERGENCY CONTROL SYSTEM ---
elif menu == "🚨 Emergency Control System":
    st.subheader("⚠️ Emergency Response System (ERS) Management Portal")
    st.warning("CRITICAL ACTIONS AHEAD: Triggering these buttons overrides standard tracking loops.")
    
    col_trigger, col_reset = st.columns(2)
    
    with col_trigger:
        if st.button("🚨 BROADCAST EMERGENCY RED ALERT STATE", type="primary", use_container_width=True):
            st.session_state.emergency_broadcast_active = True
            st.rerun()
            
    with col_reset:
        if st.button("✅ DE-ESCALATE SYSTEM TO STANDARD MONITORING", use_container_width=True):
            st.session_state.emergency_broadcast_active = False
            st.success("System returned to secure baseline operations status.")
            st.rerun()

    if st.session_state.emergency_broadcast_active:
        st.error("🚨 CURRENT SYSTEM STATE: RED CRITICAL OVERRIDE. Signal outposts pinged continuously.")
    else:
        st.success("✅ CURRENT SYSTEM STATE: Baseline standard operations.")

# --- 5. AUTOMATED DYNAMIC TIMING REFRESH CONTROLLER LOOP ---
if menu == "🫁 Live Personnel Biometrics":
    time.sleep(1.0)
    st.rerun()
