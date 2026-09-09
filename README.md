# 📡 WireTapper 

<p align="center">
  <img src="https://raw.githubusercontent.com/h9zdev/WireTapper/main/images/WireTapper.png" alt="WireTapper" />
</p>

> [!NOTE]
> **Wireless OSINT & Signal Intelligence Platform**

WireTapper is a wireless OSINT tool designed to discover, map, and analyze radio-based devices using passive signal intelligence. It provides investigators, researchers, and security analysts with real-time visibility into the invisible wireless landscape around them.

WireTapper detects and correlates signals from common wireless technologies, helping users understand what devices exist, where they are likely located, and how they interact, without active intrusion.

WireTapper identifies leaked Wi-Fi network credentials based on privacy-protecting k-Anonymity query scheme.

<p align="center">
  🔗 <strong>Website:</strong>
  <a href="https://haybnz.web.app?utm_source=github.com">https://haybnz.web.app</a>
</p>

<p align="center">
  🔗 <strong>Blog on WireTapper:</strong>
  <a href="https://medium.com/@h9z/wire-tapper-wireless-osint-signal-intelligence-platform-e5104659a1cb?utm_source=github.com">
    Read on Medium
  </a>
</p>

<p align="center">
  <a href="https://github.com/sponsors/h9zdev">
    <img src="https://img.shields.io/badge/Make%20a%20Difference-Sponser%20My%20Work-6A1B9A?style=for-the-badge&logo=github&logoColor=white" alt="Support My Work" />
  </a>
</p>
<p align="center">
  <a href="https://github.com/h9zdev/WireTapper">
    <img src="https://img.shields.io/static/v1?label=Python&message=WireTapper&color=2A3E87&labelColor=6A7DA8&style=for-the-badge&logo=python&logoColor=white" />
  </a>
  <a href="https://github.com/h9zdev/WireTapper/issues">
    <img src="https://img.shields.io/github/issues/h9zdev/WireTapper?style=for-the-badge&color=8B0000&logo=github" />
  </a>
  <a href="https://github.com/h9zdev/WireTapper/network/members">
    <img src="https://img.shields.io/github/forks/h9zdev/WireTapper?style=for-the-badge&color=455A64&logo=github" />
  </a>
  <a href="https://github.com/h9zdev/WireTapper/stargazers">
    <img src="https://img.shields.io/github/stars/h9zdev/WireTapper?style=for-the-badge&color=FFD700&logo=github" />
  </a>
</p>

> [!Note]
> ## 🛰️ SocioSential — Social Media OSINT
> [![GitHub](https://img.shields.io/badge/GitHub-h9zdev%2FSocioSential-blue?logo=github&style=flat-square)](https://github.com/h9zdev/SocioSential)
> ## 📡 EthiFi — WiFi Deauther *(New Version)*
> [![GitHub](https://img.shields.io/badge/GitHub-h9zdev%2FEthiFi-green?logo=github&style=flat-square)](https://github.com/h9zdev/EthiFi)

<br>
## 📶 Supported Signal Intelligence & Modules

WireTapper can identify and analyze signals from:

*   **Wi-Fi Intelligence**: Access points, clients, and leaked credentials using a privacy-protecting k-Anonymity query scheme.
*   **Bluetooth LE & RPA Radar (`/btscan`)**: Live passive BLE device detection, RSSI path-loss distance estimation, and Resolvable Private Address (RPA) resolution using AES-128-ECB `ah()` cryptographic functions.
*   **Flock Safety & ALPR Surveillance Intelligence**: Dedicated management, download, and mapping module for Automated License Plate Reader (ALPR) camera networks and telemetry datasets.
*   **Multi-Format Telemetry Importer**: Drag-and-drop ingestion and smart column-mapping for custom field reports in CSV, KML, GeoJSON, SQLite (`.db`), and Excel formats.
*   **IoT & SCADA Infrastructure Reconnaissance**: Real-time geolocation scanning for exposed cameras, IoT nodes, and industrial control systems via Shodan & Censys Search API v2.
*   **USB SDR Receiver Detection**: Hardware link detection for attached Software Defined Radio dongles (RTL-SDR, HackRF One, Airspy) with frequency range monitoring.
*   **Cellular Infrastructure**: Cell tower location and beacon analysis using WiGLE and OpenCellID databases.
*   **Vehicles & Consumer Devices**: RF signals from smart vehicles, dashcams, IP cameras, wearables, and IoT appliances.


## 🔑 API Services

WireTapper integrates with several external intelligence services. Configure API credentials for enhanced discovery capabilities:

*   **[Wigle.net](https://wigle.net/)** – Wireless network and Bluetooth mapping and discovery (`WIGLE_API_NAME`, `WIGLE_API_TOKEN`).
*   **[OpenCellID](https://opencellid.org/)** – Open-source global database of cell towers (`OPENCELLID_API_KEY`).
*   **[Shodan](https://www.shodan.io/)** – Search engine for Internet-connected IoT and industrial devices (`SHODAN_API_KEY`).
*   **[Censys](https://censys.io/)** – Internet host and service search API v2 (`CENSYS_API_ID`, `CENSYS_API_SECRET`).
*   **[wpa-sec](https://wpa-sec.stanev.org)** – Distributed WPA-PSK auditor database integration.


## 🚀 Installation & Configuration

Follow these steps to set up and start WireTapper:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/h9zdev/WireTapper.git
   cd WireTapper
   ```

2. **Install dependencies:**
   It is recommended to use a Python virtual environment.
   ```bash
   pip install -r WireTapper.txt
   ```

3. **Configure API Keys:**

   API credentials are saved directly into a local SQLite database (`credentials.db`). You can configure them in one of two ways:

   *   **Option A: `.env` File (Automatic Seeding)**
       Create or edit the `.env` file in the root directory:
       ```env
       WIGLE_API_NAME=your_wigle_api_name
       WIGLE_API_TOKEN=your_wigle_api_token
       OPENCELLID_API_KEY=your_opencellid_api_key
       SHODAN_API_KEY=your_shodan_api_key
       CENSYS_API_ID=your_censys_api_id
       CENSYS_API_SECRET=your_censys_api_secret
       ```
       On application startup, `app.py` automatically initializes `credentials.db` and populates any missing keys from your `.env` file.

   *   **Option B: In-App Settings UI**
       Open the application dashboard in your browser and click the **Settings** gear icon in the navigation bar to enter or update your API credentials at runtime without restarting the server.

4. **Launch Application:**
   ```bash
   python app.py
   ```

   *   **Main Signal Intelligence Dashboard:** `http://localhost:8080/map-w` (or `http://localhost:8080/`)
   *   **Bluetooth LE & RPA Radar Interface:** `http://localhost:8080/btscan`

## 📷 Screenshots

![WireTapper Image 1](https://raw.githubusercontent.com/h9zdev/WireTapper/main/images/Wiretapper11.png)  
![WireTapper Image 2](https://raw.githubusercontent.com/h9zdev/WireTapper/main/images/Wiretapper34.png)  
![WireTapper Image 3](https://raw.githubusercontent.com/h9zdev/WireTapper/main/images/Wiretapper354.png)  
![WireTapper Image 4](https://raw.githubusercontent.com/h9zdev/WireTapper/main/images/Wiretapper55.png)  
![WireTapper Image 5](https://raw.githubusercontent.com/h9zdev/WireTapper/main/images/Wiretapper568.png)


## 📜 License

This project is licensed under the Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0) License. See the [LICENSE](LICENSE) file for more details.

**Unauthorized use is strictly prohibited.**

📧 Contact: singularat@protn.me

## ☕ Support

Donate via Monero: `45PU6txuLxtFFcVP95qT2xXdg7eZzPsqFfbtZp5HTjLbPquDAugBKNSh1bJ76qmAWNGMBCKk4R1UCYqXxYwYfP2wTggZNhq`

## 👥 Contributors and Developers

[<img src="https://avatars.githubusercontent.com/u/67865621?s=64&v=4" width="64" height="64" alt="haybnzz">](https://github.com/h9zdev)
 [<img src="https://avatars.githubusercontent.com/u/108749445?s=64&v=4"  width="64" height="64" alt="VaradScript">](https://github.com/varadScript)
## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=h9zdev/WireTapper&type=timeline&legend=bottom-right)](https://www.star-history.com/#h9zdev/WireTapper&type=timeline&legend=bottom-right)
