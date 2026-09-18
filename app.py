import streamlit as st
import pandas as pd
import random
import time

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
    .metric-card {
        background-color: #1e293b;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #334155;
    }
    .status-badge {
        padding: 4px 8px;
        border-radius: 4px;
        font-weight: bold;
        font-size: 12px;
    }
    </style>
""", unsafe_allow_html=True)

# 2. Permanent Mock Database Setup (Simulated Storage State)
if 'comnap_cargo_db' not in st.session_state:
    st.session_state.comnap_cargo_db = pd.DataFrame([
        {"Manifest ID": "MFT-2026-001", "Item": "Aviation Fuel (Jet A-1)", "Category": "Fuel", "Quantity": 1500, "Unit": "Liters", "Min Threshold": 2000, "Hazard Class": "Class 3 (Flammable)", "Status": "CRITICAL"},
        {"Item": "Arctic Survival Rations", "Manifest ID": "MFT-2026-002", "Category": "Food", "Quantity": 5000, "Unit": "Packs", "Min Threshold": 1000, "Hazard Class": "Non-Hazardous", "Status": "SAFE"},
        {"Item": "Thermal Extreme Outerwear", "Manifest ID": "MFT-2026-003", "Category": "Clothing", "Quantity": 120, "Unit": "Sets", "Min Threshold": 50, "Hazard Class": "Non-Hazardous", "Status": "SAFE"},
        {"Item": "Medical Trauma Oxygen Units", "Manifest ID": "MFT-2026-004", "Category": "Medical", "Quantity": 15, "Unit": "Cylinders", "Min Threshold": 30, "Hazard Class": "Class 2.2 (Gas)", "Status": "CRITICAL"},
    ])

# 3. Sidebar Navigation Control Board
with st.sidebar:
    st.image("https://icons8.com", width=70)
    st.title("🛰️ NCPOR COMMAND")
    st.caption("National Centre for Polar & Ocean Research")
    st.write("---")
    menu = st.radio(
        "Select Control Module:",
        ["📊 Operations Overview", "🚢 COMNAP Cargo Registry", "🫁 Live Personnel Biometrics", "🌤️ Weather Gateways", "🚨 Emergency Response (SOS)"]
    )
    st.write("---")
    live_flux = st.toggle("Enable Live Telemetry Stream", value=True)
    if live_flux and menu == "🫁 Live Personnel Biometrics":
        st.caption("🔄 High-frequency streaming active (2s update)...")

# --- APP HEADER ---
st.title("❄️ Integrated Polar Expedition Logistics & Asset Management System")
st.caption("🌐 Ministry of Earth Sciences (MoES) | Government of India | Smart Automation Grid")
st.write("---")

# --- MODULE 1: OPERATIONS OVERVIEW ---
if menu == "📊 Operations Overview":
    st.subheader("📍 Real-Time Spatial Positioning & Telemetry Grid")
    
    # Visual Metrics Blocks
    m1, m2, m3 = st.columns(3)
    with m1:
        st.info("📶 **Active Polar Nodes**  \n## 03 Stations Online")
    with m2:
        critical_count = len(st.session_state.comnap_cargo_db[st.session_state.comnap_cargo_db['Status']=='CRITICAL'])
        st.error(f"⚠️ **Critical Supply Breaches**  \n## {critical_count} Items Flagged")
    with m3:
        st.success("💚 **Mission Vitals Status**  \n## Telemetry Connected")
    
    st.write("#### Live Deployment Map (Antarctica Research Grid)")
    map_data = pd.DataFrame({
        'latitude': [-69.4083, -70.7667, -74.0000],
        'longitude': [76.1944, 11.7333, 35.0000]
    })
    st.map(map_data, size=25000)

# --- MODULE 2: COMNAP CARGO REGISTRY ---
elif menu == "🚢 COMNAP Cargo Registry":
    st.subheader("🚢 Central Vessel & Station Cargo Inventory Database")
    
    # Core Intelligent System Automation Warning
    critical_items = st.session_state.comnap_cargo_db[st.session_state.comnap_cargo_db['Status'] == 'CRITICAL']
    if not critical_items.empty:
        for idx, row in critical_items.iterrows():
            st.error(f"🤖 **AUTOMATED LOGISTICS ALENT:** Supply Line Deficiency detected for `{row['Item']}` (ID: {row['Manifest ID']}). Storage dropped below safe buffer threshold ({row['Min Threshold']} {row['Unit']}). Resupply route ticket generated automatically.")

    # Search and Filter Engine for a professional layout
    st.write("#### 🔍 Filter Ledger")
    search_query = st.text_input("Search items by name or Manifest ID:", "")
    
    filtered_db = st.session_state.comnap_cargo_db
    if search_query:
        filtered_db = filtered_db[
            filtered_db['Item'].str.contains(search_query, case=False) | 
            filtered_db['Manifest ID'].str.contains(search_query, case=False)
        ]
        
    st.write("#### Verified Inventory Records Database")
    st.dataframe(filtered_db, use_container_width=True, hide_index=True)
    
    # Data Entry Control (Correctly scoped so it ONLY appears inside this module!)
    st.write("---")
    with st.expander("➕ Inject New Cargo Manifest Entry into Database"):
        with st.form("comnap_db_form", clear_on_submit=True):
            col1, col2 = st.columns(2)
            with col1:
                item_name = st.text_input("Item Name / Description")
                manifest_id = st.text_input("Manifest ID Reference", value=f"MFT-2026-{random.randint(100,999)}")
                category = st.selectbox("Inventory Category", ["Fuel", "Food", "Clothing", "Medical", "Expedition Equipment"])
            with col2:
                qty = st.number_input("Current Stored Quantity", min_value=0, value=100)
                unit_type = st.text_input("Measurement Unit", value="Units")
                threshold = st.number_input("Minimum Safety Threshold Level", min_value=0, value=50)
                hazard_class = st.selectbox("Hazard Classification", ["Non-Hazardous", "Class 2.2 (Gas)", "Class 3 (Flammable)", "Class 9 (Miscellaneous Goods)"])
            
            submit = st.form_submit_button("Commit Entry to Database Ledger")
            if submit and item_name:
                status = "SAFE" if qty >= threshold else "CRITICAL"
                new_entry = {
                    "Manifest ID": manifest_id, "Item": item_name, "Category": category, 
                    "Quantity": qty, "Unit": unit_type, "Min Threshold": threshold, 
                    "Hazard Class": hazard_class, "Status": status
                }
                st.session_state.comnap_cargo_db = pd.concat([st.session_state.comnap_cargo_db, pd.DataFrame([new_entry])], ignore_index=True)
                st.success(f"Database Write Success: Entry logged for {item_name}.")
                st.rerun()

# --- MODULE 3: LIVE PERSONNEL BIOMETRICS ---
elif menu == "🫁 Live Personnel Biometrics":
    st.subheader("👤 Real-Time Environmental Medicine & Biometric Dashboard")
    
    personnel_list = [
        {"Name": "Dr. Aarav Sharma", "Role": "Lead Meteorologist", "Loc": "Bharati Station", "Base_HR": 74, "Base_BP": 120, "Base_SpO2": 98, "Base_Temp": 36.6, "O2_Cyl": 85},
        {"Name": "Sarah Jenkins", "Role": "Logistics Chief", "Loc": "Maitri Station", "Base_HR": 78, "Base_BP": 122, "Base_SpO2": 99, "Base_Temp": 36.7, "O2_Cyl": 90},
        {"Name": "Cmdr. Rajesh Kumar", "Role": "Expedition Leader", "Loc": "Ice Shelf Outpost", "Base_HR": 108, "Base_BP": 139, "Base_SpO2": 92, "Base_Temp": 34.6, "O2_Cyl": 18}
    ]
    
    for p in personnel_list:
        # Dynamic telemetry fluctuation calculations
        current_hr = p["Base_HR"] + random.randint(-3, 3)
        current_sbp = p["Base_BP"] + random.randint(-4, 4)
        current_dbp = 80 + random.randint(-3, 3)
        current_spo2 = min(100, p["Base_SpO2"] + random.randint(-1, 1))
        current_temp = round(p["Base_Temp"] + random.uniform(-0.2, 0.2), 1)
        
        # Structural visual block container
        with st.container(border=True):
            head_col, data_col = st.columns([1, 3])
            
            with head_col:
                st.markdown(f"### 👤 {p['Name']}")
                st.caption(f"**Role:** {p['Role']}")
                st.caption(f"📍 **Location:** {p['Loc']}")
            
            with data_col:
                c1, c2, c3, c4 = st.columns(4)
                
                c1.metric("❤️ Heart Rate", f"{current_hr} BPM")
                c2.metric("🩺 Blood Pressure", f"{current_sbp}/{current_dbp} mmHg")
                
                if current_spo2 < 94:
                    c3.metric("🚨 Oxygen (SpO2)", f"{current_spo2}%", "CRITICAL HYPOXIA", delta_color="inverse")
                else:
                    c3.metric("🟢 Oxygen (SpO2)", f"{current_spo2}%")
                    
                if current_temp < 35.0:
                    c4.metric("🥶 Core Body Temp", f"{current_temp}°C", "HYPOTHERMIA RISK", delta_color="inverse")
                else:
                    c4.metric("🌡️ Core Body Temp", f"{current_temp}°C")
                
                # Visual UI Progress bar to track remaining oxygen reserves cleanly
                st.write("**Remaining Suite Oxygen Cylinder Capacity:**")
                if p["O2_Cyl"] < 25:
                    st.progress(p["O2_Cyl"] / 100, text=f"⚠️ CRITICAL LEVEL: {p['O2_Cyl']}% Stored Reserves")
                else:
                    st.progress(p["O2_Cyl"] / 100, text=f"Reserves Stable: {p['O2_Cyl']}%")

# --- MODULE 4: WEATHER DATA ---
elif menu == "🌤️ Weather Gateways":
    st.subheader("🌤️ Automated Climate Telemetry Gateway")
    col1, col2, col3 = st.columns(3)
    col1.metric("Bharati Station Temp", "-24°C", "Wind: 18 knots")
    col2.metric("Maitri Station Temp", "-31°C", "Wind: 42 knots")
    col3.metric("Field Camp Alpha Temp", "-45°C", "Wind: 61 knots 🚨", delta_color="inverse")
    st.error("🚨 **AUTOMATED WEATHER MITIGATION RULES:** Ground operations locked at Field Camp Alpha due to zero visibility blizzards.")

# --- MODULE 5: SOS PROTOCOLS ---
elif menu == "🚨 Emergency Response (SOS)":
    st.subheader("⚠️ Emergency Response System (ERS) Control Board")
    st.warning("Pressing the button below activates immediate distress protocols across all international networks.")
