import streamlit as st
import pandas as pd
import random
import time

# 1. High-Tech Theme Configuration
st.set_page_config(
    page_title="NCPOR Polar Command Center", 
    page_icon="❄️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. COMNAP-Standard Central Database Initialization
if 'comnap_cargo_db' not in st.session_state:
    st.session_state.comnap_cargo_db = pd.DataFrame([
        {"Manifest ID": "MFT-2026-001", "Item": "Aviation Fuel (Jet A-1)", "Category": "Fuel", "Quantity": 1500, "Unit": "Liters", "Min Threshold": 2000, "Hazard Class": "Class 3 (Flammable)", "Status": "CRITICAL"},
        {"Item": "Arctic Survival Rations", "Manifest ID": "MFT-2026-002", "Category": "Food", "Quantity": 5000, "Unit": "Packs", "Min Threshold": 1000, "Hazard Class": "Non-Hazardous", "Status": "SAFE"},
        {"Item": "Thermal Extreme Outerwear", "Manifest ID": "MFT-2026-003", "Category": "Clothing", "Quantity": 120, "Unit": "Sets", "Min Threshold": 50, "Hazard Class": "Non-Hazardous", "Status": "SAFE"},
        {"Item": "Medical Trauma Oxygen Units", "Manifest ID": "MFT-2026-004", "Category": "Medical", "Quantity": 15, "Unit": "Cylinders", "Min Threshold": 30, "Hazard Class": "Class 2.2 (Gas)", "Status": "CRITICAL"},
    ])

# 3. Enhanced Sidebar Navigation & Real-time Loop Control
with st.sidebar:
    st.image("https://icons8.com", width=70)
    st.title("COMNAP OPERATIONALS")
    menu = st.radio(
        "Select Control Module:",
        ["📊 Main Telemetry", "🚢 COMNAP Cargo Registry", "🫁 Live Personnel Biometrics", "🌤️ Weather Gateways", "🚨 Emergency Response (SOS)"]
    )
    st.write("---")
    
    # Live loop trigger for the fluctuating vitals feature
    st.subheader("⚙️ Stream Configuration")
    live_flux = st.toggle("Enable Live High-Frequency Telemetry", value=True)
    if live_flux:
        st.caption("🔄 System auto-refreshing database state every 2 seconds...")

# Header UI Elements
st.title("❄️ Integrated Polar Expedition Logistics & Asset Management")
st.caption("🌐 Official Operations Portal | National Centre for Polar and Ocean Research (NCPOR) | COMNAP Compatible Interface")
st.write("---")

# --- MODULE 1: MAIN TELEMETRY OVERVIEW ---
if menu == "📊 Main Telemetry":
    st.subheader("📍 Real-Time Spatial Positioning & Grid Diagnostics")
    
    m1, m2, m3 = st.columns(3)
    m1.metric(label="Active Polar Nodes", value="3", delta="Online")
    critical_count = len(st.session_state.comnap_cargo_db[st.session_state.comnap_cargo_db['Status']=='CRITICAL'])
    m2.metric(label="Critical Registry Stocks", value=f"{critical_count} Items", delta="Action Required", delta_color="inverse")
    m3.metric(label="Field Deployments Registered", value="3 Members", delta="Connected")
    
    map_data = pd.DataFrame({
        'latitude': [-69.4083, -70.7667, -74.0000],
        'longitude': [76.1944, 11.7333, 35.0000]
    })
    st.write("#### Live Deployment Map (Antarctica Research Grid)")
    st.map(map_data, size=20000)

# --- MODULE 2: COMNAP CARGO REGISTRY DATABASE ---
elif menu == "🚢 COMNAP Cargo Registry":
    st.subheader("🚢 Central Vessel & Station Cargo Inventory Database")
    
    # Automated Alert Rule Triggers
    critical_items = st.session_state.comnap_cargo_db[st.session_state.comnap_cargo_db['Status'] == 'CRITICAL']
    if not critical_items.empty:
        for idx, row in critical_items.iterrows():
            st.error(f"🤖 **AUTOMATED LOGISTICS AGENT:** Core stock breach on `{row['Item']}` (ID: {row['Manifest ID']}). Current storage levels are below safety buffers. Supply routing requested via NCPOR HQ.")

    st.write("#### Verified Inventory Database Ledger")
    st.dataframe(st.session_state.comnap_cargo_db, use_container_width=True)
    
    # Form to insert items into the simulated database
    with st.expander("➕ Inject New Cargo Manifest Entry into Database"):
        with st.form("comnap_db_form", clear_on_submit=True):
            col1, col2 = st.columns(2)
            with col1:
                item_name = st.text_input("Item Name / Description")
                manifest_id = st.text_input("Manifest ID Reference", value=f"MFT-2026-{random.randint(100,999)}")
                category = st.selectbox("Inventory Category", ["Fuel", "Food", "Clothing", "Medical", "Expedition Equipment"])
            with col2:
                qty = st.number_input("Current Stored Quantity", min_value=0, value=100)
                unit_type = st.text_input("Measurement Unit (e.g. Liters, Units, Cylinders)", value="Units")
                threshold = st.number_input("Minimum Buffer Threshold Level", min_value=0, value=50)
                hazard_class = st.selectbox("Hazard Classification", ["Non-Hazardous", "Class 2.2 (Gas)", "Class 3 (Flammable)", "Class 9 (Miscellaneous Dangerous Goods)"])
            
            submit = st.form_submit_button("Commit Entry to Database Ledger")
            if submit and item_name:
                status = "SAFE" if qty >= threshold else "CRITICAL"
                new_entry = {
                    "Manifest ID": manifest_id, "Item": item_name, "Category": category, 
                    "Quantity": qty, "Unit": unit_type, "Min Threshold": threshold, 
                    "Hazard Class": hazard_class, "Status": status
                }
                st.session_state.comnap_cargo_db = pd.concat([st.session_state.comnap_cargo_db, pd.DataFrame([new_entry])], ignore_index=True)
                st.success(f"Database Write Confirmed: Verified entry logged for {item_name}.")
                st.rerun()

# --- MODULE 3: LIVE PERSONNEL BIOMETRICS ---
elif menu == "🫁 Live Personnel Biometrics":
    st.subheader("👤 Real-Time Environmental Medicine & Biometric Stream")
    st.info("💡 **Per-Second Fluctuations Active:** These values simulate high-frequency radio pings directly from polar biosuits.")
    
    # Setup our team array with real-time changing numbers
    personnel_data = [
        {"Name": "Dr. Aarav Sharma", "Role": "Lead Meteorologist", "Loc": "Bharati Station", "Base_HR": 72, "Base_BP": 120, "Base_SpO2": 98, "Base_Temp": 36.6, "O2_Cyl": 4},
        {"Name": "Sarah Jenkins", "Role": "Logistics Chief", "Loc": "Maitri Station", "Base_HR": 78, "Base_BP": 122, "Base_SpO2": 99, "Base_Temp": 36.8, "O2_Cyl": 5},
        {"Name": "Cmdr. Rajesh Kumar", "Role": "Expedition Leader", "Loc": "Ice Shelf Field Camp", "Base_HR": 105, "Base_BP": 138, "Base_SpO2": 93, "Base_Temp": 34.9, "O2_Cyl": 1}
    ]
    
    for p in personnel_data:
        # Inject randomized minor variations per execution cycle for extreme realism
        current_hr = p["Base_HR"] + random.randint(-4, 4)
        current_sbp = p["Base_BP"] + random.randint(-5, 5)
        current_dbp = 80 + random.randint(-4, 4)
        current_spo2 = min(100, p["Base_SpO2"] + random.randint(-1, 1))
        current_temp = round(p["Base_Temp"] + random.uniform(-0.3, 0.3), 1)
        
        with st.container(border=True):
            col1, col2, col3, col4 = st.columns([1.5, 1.5, 2, 1])
            
            with col1:
                st.markdown(f"📊 **{p['Name']}**\n\n*Role:* {p['Role']}  \n📍 *Node:* {p['Loc']}")
            
            with col2:
                st.markdown(f"❤️ **Heart Rate:** {current_hr} BPM")
                st.markdown(f"🩺 **Blood Pressure:** {current_sbp}/{current_dbp} mmHg")
                
            with col3:
                # Add conditional styling indicators for oxygen levels and deep cold body temps
                if current_spo2 < 95:
                    st.markdown(f"🚨 **Oxygen Saturation (SpO2):** `{current_spo2}% (HYPOXIA WARNING)`")
                else:
                    st.markdown(f"🟢 **Oxygen Saturation (SpO2):** {current_spo2}%")
                    
                if current_temp < 35.5:
                    st.markdown(f"🥶 **Core Temp:** `{current_temp}°C (Hypothermia Risk)`")
                else:
                    st.markdown(f"🌡️ **Core Temp:** {current_temp}°C")
                    
            with col4:
                # Oxygen tank metrics display
                if p["O2_Cyl"] <= 1:
                    st.metric(label="⛽ O2 Cylinders Left", value=p["O2_Cyl"], delta="CRITICAL LOW", delta_color="inverse")
                else:
                    st.metric(label="⛽ O2 Cylinders Left", value=p["O2_Cyl"], delta="Optimal Status")

# --- MODULE 4: WEATHER DATA ---
elif menu == "🌤️ Weather Gateways":
    st.subheader("🌤️ Automated Climate Telemetry Gateway")
    col1, col2, col3 = st.columns(3)
    col1.metric("Bharati Station Temp", "-24°C", "Wind: 18 knots")
    col2.metric("Maitri Station Temp", "-31°C", "Wind: 42 knots")
    col3.metric("Field Camp Alpha Temp", "-45°C", "Wind: 61 knots 🚨", delta_color="inverse")
    st.error("🚨 **AUTOMATED WEATHER MITIGATION RULES:** Safety parameters breached at Field Camp Alpha. Ground routing suspended.")

# --- MODULE 5: SOS PROTOCOLS ---
elif menu == "🚨 Emergency Response (SOS)":
    st.subheader("⚠️ Emergency Response System (ERS) Control Board")
    st.warning("Pressing the button below activates immediate distress protocols across all international networks.")
    if st.button("🚨 BROADCAST RED ALERT PROTOCOL", type="primary", use_container_width=True):
        st.error("🚨 CRISIS MANIFEST ACTIVE: Emergency alerts broadcasted via global iridium networks. Remote rescue vehicles deployed.")

# 4. Infinite Loop Controller logic to drive real-time telemetry changes automatically
if live_flux and menu == "🫁 Live Personnel Biometrics":
    time.sleep(2)
    st.rerun()
