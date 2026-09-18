import streamlit as st
import pandas as pd
import random
import time
import pydeck as pdk

# 1. Hyper-Tech Theme & UI Architecture Configuration
st.set_page_config(
    page_title="NCPOR IPELAMS Command Node", 
    page_icon="❄️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 🎨 Cyberpunk Tactical Custom CSS Styling Engine
st.markdown("""
    <style>
    /* Main Layout Theming */
    .stApp {
        background-color: #030712 !important;
        background-image: radial-gradient(circle at 50% 0%, #0f172a 0%, #030712 70%) !important;
        color: #f8fafc !important;
        font-family: 'Courier New', Courier, monospace !important;
    }
    
    /* Neon Command Containers */
    .tactical-card {
        background: rgba(15, 23, 42, 0.6);
        border: 1px solid #1e293b;
        border-radius: 12px;
        padding: 20px;
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.4);
        backdrop-filter: blur(5px);
        margin-bottom: 15px;
        transition: all 0.3s ease;
    }
    .tactical-card:hover {
        border-color: #06b6d4;
        box-shadow: 0 0 15px rgba(6, 182, 212, 0.2);
    }
    
    /* Custom Neon Metric Badges */
    .neon-text-cyan { color: #06b6d4 !important; font-weight: bold; font-size: 24px; text-shadow: 0 0 8px rgba(6, 182, 212, 0.6); }
    .neon-text-red { color: #ef4444 !important; font-weight: bold; font-size: 24px; text-shadow: 0 0 8px rgba(239, 68, 68, 0.6); }
    .neon-text-green { color: #10b981 !important; font-weight: bold; font-size: 24px; text-shadow: 0 0 8px rgba(16, 185, 129, 0.6); }
    
    /* Header Titles */
    h1 {
        color: #f8fafc !important;
        text-transform: uppercase;
        letter-spacing: 2px;
        text-shadow: 0 0 10px rgba(255, 255, 255, 0.1);
    }
    
    /* Streamlit Sidebar Overrides */
    section[data-testid="stSidebar"] {
        background-color: #090d16 !important;
        border-right: 1px solid #1e293b !important;
    }
    
    /* Dataframe Grid Customization */
    .stDataFrame {
        border: 1px solid #1e293b !important;
        border-radius: 8px !important;
        overflow: hidden;
    }
    </style>
""", unsafe_allow_html=True)

# 2. Simulated Decentralized Database Initialization (COMNAP Core)
if 'comnap_cargo_db' not in st.session_state:
    st.session_state.comnap_cargo_db = pd.DataFrame([
        {"Manifest ID": "MFT-2026-001", "Item": "Aviation Fuel (Jet A-1)", "Category": "Fuel", "Quantity": 1500, "Unit": "Liters", "Min Threshold": 2000, "Status": "CRITICAL"},
        {"Item": "Arctic Survival Rations", "Manifest ID": "MFT-2026-002", "Category": "Food", "Quantity": 5000, "Unit": "Packs", "Min Threshold": 1000, "Status": "SAFE"},
        {"Item": "Thermal Extreme Outerwear", "Manifest ID": "MFT-2026-003", "Category": "Clothing", "Quantity": 120, "Unit": "Sets", "Min Threshold": 50, "Status": "SAFE"},
        {"Item": "Medical Oxygen Cylinders", "Manifest ID": "MFT-2026-004", "Category": "Medical", "Quantity": 15, "Unit": "Cylinders", "Min Threshold": 30, "Status": "CRITICAL"},
    ])

if 'emergency_broadcast_active' not in st.session_state:
    st.session_state.emergency_broadcast_active = False

# --- SYSTEM GLOBAL HEADER BANNER ---
st.markdown("""
    <div style="border-left: 4px solid #06b6d4; padding-left: 15px; margin-bottom: 20px;">
        <h1 style='margin: 0; padding: 0;'>⚡ IPELAMS TACTICAL COMMAND NODE</h1>
        <p style='margin: 5px 0 0 0; color: #94a3b8; font-size: 13px;'>MINISTRY OF EARTH SCIENCES (MoES) • NATIONAL CENTRE FOR POLAR AND OCEAN RESEARCH (NCPOR)</p>
    </div>
""", unsafe_allow_html=True)

if st.session_state.emergency_broadcast_active:
    st.markdown("""
        <div style="background-color: rgba(239, 68, 68, 0.1); border: 1px solid #ef4444; border-radius: 8px; padding: 15px; margin-bottom: 20px; animation: pulse 2s infinite;">
            <span style="color: #ef4444; font-weight: bold; font-size: 16px;">🚨 GLOBAL CRITICAL OVERRIDE: SOS DISTRESS MATRIX BROADCASTING OVER SATCOM NETWORKS</span>
        </div>
    """, unsafe_allow_html=True)

# 3. Sidebar Tactical Engine Menu
with st.sidebar:
    st.markdown("<h3 style='color: #06b6d4; letter-spacing: 1px;'>📡 NAV-COM DATA LINK</h3>", unsafe_allow_html=True)
    menu = st.radio(
        "SELECT MODULE EXECUTION:",
        ["📊 Operations Overview", "🚢 COMNAP Cargo Registry", "🫁 Live Personnel Biometrics", "🌤️ Climate Telemetry Grid", "🚨 Emergency Control System"],
        label_visibility="collapsed"
    )
    st.write("---")
    st.status("Telemetry Stream: SYNCHRONIZED", state="running")

# --- MODULE 1: OPERATIONS OVERVIEW (CLEAN 3D VECTOR MATRIX MAP) ---
if menu == "📊 Operations Overview":
    st.markdown("### 🌐 Spatial Node Positioning Metrics")
    
    # Custom Styled Flex Columns
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f"""<div class='tactical-card'>
            <span style='color: #94a3b8; font-size: 12px;'>POLAR NODES SYSTEM STATUS</span><br/>
            <span class='neon-text-green'>03 STATIONS ONLINE</span>
        </div>""", unsafe_allow_html=True)
    with col2:
        crit_qty = len(st.session_state.comnap_cargo_db[st.session_state.comnap_cargo_db['Status']=='CRITICAL'])
        st.markdown(f"""<div class='tactical-card'>
            <span style='color: #94a3b8; font-size: 12px;'>AUTOMATED INVENTORY BREACHES</span><br/>
            <span class='neon-text-red'>{crit_qty} CRITICAL ALERTS</span>
        </div>""", unsafe_allow_html=True)
    with col3:
        st.markdown(f"""<div class='tactical-card'>
            <span style='color: #94a3b8; font-size: 12px;'>SATELLITE DOWNLINK STATUS</span><br/>
            <span class='neon-text-cyan'>SECURE TRANS-LINK</span>
        </div>""", unsafe_allow_html=True)
    
    st.markdown("#### 🗺️ 3D Tactical Vector Mesh Grid (Antarctic Coast Matrix)")
    
    map_data = pd.DataFrame([
        {"name": "Bharati Station (India)", "latitude": -69.4083, "longitude": 76.1944},
        {"name": "Maitri Station (India)", "latitude": -70.7667, "longitude": 11.7333},
        {"name": "Field Camp Alpha", "latitude": -72.0000, "longitude": 45.0000}
    ])
    
    view_state = pdk.ViewState(latitude=-68.0, longitude=45.0, zoom=2.2, pitch=35)
    
    layer = pdk.Layer(
        "ScatterplotLayer",
        map_data,
        get_position=["longitude", "latitude"],
        get_color=[6, 182, 212, 200],  # Cyan neon color engine
        get_radius=140000,
        pickable=True
    )
    
    st.pydeck_chart(pdk.Deck(
        map_style="mapbox://styles/mapbox/dark-v11", 
        initial_view_state=view_state,
        layers=[layer],
        tooltip={"text": "{name}"}
    ))

# --- MODULE 2: COMNAP CARGO REGISTRY ---
elif menu == "🚢 COMNAP Cargo Registry":
    st.markdown("### 🚢 COMNAP Central Stockpile Ledger Matrix")
    
    critical_items = st.session_state.comnap_cargo_db[st.session_state.comnap_cargo_db['Status'] == 'CRITICAL']
    if not critical_items.empty:
        for idx, row in critical_items.iterrows():
            st.markdown(f"""<div style='background-color: rgba(239,68,68,0.05); border-left: 3px solid #ef4444; padding: 10px; margin-bottom: 10px; font-size: 13px;'>
                🤖 <b>SMART AUTO-INDENT TRACER:</b> Supply depletion logged on <code>{row['Item']}</code>. Automated replenishment request dispatched to NCPOR HQ.
            </div>""", unsafe_allow_html=True)

    st.markdown("<div class='tactical-card'>", unsafe_allow_html=True)
    search_box = st.text_input("🔍 Query Ledger Database (Keyword or ID Ref):", "", placeholder="Type to filter...")
    
    display_db = st.session_state.comnap_cargo_db
    if search_box:
        display_db = display_db[display_db['Item'].str.contains(search_box, case=False)]
        
    st.dataframe(display_db, use_container_width=True, hide_index=True)
    st.markdown("</div>", unsafe_allow_html=True)
    
    with st.expander("➕ Inject New Asset Tracking Log"):
        with st.form("cargo_entry_form", clear_on_submit=True):
            col1, col2 = st.columns(2)
            with col1:
                i_name = st.text_input("Asset Label Description")
                m_id = st.text_input("Manifest Registry Key Reference", value=f"MFT-2026-{random.randint(100,999)}")
                cat = st.selectbox("Category Grouping", ["Fuel", "Food", "Clothing", "Medical", "Equipment"])
            with col2:
                current_qty = st.number_input("Registered Storage Quantities", min_value=0, value=100)
                u_type = st.text_input("Unit Scale Label", value="Units")
                safety_t = st.number_input("System Buffer Guard Levels", min_value=0, value=50)
            
            if st.form_submit_button("Commit Node Data Write Sequence"):
                if i_name:
                    stat = "SAFE" if current_qty >= safety_t else "CRITICAL"
                    new_item = {"Manifest ID": m_id, "Item": i_name, "Category": cat, "Quantity": current_qty, "Unit": u_type, "Min Threshold": safety_t, "Status": stat}
                    st.session_state.comnap_cargo_db = pd.concat([st.session_state.comnap_cargo_db, pd.DataFrame([new_item])], ignore_index=True)
                    st.success("Database update sequence finalized.")
                    st.rerun()

# --- MODULE 3: LIVE PERSONNEL BIOMETRICS ---
elif menu == "🫁 Live Personnel Biometrics":
    st.markdown("### 🫁 Biosuit High-Frequency Radio Telemetry Stream")
    st.caption("🔄 Telemetry Loop Sync: Active | Data frame polling intervals: 1.0 seconds.")
    
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
        
        st.markdown("<div class='tactical-card'>", unsafe_allow_html=True)
        h_col, d_col = st.columns([1, 2])
        
        with h_col:
            st.markdown(f"### 👤 {p['Name']}")
            st.markdown(f"<span style='color: #06b6d4; font-size: 13px;'><b>Role:</b> {p['Role']}</span>", unsafe_allow_html=True)
            st.markdown(f"<p style='margin-top: 5px; color: #94a3b8;'>📍 Node: {p['Loc']}</p>", unsafe_allow_html=True)
            
        with d_col:
            c1, c2, c3, c4 = st.columns(4)
            c1.metric("❤️ Heart Rate", f"{live_hr} BPM")
            c2.metric("🩺 Blood Pressure", f"{live_sys}/{live_dia} mmHg")
            
            if live_spo2 < 93:
                c3.metric("🚨 Oxygen (SpO2)", f"{live_spo2}%", "HYPOXIA ALARM", delta_color="inverse")
            else:
                c3.metric("🟢 Oxygen (SpO2)", f"{live_spo2}%")
                
            if live_temp < 35.0:
                c4.metric("🥶 Core Body Temp", f"{live_temp}°C", "HYPOTHERMIA ALERT", delta_color="inverse")
            else:
                c4.metric("🌡️ Core Body Temp", f"{live_temp}°C")
            
            st.write(f"**Life-Support Oxygen Cylinder Reserves Level:** {p['O2']}%")
            st.progress(p["O2"] / 100)
            
        st.markdown("</div>", unsafe_allow_html=True)

# --- MODULE 4: CLIMATE TELEMETRY ---
elif menu == "🌤️ Climate Telemetry Grid":
    st.markdown("### 🌤️ Automated Environmental Sensor Array")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("<div class='tactical-card'>", unsafe_allow_html=True)
        st.metric("Bharati Station Node", "-22°C", "Wind: 14 knots")
        st.markdown("</div>", unsafe_allow_html=True)
        
    with col2:
        st.markdown("<div class='tactical-card'>", unsafe_allow_html=True)
        st.metric("Maitri Station Node", "-29°C", "Wind: 39 knots")
        st.markdown("</div>", unsafe_allow_html=True)
        
    with col3:
        st.markdown("<div class='tactical-card'>", unsafe_allow_html=True)
        st.metric("Field Camp Outpost Alpha", "-44°C", "Wind: 64 knots 🚨", delta_color="inverse")
        st.markdown("</div>", unsafe_allow_html=True)
        
    st.error("🤖 AUTOMATED ECO-MITIGATION ENFORCEMENT: Environmental hazard thresholds crossed at Outpost Alpha. Ground supply operations are automatically locked.")

# --- MODULE 5: EMERGENCY CONTROL SYSTEM ---
elif menu == "🚨 Emergency Control System":
    st.markdown("### ⚠️ Crisis Mitigation Control Console")
    st.markdown("<div class='tactical-card'>", unsafe_allow_html=True)
    st.warning("CRITICAL SYSTEM DIRECTIVE: Activating the distress override switches redirects all active telemetry nodes into high-priority tracking loops.")
    
    col_trigger, col_reset = st.columns(2)
    
    with col_trigger:
        if st.button("🚨 DISTRESS OVERRIDE STATE", type="primary", use_container_width=True):
            st.session_state.emergency_broadcast_active = True
            st.rerun()
            
    with col_reset:
        if st.button("✅ RE-ENGAGE STANDBY TRACKING PROTOCOLS", use_container_width=True):
            st.session_state.emergency_broadcast_active = False
            st.success("Tactical arrays scaled back to safe system baselines.")
            st.rerun()

    if st.session_state.emergency_broadcast_active:
        st.error("🚨 LIVE LOGISTICS MONITORING STATE: IMMEDIATE DISTRESS MANIFEST SIGNALS ENFORCED.")
    else:
        st.success("✅ LIVE LOGISTICS MONITORING STATE: Operational boundaries functioning normally.")
    st.markdown("</div>", unsafe_allow_html=True)

# --- 5. AUTOMATED DYNAMIC TIMING REFRESH CONTROLLER LOOP ---
if menu == "🫁 Live Personnel Biometrics":
    time.sleep(1.0)
    st.rerun()
