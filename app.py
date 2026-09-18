import streamlit as st
import pandas as pd
import random
import time
import streamlit.components.v1 as components

# 1. Enterprise Dashboard Layout Configuration
st.set_page_config(
    page_title="NCPOR IPELAMS Command Node", 
    page_icon="❄️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 🎨 Clean Enterprise Dark CSS Styling Engine
st.markdown("""
    <style>
    /* Main Layout Framework */
    .stApp {
        background-color: #0b0f17 !important;
        color: #f8fafc !important;
    }
    
    /* Structural Enterprise Data Modules */
    .data-module-card {
        background-color: #111827;
        border: 1px solid #1f2937;
        border-radius: 8px;
        padding: 20px;
        margin-bottom: 15px;
    }
    
    /* Typography Consistency */
    h1, h2, h3, h4 {
        color: #f8fafc !important;
        font-weight: 600 !important;
    }
    
    /* Navigation Sidebar Customization */
    section[data-testid="stSidebar"] {
        background-color: #0b0f17 !important;
        border-right: 1px solid #1f2937 !important;
    }
    </style>
""", unsafe_allow_html=True)

# 2. Simulated Relational Database State (COMNAP Logistics Standard)
if 'comnap_cargo_db' not in st.session_state:
    st.session_state.comnap_cargo_db = pd.DataFrame([
        {"Manifest ID": "MFT-2026-001", "Item": "Aviation Fuel (Jet A-1)", "Category": "Fuel", "Quantity": 1500, "Unit": "Liters", "Min Threshold": 2000, "Status": "CRITICAL"},
        {"Item": "Arctic Survival Rations", "Manifest ID": "MFT-2026-002", "Category": "Food", "Quantity": 5000, "Unit": "Packs", "Min Threshold": 1000, "Status": "SAFE"},
        {"Item": "Thermal Extreme Outerwear", "Manifest ID": "MFT-2026-003", "Category": "Clothing", "Quantity": 120, "Unit": "Sets", "Min Threshold": 50, "Status": "SAFE"},
        {"Item": "Medical Oxygen Cylinders", "Manifest ID": "MFT-2026-004", "Category": "Medical", "Quantity": 15, "Unit": "Cylinders", "Min Threshold": 30, "Status": "CRITICAL"},
    ])

if 'emergency_broadcast_active' not in st.session_state:
    st.session_state.emergency_broadcast_active = False

# --- CORE CONSOLE HEADER ---
st.markdown("""
    <div style="border-left: 4px solid #38bdf8; padding-left: 15px; margin-bottom: 25px;">
        <h2 style='margin: 0; padding: 0;'>INTEGRATED POLAR EXPEDITION LOGISTICS & ASSET MANAGEMENT</h2>
        <p style='margin: 5px 0 0 0; color: #94a3b8; font-size: 13px;'>NATIONAL CENTRE FOR POLAR AND OCEAN RESEARCH (NCPOR) • MINISTRY OF EARTH SCIENCES</p>
    </div>
""", unsafe_allow_html=True)

if st.session_state.emergency_broadcast_active:
    st.error("🚨 EMERGENCY OVERRIDE ENABLED: SOS DISTRESS MATRIX BROADCASTING OVER ACTIVE SATCOM CHANNELS.")

# 3. Sidebar Navigation Panel
with st.sidebar:
    st.markdown("### SYSTEM MODULES")
    menu = st.sidebar.radio(
        "Navigation",
        ["📊 Operations Overview", "🚢 COMNAP Cargo Registry", "🫁 Live Personnel Biometrics", "🌤️ Climate Telemetry Grid", "🚨 Emergency Control System"],
        label_visibility="collapsed"
    )
    st.write("---")
    st.status("Telemetry Link: ACTIVE", state="complete")

# --- MODULE 1: OPERATIONS OVERVIEW (TACTICAL RADAR & VITAL MONITOR INTERFACE) ---
if menu == "📊 Operations Overview":
    st.markdown("### 🌐 Core Telemetry Metrics")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Active Polar Nodes", value="3 Stations", delta="Operational")
    with col2:
        crit_qty = len(st.session_state.comnap_cargo_db[st.session_state.comnap_cargo_db['Status']=='CRITICAL'])
        st.metric(label="Automated Supply Breaches", value=f"{crit_qty} Flagged", delta="Action Required", delta_color="inverse")
    with col3:
        st.metric(label="Downlink Configuration", value="Secure SATCOM", delta="Online")
    
    # ⚡ PURE HTML5 CANVAS ENGINE IMPLEMENTATION (Draws Radar Sweep + Live Sine Wave Medical Charts)
    radar_html = """
    <div style="background-color: #0b0f17; display: flex; flex-direction: row; gap: 20px; padding: 20px; border-radius: 8px; border: 1px solid #1f2937; font-family: sans-serif;">
        <!-- Left Side: Tactical Radar Screen -->
        <div style="flex: 1; text-align: center;">
            <div style="color: #38bdf8; font-size: 14px; font-weight: bold; text-align: left; margin-bottom: 10px; letter-spacing: 1px;">POLAR MAP SYS</div>
            <canvas id="radarCanvas" width="340" height="340" style="background: #0b0f17; border-radius: 50%;"></canvas>
        </div>
        
        <!-- Right Side: Vitals Signal Matrix -->
        <div style="flex: 1.2; display: flex; flex-direction: column; justify-content: space-between;">
            <div style="color: #38bdf8; font-size: 14px; font-weight: bold; margin-bottom: 10px; letter-spacing: 1px;">VITAL STREAM MATRIX (60HZ)</div>
            
            <div style="margin-bottom: 10px;">
                <div style="color: #10b981; font-size: 11px; font-weight: bold; margin-bottom: 2px;">ECG</div>
                <canvas id="ecgCanvas" width="400" height="60" style="background: #0b0f17; border-bottom: 1px solid #1f2937;"></canvas>
            </div>
            <div style="margin-bottom: 10px;">
                <div style="color: #06b6d4; font-size: 11px; font-weight: bold; margin-bottom: 2px;">SPO2</div>
                <canvas id="spo2Canvas" width="400" height="60" style="background: #0b0f17; border-bottom: 1px solid #1f2937;"></canvas>
            </div>
            <div>
                <div style="color: #f59e0b; font-size: 11px; font-weight: bold; margin-bottom: 2px;">RESP</div>
                <canvas id="respCanvas" width="400" height="60" style="background: #0b0f17;"></canvas>
            </div>
        </div>
    </div>

    <script>
        // --- 1. Radar Rendering System ---
        const radarCanvas = document.getElementById('radarCanvas');
        const rCtx = radarCanvas.getContext('2d');
        let angle = 0;
        
        const targets = [
            { name: "S-101", x: 200, y: 140, color: "#10b981" },
            { name: "S-102", x: 250, y: 90, color: "#10b981" },
            { name: "S-105", x: 100, y: 150, color: "#ef4444" },
            { name: "G-201", x: 95, y: 240, color: "#f59e0b" },
            { name: "N-304", x: 270, y: 200, color: "#10b981" }
        ];

        function drawRadar() {
            const cx = radarCanvas.width / 2;
            const cy = radarCanvas.height / 2;
            const r = cx - 10;
            
            rCtx.clearRect(0, 0, radarCanvas.width, radarCanvas.height);
            
            // Outer concentric scope rings
            rCtx.strokeStyle = 'rgba(56, 189, 248, 0.15)';
            rCtx.lineWidth = 1;
            for(let i = 1; i <= 4; i++) {
                rCtx.beginPath();
                rCtx.arc(cx, cy, (r/4)*i, 0, Math.PI * 2);
                rCtx.stroke();
            }
            
            // Crosshairs axes layout lines
            rCtx.beginPath();
            rCtx.moveTo(cx, 0); rCtx.lineTo(cx, radarCanvas.height);
            rCtx.moveTo(0, cy); rCtx.lineTo(radarCanvas.width, cy);
            rCtx.stroke();
            
            // Sweeping radar arm calculation line
            rCtx.strokeStyle = 'rgba(56, 189, 248, 0.6)';
            rCtx.lineWidth = 2;
            rCtx.beginPath();
            rCtx.moveTo(cx, cy);
            rCtx.lineTo(cx + r * Math.cos(angle), cy + r * Math.sin(angle));
            rCtx.stroke();
            
            // Render Target Blips
            targets.forEach(t => {
                rCtx.fillStyle = t.color;
                rCtx.beginPath();
                rCtx.arc(t.x, t.y, 6, 0, Math.PI * 2);
                rCtx.fill();
                
                rCtx.fillStyle = "#94a3b8";
                rCtx.font = "10px sans-serif";
                rCtx.fillText(t.name, t.x + 10, t.y + 4);
            });
            
            angle += 0.015;
            requestAnimationFrame(drawRadar);
        }

        // --- 2. Real-Time Waveform Generator Charts ---
        function setupWave(canvasId, drawFn) {
            const canvas = document.getElementById(canvasId);
            const ctx = canvas.getContext('2d');
            let offset = 0;
            
            function animate() {
                ctx.clearRect(0, 0, canvas.width, canvas.height);
                ctx.lineWidth = 1.5;
                ctx.beginPath();
                drawFn(ctx, canvas.width, canvas.height, offset);
                ctx.stroke();
                offset += 2;
                requestAnimationFrame(animate);
            }
            animate();
        }

        setupWave('ecgCanvas', (ctx, w, h, offset) => {
            ctx.strokeStyle = '#10b981';
            for (let x = 0; x < w; x++) {
                let y = h / 2;
                let phase = (x + offset) % 120;
                if (phase > 40 && phase < 45) y -= 15;
                else if (phase >= 45 && phase < 52) y += 20;
                else if (phase >= 52 && phase < 58) y -= 8;
                
                if (x === 0) ctx.moveTo(x, y); else ctx.lineTo(x, y);
            }
        });

        setupWave('spo2Canvas', (ctx, w, h, offset) => {
            ctx.strokeStyle = '#06b6d4';
            for (let x = 0; x < w; x++) {
                let y = h/2 + Math.sin((x + offset) * 0.04) * 8 + Math.sin((x + offset) * 0.01) * 3;
                if (x === 0) ctx.moveTo(x, y); else ctx.lineTo(x, y);
            }
        });

        setupWave('respCanvas', (ctx, w, h, offset) => {
            ctx.strokeStyle = '#f59e0b';
            for (let x = 0; x < w; x++) {
                let y = h/2 + Math.sin((x + offset) * 0.015) * 12;
                if (x === 0) ctx.moveTo(x, y); else ctx.lineTo(x, y);
            }
        });

        drawRadar();
    </script>
    """
    
    # Securely mount the real-time layout canvas onto the central container box
    components.html(radar_html, height=400)

# --- MODULE 2: COMNAP CARGO REGISTRY ---
elif menu == "🚢 COMNAP Cargo Registry":
    st.markdown("### 🚢 Central Inventory Control Matrix")
    
    critical_items = st.session_state.comnap_cargo_db[st.session_state.comnap_cargo_db['Status'] == 'CRITICAL']
    if not critical_items.empty:
        for idx, row in critical_items.iterrows():
            st.warning(f"🤖 **AUTOMATED INVENTORY AUDIT:** Storage breach logged on `{row['Item']}`. Automated procurement indent dispatched.")

    st.markdown("<div class='data-module-card'>", unsafe_allow_html=True)
    search_box = st.text_input("🔍 Search Database Ledger (Item Name or ID Reference):", "", placeholder="Query item status...")
    
    display_db = st.session_state.comnap_cargo_db
    if search_box:
        display_db = display_db[display_db['Item'].str.contains(search_box, case=False)]
        
    st.dataframe(display_db, use_container_width=True, hide_index=True)
    st.markdown("</div>", unsafe_allow_html=True)
    
    with st.expander("➕ Register New Cargo Container Entry"):
        with st.form("cargo_entry_form", clear_on_submit=True):
            col1, col2 = st.columns(2)
            with col1:
                i_name = st.text_input("Asset Description")
                m_id = st.text_input("Manifest Reference Key", value=f"MFT-2026-{random.randint(100,999)}")
                cat = st.selectbox("Category Group", ["Fuel", "Food", "Clothing", "Medical", "Equipment"])
            with col2:
                current_qty = st.number_input("Current Stored Quantity", min_value=0, value=100)
                u_type = st.text_input("Measurement Unit Label", value="Units")
                safety_t = st.number_input("Minimum Buffer Level", min_value=0, value=50)
            
            if st.form_submit_button("Commit Data Write Sequence"):
                if i_name:
                    stat = "SAFE" if current_qty >= safety_t else "CRITICAL"
                    new_item = {"Manifest ID": m_id, "Item": i_name, "Category": cat, "Quantity": current_qty, "Unit": u_type, "Min Threshold": safety_t, "Status": stat}
                    st.session_state.comnap_cargo_db = pd.concat([st.session_state.comnap_cargo_db, pd.DataFrame([new_item])], ignore_index=True)
                    st.success("Database write sequence finalized.")
                    st.rerun()

# --- MODULE 3: LIVE PERSONNEL BIOMETRICS ---
elif menu == "🫁 Live Personnel Biometrics":
    st.markdown("### 🫁 Biosuit Environmental Medicine & Telemetry")
    st.caption("🔄 Telemetry Polling Rate: 1.0Hz | Status: Online")
    
    team = [
        {"Name": "Dr. Mohemmed Farhan", "Role": "Lead Meteorologist", "Loc": "Bharati Station", "HR": 72, "SYS": 120, "DIA": 80, "SpO2": 98, "Temp": 36.6, "O2": 82},
        {"Name": "Aaron.A.R", "Role": "Logistics Chief", "Loc": "Maitri Station", "HR": 76, "SYS": 122, "DIA": 82, "SpO2": 99, "Temp": 36.8, "O2": 91},
        {"Name": "A.K.Pavan", "Role": "Expedition Leader", "Loc": "Ice Outpost Alpha", "HR": 106, "SYS": 141, "DIA": 92, "SpO2": 91, "Temp": 34.4, "O2": 14}
    ]
    
    for p in team:
        live_hr = p["HR"] + random.randint(-3, 3)
        live_sys = p["SYS"] + random.randint(-4, 4)
        live_dia = p["DIA"] + random.randint(-2, 2)
        live_spo2 = min(100, p["SpO2"] + random.randint(-1, 1))
        live_temp = round(p["Temp"] + random.uniform(-0.2, 0.2), 1)
        
        st.markdown("<div class='data-module-card'>", unsafe_allow_html=True)
        h_col, d_col = st.columns(2)
        with h_col:
            st.markdown(f"#### 👤 {p['Name']}")
            st.markdown(f"<p style='color: #94a3b8; margin: 0;'><b>Assignment:</b> {p['Role']}<br/><b>Current Sector:</b> {p['Loc']}</p>", unsafe_allow_html=True)
        with d_col:
            c1, c2, c3, c4 = st.columns(4)
            c1.metric("❤️ Heart Rate", f"{live_hr} BPM")
            c2.metric("🩺 Blood Pressure", f"{live_sys}/{live_dia} mmHg")
            
            if live_spo2 < 93:
                c3.metric("🚨 Oxygen (SpO2)", f"{live_spo2}%", "HYPOXIA WARNING", delta_color="inverse")
            else:
                c3.metric("🟢 Oxygen (SpO2)", f"{live_spo2}%")
                
            if live_temp < 35.0:
                c4.metric("🥶 Core Body Temp", f"{live_temp}°C", "HYPOTHERMIA RISK", delta_color="inverse")
            else:
                c4.metric("🌡️ Core Body Temp", f"{live_temp}°C")
            
            st.write(f"**Life-Support Oxygen Cylinder Level:** {p['O2']}%")
            st.progress(p["O2"] / 100)
        st.markdown("</div>", unsafe_allow_html=True)

# --- MODULE 4: CLIMATE TELEMETRY ---
elif menu == "🌤️ Climate Telemetry Grid":
    st.markdown("### 🌤️ Regional Climate Sensor Telemetry Matrix")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("<div class='data-module-card'>", unsafe_allow_html=True)
        st.metric("Bharati Station Node", "-22°C", "Wind: 14 knots")
        st.markdown("</div>", unsafe_allow_html=True)
        
    with col2:
        st.markdown("<div class='data-module-card'>", unsafe_allow_html=True)
        st.metric("Maitri Station Node", "-29°C", "Wind: 39 knots")
        st.markdown("</div>", unsafe_allow_html=True)
        
    with col3:
        st.markdown("<div class='data-module-card'>", unsafe_allow_html=True)
        st.metric("Field Camp Outpost Alpha", "-44°C", "Wind: 64 knots 🚨", delta_color="inverse")
        st.markdown("</div>", unsafe_allow_html=True)
        
    st.error("🤖 SYSTEM RISK FLAG: Ground navigation suspended at Outpost Alpha due to blizzard density.")

# --- MODULE 5: EMERGENCY CONTROL SYSTEM ---
elif menu == "🚨 Emergency Control System":
    st.markdown("### ⚠️ Incident Management & Crisis Control Console")
    st.markdown("<div class='data-module-card'>", unsafe_allow_html=True)
    st.warning("SYSTEM NOTE: Distress toggles override telemetry streams and broadcast tracking indices instantly to global emergency outposts.")
    
    col_trigger, col_reset = st.columns(2)
    
    with col_trigger:
        if st.button("🚨 TRIGGER CRISIS OVERRIDE", type="primary", use_container_width=True):
            st.session_state.emergency_broadcast_active = True
            st.rerun()
            
    with col_reset:
        if st.button("✅ RESET SYSTEM BASELINE", use_container_width=True):
            st.session_state.emergency_broadcast_active = False
            st.success("System returned to secure baseline operations status.")
            st.rerun()

    if st.session_state.emergency_broadcast_active:
        st.error("🚨 LIVE LOGISTICS MONITORING STATE: EMERGENCY DISPATCH AND RESCUE FLOW CHANNELS ENGAGED.")
    else:
        st.success("LIVE LOGISTICS MONITORING STATE: System baseline stable.")
    st.markdown("</div>", unsafe_allow_html=True)

# --- 5. AUTOMATED DYNAMIC TIMING REFRESH CONTROLLER LOOP ---
if menu == "🫁 Live Personnel Biometrics":
    time.sleep(1.0)
    st.rerun()
