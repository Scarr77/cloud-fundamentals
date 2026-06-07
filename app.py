import streamlit as st

# 1. Global Page Settings
st.set_page_config(
    page_title="Shadrick Carr | Engineering Hub", 
    page_icon="💻", 
    layout="wide"  # Wide mode layout for professional tracking interfaces
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
    
    # Renders the verification screenshot directly from your root images directory
    st.image(
        "images/aws-deployment-success.png", 
        caption="AWS Management EC2 Console verifying successful programmatic deployment of prod-web-server via Terraform.",
        use_container_width=True
    )
    
    st.write("\n")
    
    # Interactive outbound button directly to your repository
    st.link_button(
        "View Source Code & IaC Scripts on GitHub 🚀", 
        "https://github.com/Scarr77/cloud-fundamentals"
    )

# 5. PAGE 3: LINUX AUTOMATION
elif page == "Linux Automation":
    st.title("🐧 Automated Linux Systems Orchestration")
    st.subheader("Bash Scripting & Core Server Administration Modules")
    st.write("---")
    st.write("*(Stay tuned! We will map out your custom shell scripts and health monitoring systems logic here next).*")

# 6. PAGE 4: NETWORKING LABS
elif page == "Networking Labs":
    st.title("🎛️ Networking Architecture & Topologies")
    st.subheader("Cisco Infrastructure Switching & Subnetting Blueprints")
    st.write("---")
    st.write("*(Stay tuned! We will highlight your VLAN mappings, inter-VLAN trunking protocols, and subnet engineering modules here next).*")