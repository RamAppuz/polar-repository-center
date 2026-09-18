import streamlit as st
import pandas as pd
import random

# 1. High-Tech Theme Configuration
st.set_page_config(
    page_title="NCPOR Polar Command Center", 
    page_icon="❄️",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("❄️ Integrated Polar Expedition Logistics & Asset Management")
st.caption("🌐 Official Operations Portal | National Centre for Polar and Ocean Research (NCPOR)")
st.write("---")

# 2. Setup Persistent Variables (Simulated System Database)
if 'inventory' not in st.session_state:
    st.session_state.inventory = pd.DataFrame([
        {"Item": "Aviation Fuel (Jet A-1)", "Category": "Fuel", "Quantity": 1500, "Min Threshold": 2000, "Status": "CRITICAL"},
        {"Item": "Arctic Survival Rations", "Category": "Food", "Quantity": 5000, "Min Threshold": 1000, "Status": "SAFE"},
        {"Item": "Thermal Extreme Gear", "Category": "Clothing", "Quantity": 120, "Min Threshold": 50, "Status": "SAFE"},
        {"Item": "Medical Trauma Kits", "Category": "Medical", "Quantity": 15, "Min Threshold": 30, "Status": "CRITICAL"},
    ])

if 'personnel' not in st.session_state:
    st.session_state.personnel = pd.DataFrame([
        {"Name": "Dr. Mohemmed Farhan", "Role": "Lead Meteorologist", "Location": "Bharati Station", "Vitals": "Healthy"},
        {"Name": "Aaron.A.R", "Role": "Logistics Chief", "Location": "Maitri Station", "Vitals": "Healthy"},
        {"Name": "A.K.Pavan", "Role": "Expedition Leader", "Location": "Field Camp Alpha", "Vitals": "Cold Stress Warning"},
    ])

# 3. Enhanced Sidebar Navigation
with st.sidebar:
    st.title("OPERATIONS MENU")
    menu = st.radio(
        "Select Control Module:",
        ["📊 Main Overview", "📦 Cargo & Inventory", "👤 Personnel Safety", "🌤️ Polar Weather Monitoring", "🚨 Emergency Response (SOS)"]
    )
    st.write("---")
    st.status("📡 Satellite Sync: ACTIVE", state="complete")

# --- MODULE 1: MAIN OVERVIEW & MAP FIX ---
if menu == "📊 Main Overview":
    st.subheader("📍 Real-Time Spatial Positioning & Telemetry")
    
    m1, m2, m3 = st.columns(3)
    m1.metric(label="Active Stations", value="3", delta="Online")
    m2.metric(label="Critical Assets", value=f"{len(st.session_state.inventory[st.session_state.inventory['Status']=='CRITICAL'])} Items", delta="-500 L Fuel", delta_color="inverse")
    m3.metric(label="Personnel in Field", value=f"{len(st.session_state.personnel)} Members", delta="Operational")
    
    # Corrected Coordinates for Antarctica plotting map points cleanly
    map_data = pd.DataFrame({
        'latitude': [-69.4083, -70.7667, -74.0000],
        'longitude': [76.1944, 11.7333, 35.0000]
    })
    
    st.write("#### Live Deployment Map (Antarctica Research Grid)")
    # Using specific mapping coordinates to auto-center near the bottom region
    st.map(map_data, size=20000)

# --- MODULE 2: CARGO & INVENTORY ---
elif menu == "📦 Cargo & Inventory":
    st.subheader("📦 Supply Chain & Central Inventory Management")
    
    critical_items = st.session_state.inventory[st.session_state.inventory['Status'] == 'CRITICAL']
    if not critical_items.empty:
        for idx, row in critical_items.iterrows():
            st.error(f"🤖 **AUTOMATED SYSTEM ALERT:** Stock alert on `{row['Item']}`! Inventory is below minimum safety threshold. Reorder ping sent to NCPOR HQ.")

    st.write("#### Current Stock Levels")
    st.dataframe(st.session_state.inventory, use_container_width=True)
    
    st.write("---")
    with st.expander("➕ Register New Cargo Container / Asset"):
        with st.form("add_item_form", clear_on_submit=True):
            name = st.text_input("Item Name")
            category = st.selectbox("Category", ["Fuel", "Food", "Clothing", "Medical", "Equipment"])
            qty = st.number_input("Current Quantity", min_value=0, value=100)
            threshold = st.number_input("Minimum Safety Threshold", min_value=0, value=50)
            
            submit = st.form_submit_button("Log Asset to System")
            if submit and name:
                status = "SAFE" if qty >= threshold else "CRITICAL"
                new_row = {"Item": name, "Category": category, "Quantity": qty, "Min Threshold": threshold, "Status": status}
                st.session_state.inventory = pd.concat([st.session_state.inventory, pd.DataFrame([new_row])], ignore_index=True)
                st.success(f"Tracked: {name}")
                st.rerun()

# --- MODULE 3: PERSONNEL SAFETY ---
elif menu == "👤 Personnel Safety":
    st.subheader("👤 Real-Time Team Tracking & Biometrics")
    
    for idx, row in st.session_state.personnel.iterrows():
        with st.container(border=True):
            c1, c2, c3 = st.columns(3)
            c1.markdown(f"**Member:** {row['Name']}  \n*Role:* {row['Role']}")
            c2.markdown(f"📍 **Position:**  \n{row['Location']}")
            
            if "Warning" in row['Vitals']:
                c3.error(f"⚠️ Vitals: {row['Vitals']}")
            else:
                c3.success(f"💚 Vitals: {row['Vitals']}")

# --- MODULE 4: NEW WEATHER RADAR INTERFACE ---
elif menu == "🌤️ Polar Weather Monitoring":
    st.subheader("🌤️ Automated Climate Telemetry")
    st.info("🤖 **Automation Rule Active:** Logistics tracks are locked if wind velocities cross 55 knots.")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Bharati Station Temp", "-24°C", "Wind: 18 knots")
    col2.metric("Maitri Station Temp", "-31°C", "Wind: 42 knots")
    
    # Simulate a dangerous condition for the presentation
    col3.metric("Field Camp Alpha Temp", "-45°C", "Wind: 61 knots 🚨", delta_color="inverse")
    
    st.error("🚨 **AUTOMATED HAZARD MITIGATION:** Extreme blizzard velocities detected at Field Camp Alpha. Personnel deployment capabilities are suspended automatically until visibility parameters clear.")

# --- MODULE 5: EMERGENCY RESPONSE ---
elif menu == "🚨 Emergency Response (SOS)":
    st.subheader("⚠️ Emergency Response System (ERS) Control Board")
    
    st.warning("Pressing the button below activates immediate distress protocols across all international networks.")
    sos = st.button("🚨 BROADCAST RED ALERT PROTOCOL", type="primary", use_container_width=True)
    
    if sos:
        st.error("🚨 CRISIS MANIFEST ACTIVE: Emergency alerts broadcasted via global iridium networks. Remote rescue vehicles deployed.")
