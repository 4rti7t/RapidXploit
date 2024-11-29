# 🚀 **ReconRapid - Automated Hacking Tool** 🛠️

**ReconRapid** ek advanced aur automated hacking tool hai jo **penetration testing**, **vulnerability exploitation**, aur **post-exploitation** ko streamline karta hai. Yeh tool **reconnaissance**, **exploit**, aur **post-exploitation** phases ko automatically handle karta hai, jisse aapko security assessments tezi se aur efficiently complete karne mein madad milti hai. 🔥

## ✨ **Features**:
- **🔍 Reconnaissance:** Automated Nmap scanning aur service detection.
- **⚡ Exploitation:** SMB vulnerabilities (EternalBlue) exploitation.
- **💥 Post-Exploitation:** Meterpreter sessions, hash dumping, aur persistence setup.
- **📱 User-Friendly:** Interactive IP input aur clear screen interface.
- **🔒 Secure:** Smooth error handling aur log management.
- **🌟 Branding:** Beautiful logo and tool banners for an awesome experience.

## 🚀 **Installation**:
To install and run **ReconRapid**, please follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/ReconRapid.git
    cd ReconRapid
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Ensure you have the following installed**:
    - **Nmap**: `sudo apt install nmap`
    - **Metasploit Framework**: `sudo apt install metasploit-framework`

---

## 🏃‍♂️ **Usage**:

1. **Run the tool**:
    ```bash
    python main.py
    ```

2. **Interactive IP Input**:
   Tool aap se IP address maangay ga, jise aap scan karna chahte hain. Example:

    ```
    [?] Enter Target IP Address: 192.168.1.100
    ```

3. **Phase 1: Reconnaissance**:
   Tool Nmap scan start karega aur target machine ke open ports aur services ko detect karega.

4. **Phase 2: Exploitation**:
   Agar reconnaissance successful ho gaya, toh tool SMB vulnerability exploit karne ki koshish karega.

5. **Phase 3: Post-Exploitation**:
   Agar exploit successful ho gaya, toh tool post-exploitation tasks execute karega, jaise hashdump aur persistence setup.

6. **Example Output**:
    ```bash
    ==============================
      ReconRapid - Hacking Tool
    ==============================

    [?] Enter Target IP Address: 192.168.1.100
    [+] Target IP: 192.168.1.100
    [*] Starting reconnaissance...
    [+] Scanning target: 192.168.1.100
    ...
    [+] Exploit Successful! Reverse shell obtained.
    [+] Post-exploitation complete.
    ```

---

## 💻 **Contributing**:
We welcome contributions! If you want to improve the tool or add more exploits, feel free to fork the repository and submit a pull request.

- 🔧 Fix bugs
- ✨ Add new features
- 📝 Improve documentation

---

## 📜 **Disclaimer**:
This tool is for **educational** purposes only. Use it only on systems you own or have explicit permission to test. The creators are not responsible for any illegal activities performed using this tool.

---

## 🛠️ **Dependencies**:
- **Nmap**: For port scanning and service detection.
- **Metasploit**: For exploitation using various payloads.

---

## 🔧 **License**:
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Happy Hacking! 🔥👨‍💻👩‍💻
