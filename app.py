import streamlit as st

# 1. Global Page Settings
st.set_page_config(
    page_title="Shadrick Carr | Engineering Hub", 
    page_icon="💻", 
    layout="wide"
)

# 2. Sidebar Navigation Panel
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Go to page:", 
    ["Overview", "Cloud Infrastructure", "Linux Automation", "Networking Labs"]
)

# 3. PAGE 1: OVERVIEW PANEL
if page == "Overview":
    st.title("Shadrick Carr")
    st.subheader("Software & Cloud Technology Engineer")
    st.write("---")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### Professional Summary")
        st.write("""
        Multi-industry technology practitioner transitioning deep operational logistics, 
        systems infrastructure knowledge, and advanced automation skills into core 
        Software and Cloud Engineering frameworks. Focused on programmatically scaling, 
        optimizing, and securing microservice application tiers.
        """)
        
        st.markdown("### Technical Toolkit Matrix")
        st.write("**Operating Systems:** Linux (Ubuntu/RHEL Server), macOS")
        st.write("**Infrastructure as Code / Cloud:** Terraform, Amazon Web Services (AWS)")
        st.write("**Networking Architecture:** TCP/IP, Cisco IOS CLI, Subnetting/VLSM, VLANs")
        st.write("**Languages & Version Control:** Python, Bash Shell Scripting, Git/GitHub, Cursor AI")

    with col2:
        st.info("💡 **Active Sandbox Status**\n\nAll primary backend repository trees are fully operational, version-controlled, and validated via live console telemetry traces.")

# 4. PAGE 2: CLOUD INFRASTRUCTURE (IaC)
elif page == "Cloud Infrastructure":
    st.title("☁️ Automated Cloud Infrastructure")
    st.subheader("Declarative Provisioning via Infrastructure as Code (IaC)")
    st.write("---")
    
    st.markdown("### Core Project: Multi-Tier AWS VPC Production Stack")
    st.write("""
    Architected and executed an automated programmatic deployment blueprint using **Terraform** to spin up isolated production microservice components seamlessly on AWS.
    """)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### Systems Provisions Architected:")
        st.write("✔️ **Custom VPC Boundary:** 10.0.0.0/16 virtual private network perimeter isolation.")
        st.write("✔️ **Public Subnet Topology:** Tiered network partition mapping block schemes.")
        st.write("✔️ **Edge Internet Gateway (IGW):** Bi-directional public internet pipeline mapping.")
        st.write("✔️ **Stateful Firewall Group:** Strict rule matrices locking down HTTP (80) and SSH (22).")
        st.write("✔️ **Compute Resource Tier:** Automated provision of an active EC2 Ubuntu instance tier.")

    with col2:
        st.markdown("#### DevOps Best Practices Implemented:")
        st.write("🔬 **Dry-Run Compilation:** Pre-flight sanity validation via `terraform plan` execution logs.")
        st.write("🛡️ **Dependency Mitigation:** Programmatic tracking security parameter isolation via custom `.gitignore` rules.")
        st.write("🧹 **Lifecycle Reclamations:** Clean stack environment dismantling via complete `terraform destroy` sequences.")

    st.write("---")
    st.markdown("### 📊 Live Console Deployment Telemetry")
    
    st.image(
        "images/aws-deployment-success.png", 
        caption="AWS Management EC2 Console verifying successful programmatic deployment of prod-web-server via Terraform.",
        width=None
    )
    
    st.write("\n")
    
    st.link_button(
        "View Source Code & IaC Scripts on GitHub 🚀", 
        "https://github.com/Scarr77/cloud-fundamentals"
    )

# 5. PAGE 3: LINUX AUTOMATION
elif page == "Linux Automation":
    st.title("🐧 Automated Linux Systems Orchestration")
    st.subheader("Bash Scripting & Core Server Administration Modules")
    st.write("---")
    
    st.markdown("### Core Project: Shell Script System Health Monitor")
    st.write("""
    Engineered a production-ready **Bash shell script** (`system_health.sh`) designed to sit on remote 
    server layers and continuously track system metric stability (disk utilization, partition bounds, and core allocation pools).
    """)
    
    with st.expander("📝 View Raw Automation Script Source Code"):
        try:
            with open("system_health.sh", "r") as f:
                script_code = f.read()
            st.code(script_code, language="bash")
        except FileNotFoundError:
            st.error("Could not find system_health.sh file in the project directory.")
        
    st.write("\n")
    st.markdown("### 📋 Live Engine Analysis Log Output")
    st.write("The window below displays real-time telemetry parses directly from the physical `system_health.log` generated natively:")

    try:
        with open("system_health.log", "r") as f:
            log_contents = f.read()
        st.text_area(label="System Log Terminal View", value=log_contents, height=250, label_visibility="collapsed")
    except FileNotFoundError:
        st.warning("⚠️ Telemetry engine log not detected yet. Run './system_health.sh' in your terminal to initialize system metrics.")

# 6. PAGE 4: NETWORKING LABS (Interactive App)
elif page == "Networking Labs":
    st.title("🎛️ Networking Architecture & Topologies")
    st.subheader("Cisco Systems Infrastructure & Algorithmic Subnetting")
    st.write("---")
    
    st.markdown("### Core Concept: Subnetting Engineering & Boundary Calculations")
    st.write("""
    In enterprise systems, breaking down IP blocks into precise subnets is critical for security isolation, 
    broadcast domain containment, and structural routing. Below is an active, programmatic **Subnet Explorer Engine** written in Python to calculate mask metrics instantly.
    """)
    
    st.write("\n")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("#### ⚡ Subnet Engine Inputs")
        ip_input = st.text_input("Enter Base Network IP Address:", "192.168.1.0")
        cidr_select = st.slider("Select CIDR Prefix Slash Notation (/) Mask:", min_value=24, max_value=30, value=24)
    
    with col2:
        st.markdown("#### 📊 Processed Architecture Output")
        
        hosts_matrix = {24: 254, 25: 126, 26: 62, 27: 30, 28: 14, 29: 6, 30: 2}
        mask_matrix = {24: "255.255.255.0", 25: "255.255.255.128", 26: "255.255.255.192", 27: "255.255.255.224", 28: "255.255.255.240", 29: "255.255.255.248", 30: "255.255.255.252"}
        
        usable_hosts = hosts_matrix[cidr_select]
        subnet_mask = mask_matrix[cidr_select]
        
        st.metric(label="Calculated Subnet Mask", value=subnet_mask)
        st.metric(label="Total Usable Host IP Allocations Allowed", value=f"{usable_hosts} addresses")
        
    st.write("---")
    st.markdown("### 🛠️ Cisco CLI Infrastructure Blueprint Reference")
    st.write("Beyond math, here is a production reference template illustrating how I configure VLAN isolation, 802.1Q trunking links, and Inter-VLAN routing interfaces within standard Cisco IOS CLI architectures:")
    
    cisco_snippet = """
! --- 1. CONFIGURE WORKSTATION VLAN ISOLATION BOUNDARIES ---
Switch# configure terminal
Switch(config)# vlan 10
Switch(config-vlan)# name PROD_WEB_TRAFFIC
Switch(config-vlan)# exit

! --- 2. MAP PHYSICAL PORTS INTERFACE TO VLAN PERIMETER ---
Switch(config)# interface fastEthernet 0/5
Switch(config-if)# switchport mode access
Switch(config-if)# switchport access vlan 10
Switch(config-if)# exit

! --- 3. CONFIGURE INTER-SWITCH 802.1Q TRUNKING AGGREGATION ---
Switch(config)# interface gigabitEthernet 0/1
Switch(config-if)# switchport mode trunk
Switch(config-if)# switchport trunk allowed vlan 10,20
Switch(config-if)# end
    """
    st.code(cisco_snippet, language="io")